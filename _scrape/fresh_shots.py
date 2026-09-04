"""Download CURRENT App Store screenshots by scraping each app page (es storefront).

Screenshot assets live under PurpleSource buckets. Related-app thumbnails only get
64/128px variants; the app's own screenshots get large variants (>=230px). We keep
PurpleSource bases that appear with a large size variant, in DOM order.
"""
import io
import json
import os
import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(SRC, "..", "docs", "assets", "img"))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9,es;q=0.8",
}

APPS = {
    "igarage": "6544782316",
    "socialgym": "1614796934",
    "findmycar": "1605937769",
    "carkeep": "6479198249",
}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
        return r.read()


manifest = {}
for key, app_id in APPS.items():
    html = get(f"https://apps.apple.com/es/app/id{app_id}").decode("utf-8", errors="replace")
    order = []          # bases in DOM order
    max_size = {}       # base -> largest width variant seen
    for m in re.finditer(r"https://is\d-ssl\.mzstatic\.com/image/thumb/(PurpleSource[^\"'\s,>]+?)/(\d+)x\d+", html):
        base = f"https://is1-ssl.mzstatic.com/image/thumb/{m.group(1)}/"
        w = int(m.group(2))
        if base not in max_size:
            order.append(base)
            max_size[base] = w
        else:
            max_size[base] = max(max_size[base], w)
    bases = [b for b in order if max_size[b] >= 230]
    files = []
    for i, base in enumerate(bases[:6], 1):
        fname = f"app-{key}-shot{i}.png"
        with open(os.path.join(OUT, fname), "wb") as f:
            f.write(get(base + "460x0w.png"))
        files.append(fname)
    manifest[key] = files
    print(f"{key}: kept {len(bases)} of {len(order)} PurpleSource assets -> {len(files)} downloaded")

with io.open(os.path.join(SRC, "shots_manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)
