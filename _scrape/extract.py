"""Extract main content (headings, paragraphs, lists, images, links) from WP/Elementor pages."""
import html
import json
import os
import re
from html.parser import HTMLParser

SKIP_TAGS = {"script", "style", "noscript", "svg", "form"}
BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote", "figcaption"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.images = []
        self.links = []
        self.title = ""
        self.meta_desc = ""
        self.skip_depth = 0          # inside script/style/etc
        self.chrome_depth = 0        # inside header/footer/nav
        self.block_stack = []        # current block tag capture
        self.buf = []
        self.in_title = False
        self.cur_href = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if tag in ("header", "footer", "nav") or "elementor-location-header" in a.get("class", "") or "elementor-location-footer" in a.get("class", ""):
            self.chrome_depth += 1
            return
        if self.skip_depth or self.chrome_depth:
            return
        if tag == "title":
            self.in_title = True
        elif tag == "meta" and a.get("name") == "description":
            self.meta_desc = a.get("content", "")
        elif tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            if src and "wp-content/uploads" in src:
                self.images.append({"src": src, "alt": a.get("alt", "")})
                if self.block_stack:
                    self.buf.append(f"[IMG:{src}]")
        elif tag == "a":
            self.cur_href = a.get("href")
            if self.block_stack and self.cur_href:
                self.buf.append(f"[A:{self.cur_href}]")
        elif tag in BLOCK_TAGS:
            if self.block_stack:
                self._flush()
            self.block_stack.append(tag)
            self.buf = []

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag in ("header", "footer", "nav"):
            self.chrome_depth = max(0, self.chrome_depth - 1)
            return
        if self.skip_depth or self.chrome_depth:
            return
        if tag == "title":
            self.in_title = False
        elif tag == "a":
            if self.cur_href and self.block_stack:
                self.buf.append("[/A]")
            self.cur_href = None
        elif tag in BLOCK_TAGS and self.block_stack and self.block_stack[-1] == tag:
            self._flush()

    def _flush(self):
        tag = self.block_stack.pop()
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if text:
            self.out.append({"tag": tag, "text": text})
        self.buf = []

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.block_stack and not self.skip_depth and not self.chrome_depth:
            self.buf.append(data)


def main():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(src_dir, "extracted")
    os.makedirs(out_dir, exist_ok=True)
    for name in sorted(os.listdir(src_dir)):
        if not name.endswith(".html"):
            continue
        with open(os.path.join(src_dir, name), encoding="utf-8", errors="replace") as f:
            raw = f.read()
        ex = Extractor()
        ex.feed(raw)
        result = {
            "file": name,
            "title": ex.title.strip(),
            "meta_description": ex.meta_desc,
            "blocks": ex.out,
            "images": ex.images,
        }
        out_path = os.path.join(out_dir, name.replace(".html", ".json"))
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=1)
        print(f"{name}: {len(ex.out)} blocks, {len(ex.images)} images")


if __name__ == "__main__":
    main()
