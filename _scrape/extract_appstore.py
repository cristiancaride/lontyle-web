"""Extract name, description, icon and screenshots from downloaded App Store pages."""
import json
import os
import re

SRC = os.path.dirname(os.path.abspath(__file__))

for key in ("igarage", "socialgym", "findmycar", "carkeep"):
    path = os.path.join(SRC, f"appstore-{key}.html")
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    print(f"===== {key}")
    # schema.org JSON-LD
    for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', raw, re.S):
        try:
            data = json.loads(m.group(1))
        except Exception:
            continue
        if isinstance(data, dict) and data.get("@type") in ("SoftwareApplication", "MobileApplication"):
            print("NAME:", data.get("name"))
            desc = (data.get("description") or "").strip()
            print("DESC:", desc[:2500])
            shots = data.get("screenshot", [])
            if isinstance(shots, list):
                for s in shots[:6]:
                    print("SHOT:", s if isinstance(s, str) else s.get("url"))
            rating = data.get("aggregateRating") or {}
            print("RATING:", rating.get("ratingValue"), "count:", rating.get("reviewCount"))
    icon = re.search(r'property="og:image" content="([^"]+)"', raw)
    if icon:
        print("OG_IMAGE:", icon.group(1))
