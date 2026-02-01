from pathlib import Path
import re

README_PATH = Path("README.md")

def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.iterdir() if p.is_dir())

def scan_codetree():
    base = Path("Codetree")
    total = 0
    if base.exists():
        for day in base.iterdir():
            if day.is_dir():
                total += count_dirs(day)
    return total

def scan_leetcode():
    return count_dirs(Path("Leetcode"))

def scan_baekjoon():
    base = Path("백준")
    result = {}
    if base.exists():
        for tier in base.iterdir():
            if tier.is_dir():
                result[tier.name] = count_dirs(tier)
    return result

def scan_swea():
    base = Path("SWEA")
    result = {}
    if base.exists():
        for level in base.iterdir():
            if level.is_dir():
                result[level.name] = count_dirs(level)
    return result

def scan_programmers():
    base = Path("프로그래머스")
    total = 0
    if base.exists():
        for level in base.iterdir():
            if level.is_dir():
                total += count_dirs(level)
    return total

def update_readme(stats: dict):
    text = README_PATH.read_text(encoding="utf-8")

    replacements = {
        "Codetree": stats["codetree"],
        "LeetCode": stats["leetcode"],
        "Programmers": stats["programmers"],
        "Baekjoon": sum(stats["baekjoon"].values()),
        "SWEA": sum(stats["swea"].values()),
    }

    for key, value in replacements.items():
        pattern = rf"({key}\s*\|\s*)(\d+)"
        text = re.sub(
            pattern,
            lambda m, v=value: m.group(1) + str(v),
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
