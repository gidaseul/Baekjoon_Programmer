from pathlib import Path
import re

README_PATH = Path("README.md")

def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.iterdir() if p.is_dir())

def count_nested_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.rglob("*") if p.is_dir() and not any(p.iterdir()))

# Codetree: 날짜/문제명
def scan_codetree():
    base = Path("Codetree")
    total = 0
    for day in base.iterdir():
        if day.is_dir():
            total += count_dirs(day)
    return total

# Leetcode: 1문제 = 1폴더
def scan_leetcode():
    return count_dirs(Path("Leetcode"))

# 백준: 티어/Bronze/문제명
def scan_baekjoon():
    base = Path("백준")
    result = {}
    for tier in base.iterdir():
        if tier.is_dir():
            result[tier.name] = count_dirs(tier)
    return result

# SWEA: D1/D2/문제명
def scan_swea():
    base = Path("SWEA")
    result = {}
    for level in base.iterdir():
        if level.is_dir():
            result[level.name] = count_dirs(level)
    return result

# 프로그래머스: 레벨 하위 문제 폴더
def scan_programmers():
    base = Path("프로그래머스")
    total = 0
    for level in base.iterdir():
        if level.is_dir():
            total += count_dirs(level)
    return total

def update_readme(stats: dict):
    text = README_PATH.read_text(encoding="utf-8")

    def replace(section, value):
        return re.sub(
            rf"({section}\s*:\s*)(\d+)",
            rf"\1{value}",
            text
        )

    replacements = {
        "Codetree": stats["codetree"],
        "LeetCode": stats["leetcode"],
        "Programmers": stats["programmers"],
        "Baekjoon": sum(stats["baekjoon"].values()),
        "SWEA": sum(stats["swea"].values()),
    }

    for k, v in replacements.items():
        text = re.sub(
            rf"({k}\s*\|\s*)(\d+)",
            rf"\1{v}",
            text
        )

    README_PATH.write_text(text, encoding="utf-8")

def main():
    stats = {
        "codetree": scan_codetree(),
        "leetcode": scan_leetcode(),
        "programmers": scan_programmers(),
        "baekjoon": scan_baekjoon(),
        "swea": scan_swea(),
    }

    update_readme(stats)

if __name__ == "__main__":
    main()
