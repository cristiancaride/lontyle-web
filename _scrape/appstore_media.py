"""Pull icon + screenshot URLs from App Store pages and download them."""
import os
import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(SRC, "..", "docs", "assets", "img"))

APPS = ("igarage", "socialgym", "findmycar", "carkeep")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch(url, dest):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as r, open(dest, "wb") as f:
        f.write(r.read())


for key in APPS:
    with open(os.path.join(SRC, f"appstore-{key}.html"), encoding="utf-8", errors="replace") as f:
        raw = f.read()

    # icon: webp/png square icon urls (AppIcon marketing asset)
    icons = re.findall(r'(https://is\d-ssl\.mzstatic\.com/image/thumb/[^"\s,]+AppIcon[^"\s,]+/230x0w\.webp)', raw)
    # screenshots: source srcset entries, screenshots have SS or Placeholder paths ending 600x0w
    shots = re.findall(r'(https://is\d-ssl\.mzstatic\.com/image/thumb/[^"\s,]+/600x0w\.webp)', raw)
    # dedupe preserving order, drop icon urls from shots
    seen, clean = set(), []
    for s in shots:
        if s in seen or "AppIcon" in s:
            continue
        seen.add(s)
        clean.append(s)

    print(f"===== {key}: {len(icons)} icons, {len(clean)} shots")
    if icons:
        dest = os.path.join(OUT, f"appstore-{key}-icon.webp")
        fetch(icons[0], dest)
        print("  icon ->", os.path.basename(dest))
    for i, s in enumerate(clean[:6], 1):
        dest = os.path.join(OUT, f"appstore-{key}-shot{i}.webp")
        fetch(s, dest)
        print(f"  shot{i} ->", os.path.basename(dest))
