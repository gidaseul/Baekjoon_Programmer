import os
import subprocess
from datetime import datetime

# === 기본 설정 ===
PLATFORMS = {
    "Baekjoon": "백준",
    "Programmers": "프로그래머스",
    "SWEA": "SWEA",
    "Codetree": "Codetree",
    "LeetCode": "Leetcode",
}

EXTENSIONS = (".py", ".java", ".cpp", ".c")

DIFFICULTY_KEYWORDS = {
    "Gold": ["Gold"],
    "Silver": ["Silver"],
    "Bronze": ["Bronze"],
    "Level": ["level", "Level", "Lv"],
}

# === 유틸 함수 ===
def count_files(path):
    count = 0
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(EXTENSIONS):
                count += 1
    return count

def count_difficulty(path):
    result = {k: 0 for k in DIFFICULTY_KEYWORDS}
    for root, _, files in os.walk(path):
        for f in files:
            for k, keywords in DIFFICULTY_KEYWORDS.items():
                if any(word in root or word in f for word in keywords):
                    result[k] += 1
                    break
    return result

def last_commit_date(path):
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", path],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except:
        return "N/A"

# === 통계 계산 ===
platform_rows = []
difficulty_total = {k: 0 for k in DIFFICULTY_KEYWORDS}
total_count = 0
latest_commit = "N/A"

for name, folder in PLATFORMS.items():
    if not os.path.exists(folder):
        continue

    count = count_files(folder)
    diff = count_difficulty(folder)
    last = last_commit_date(folder)

    total_count += count
    for k in diff:
        difficulty_total[k] += diff[k]

    platform_rows.append((name, count, last))
    latest_commit = max(latest_commit, last)

# === README 내용 생성 ===
stats_md = ["| Platform | Problems | Last Commit |", "|---|---:|---|"]
for name, cnt, last in platform_rows:
    stats_md.append(f"| {name} | {cnt} | {last} |")

stats_md.append(f"\n**Total:** {total_count}")
stats_md.append(
    " / ".join(f"{k}: {v}" for k, v in difficulty_total.items())
)

badges_md = [
    f"![{name}](https://img.shields.io/badge/{name}-{cnt}-blue)"
    for name, cnt, _ in platform_rows
]

updated_md = f"🕒 Last Auto Update: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"

# === README 치환 ===
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

def replace_block(text, start, end, content):
    return text.split(start)[0] + start + "\n" + content + "\n" + end + text.split(end)[1]

readme = replace_block(
    readme,
    "<!-- STATS:START -->",
    "<!-- STATS:END -->",
    "\n".join(stats_md),
)

readme = replace_block(
    readme,
    "<!-- BADGES:START -->",
    "<!-- BADGES:END -->",
    " ".join(badges_md),
)

readme = replace_block(
    readme,
    "<!-- UPDATED:START -->",
    "<!-- UPDATED:END -->",
    updated_md,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
