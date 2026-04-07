#!/usr/bin/env python3
"""
Caveman Memory Orchestrator (Chinese Edition)

Usage:
    python memory/compress.py <filepath>
"""

import subprocess
import sys
from pathlib import Path
from typing import List

from .detect import should_compress
from .validate import validate

MAX_RETRIES = 2


# ---------- Claude Calls ----------


def call_claude(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["claude", "--print"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Claude call failed:\n{e.stderr}")


def build_compress_prompt(original: str) -> str:
    return f"""
将这个 markdown 压缩成原始人(ultra-caveman)格式。

严格规则 (STRICT RULES):
- 绝不要修改 ``` 代码块内部的任何内容
- 绝不要修改内联代码(`反引号`)内部的任何内容
- 完全保留所有的 URLs
- 完全保留所有的标题 (headings)
- 保留文件路径和终端命令

仅压缩自然语言，并使用极其精简的中文原始人语法。

文本 (TEXT):
{original}
"""


def build_fix_prompt(original: str, compressed: str, errors: List[str]) -> str:
    errors_str = "\n".join(f"- {e}" for e in errors)
    return f"""你正在修复一个被超级超级超级原始人压缩的 markdown 文件。发现了特定的验证错误。

关键规则 (CRITICAL RULES):
- 不要重新压缩或重述带有新意图的文件
- 只修复列出的错误 — 其他所有部分保持原样
- 原文仅作为参考提供（用于恢复丢失的内容）
- 在所有未触及的部分保留原始人风格

需要修复的错误 (ERRORS TO FIX):
{errors_str}

如何修复 (HOW TO FIX):
- 丢失的URL: 从原文件中找到它，并准确放回压缩版应有的位置
- 代码块不匹配: 从原文件中找到完全相同的代码块，并在压缩版中恢复它
- 标题不匹配: 从原文件中恢复完全相同的标题文字到压缩版本中
- 不要修改未在错误中提及的任何部分

原文(仅供参考) (ORIGINAL):
{original}

压缩版(需修复) (COMPRESSED):
{compressed}

只返回修复后的压缩文件。不要解释。
"""


# ---------- Core Logic ----------


def compress_file(filepath: Path) -> bool:
    print(f"📄 Processing: {filepath}")

    if not should_compress(filepath):
        print("⚠️ Skipping (not natural language)")
        return False

    original_text = filepath.read_text(errors="ignore")
    backup_path = filepath.with_name(filepath.stem + ".original.md")

    # Step 1: Compress
    print("🧠 Compressing with Claude...")
    compressed = call_claude(build_compress_prompt(original_text))

    # Save original as backup, write compressed to original path
    backup_path.write_text(original_text)
    filepath.write_text(compressed)

    # Step 2: Validate + Retry
    for attempt in range(MAX_RETRIES):
        print(f"\n🔍 Validation attempt {attempt + 1}")

        result = validate(backup_path, filepath)

        if result.is_valid:
            print("✅ Validation passed")
            break

        print("❌ Validation failed:")
        for err in result.errors:
            print(f"   - {err}")

        if attempt == MAX_RETRIES - 1:
            # Restore original on failure
            filepath.write_text(original_text)
            backup_path.unlink(missing_ok=True)
            print("❌ Failed after retries — original restored")
            return False

        print("🛠 Fixing with Claude...")
        compressed = call_claude(
            build_fix_prompt(original_text, compressed, result.errors)
        )
        filepath.write_text(compressed)

    return True


# ---------- Main ----------


def main():
    if len(sys.argv) != 2:
        print("Usage: python memory/compress.py <filepath>")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        sys.exit(1)

    success = compress_file(filepath)

    if success:
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
