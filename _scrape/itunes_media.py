"""Fetch app metadata (icon, screenshots) via iTunes Lookup API and download media."""
import json
import os
import ssl
import urllib.request

CTX = ssl.create_default_context()
SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(SRC, "..", "docs", "assets", "img"))

APPS = {
    "igarage": "6544782316",
    "socialgym": "1614796934",
    "findmycar": "1605937769",
    "carkeep": "6479198249",
}
HEADERS = {"User-Agent": "Mozilla/5.0"}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
        return r.read()


meta = {}
for key, app_id in APPS.items():
    data = json.loads(get(f"https://itunes.apple.com/lookup?id={app_id}&country=gm"))
    if not data["results"]:
        print(f"{key}: NOT FOUND")
        continue
    r = data["results"][0]
    meta[key] = {
        "name": r["trackName"],
        "url": r["trackViewUrl"],
        "genres": r.get("genres"),
        "rating": r.get("averageUserRating"),
        "ratingCount": r.get("userRatingCount"),
        "version": r.get("version"),
        "releaseDate": r.get("releaseDate"),
        "currentVersionDate": r.get("currentVersionReleaseDate"),
    }
    icon = r.get("artworkUrl512") or r.get("artworkUrl100")
    if icon:
        with open(os.path.join(OUT, f"app-{key}-icon.png"), "wb") as f:
            f.write(get(icon))
    shots = r.get("screenshotUrls", [])[:5]
    for i, s in enumerate(shots, 1):
        with open(os.path.join(OUT, f"app-{key}-shot{i}.png"), "wb") as f:
            f.write(get(s))
    print(f"{key}: {r['trackName']} | icon + {len(shots)} shots | rating {r.get('averageUserRating')} ({r.get('userRatingCount')})")

with open(os.path.join(SRC, "itunes_meta.json"), "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=1)
