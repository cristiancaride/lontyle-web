"""Download all referenced wp-content images into docs/assets/img with safe names."""
import json
import os
import re
import ssl
import unicodedata
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()  # site cert is expired
SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(SRC, "..", "docs", "assets", "img"))
os.makedirs(OUT, exist_ok=True)

urls = set()
for name in os.listdir(os.path.join(SRC, "extracted")):
    with open(os.path.join(SRC, "extracted", name), encoding="utf-8") as f:
        data = json.load(f)
    for img in data["images"]:
        urls.add(img["src"])
    for b in data["blocks"]:
        for m in re.findall(r"\[IMG:([^\]]+)\]", b["text"]):
            urls.add(m)


def safe_name(url):
    base = urllib.parse.unquote(url.rsplit("/", 1)[-1])
    base = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode()
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", base)
    return re.sub(r"-{2,}", "-", base).strip("-").lower()


mapping = {}
for url in sorted(urls):
    fname = safe_name(url)
    # avoid collisions
    stem, ext = os.path.splitext(fname)
    i = 2
    while fname in mapping.values() and not os.path.exists(os.path.join(OUT, fname)):
        fname = f"{stem}-{i}{ext}"
        i += 1
    dest = os.path.join(OUT, fname)
    if not os.path.exists(dest):
        enc = urllib.parse.quote(url, safe=":/?&=%")
        try:
            with urllib.request.urlopen(enc, context=CTX, timeout=30) as r, open(dest, "wb") as f:
                f.write(r.read())
            print(f"OK  {fname}")
        except Exception as e:
            print(f"ERR {url}: {e}")
            continue
    mapping[url] = fname

with open(os.path.join(SRC, "img_map.json"), "w", encoding="utf-8") as f:
    json.dump(mapping, f, ensure_ascii=False, indent=1)
print(f"{len(mapping)} images mapped")
