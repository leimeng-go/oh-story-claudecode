import re, sys
from pathlib import Path

lo, hi = int(sys.argv[1]), int(sys.argv[2])
base = Path(r"C:\Users\19558\myspace\oh-story-claudecode\demo\拆文库\长夜余火\章节")
tone_enum = set("紧张 轻松 悲伤 热血 爽 甜 温馨 恐怖 压抑 其他".split())
tag_enum = set("爱情 亲情 友情 权力 金钱 成长 复仇 悬念 搞笑 热血 日常 其他".split())
bad = 0
total_p = 0
for n in range(lo, hi + 1):
    f = base / f"第{n}章_摘要.md"
    if not f.exists():
        print(f"第{n}章: 缺失")
        bad += 1
        continue
    t = f.read_text(encoding="utf-8")
    p = len(re.findall(r"(?m)^P\d+ ", t))
    tone = re.findall(r"基调：(\S+)", t)
    tag = re.findall(r"主题标签(\S+?)\s*\|", t)
    braces = t.count("{") + t.count("}")
    head = "**概要**" in t
    bad_tone = [x for x in tone if x not in tone_enum]
    bad_tag = [x for x in tag if x not in tag_enum]
    ok = p == len(tone) == len(tag) and braces == 0 and head and not bad_tone and not bad_tag
    total_p += p
    status = "OK" if ok else f"FAIL p={p} tone={len(tone)} tag={len(tag)} braces={braces} head={head} badtone={bad_tone} badtag={bad_tag}"
    if not ok:
        bad += 1
    print(f"第{n}章: P={p} [{status}]")
print(f"range {lo}-{hi}: bad={bad}, totalP={total_p}")
