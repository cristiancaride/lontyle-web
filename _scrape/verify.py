"""Check that every root-relative href/src in docs/ points to an existing file."""
import os
import re

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
errors = 0
checked = set()
for dirpath, _, files in os.walk(DOCS):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        path = os.path.join(dirpath, fn)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        for m in re.finditer(r'(?:href|src)="(/[^"#?]*)', content):
            url = m.group(1)
            if url in checked:
                continue
            checked.add(url)
            target = os.path.join(DOCS, url.strip("/").replace("/", os.sep))
            ok = os.path.isfile(target) or os.path.isfile(os.path.join(target, "index.html"))
            if not ok:
                print(f"BROKEN {url}  (first seen in {os.path.relpath(path, DOCS)})")
                errors += 1
print(f"{len(checked)} unique internal URLs checked, {errors} broken")
