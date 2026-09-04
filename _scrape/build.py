# -*- coding: utf-8 -*-
"""Static site generator for lontylegames.com — reads _scrape/extracted/*.json, writes docs/."""
import html
import json
import os
import re

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SRC, ".."))
DOCS = os.path.join(ROOT, "docs")
DOMAIN = "https://www.lontylegames.com"

with open(os.path.join(SRC, "img_map.json"), encoding="utf-8") as f:
    IMG_MAP = json.load(f)

APPLE_DEV = "https://apps.apple.com/developer/cristian-caride-rodriguez/id1605937771"

# ---------------------------------------------------------------- live apps
APPS = [
    {
        "slug": "igarage-workshop-manager",
        "name": "iGarage: Workshop Manager",
        "short": "The ideal app for workshops to optimize vehicle management and client communication. Add vehicles, record details, contact clients.",
        "cats": ["iOS Apps"], "new": True,
        "icon": "app-igarage-icon.png",
        "screens": [f"app-igarage-shot{i}.png" for i in range(1, 5)],
        "apple": "https://apps.apple.com/app/id6544782316", "google": None,
        "category": "BusinessApplication",
        "meta": "iGarage is the ideal app for workshops looking to optimize vehicle management and enhance communication with their clients.",
        "body": """<p>iGarage is the ideal app for workshops looking to optimize vehicle management and enhance communication with their clients. With an intuitive interface, you can quickly add vehicles and record essential details such as license plate, make, model, and client phone numbers.</p>
<h2>Key Features</h2>
<ul>
<li>🔧 <strong>Complete workshop management:</strong> easily add and organize vehicles.</li>
<li>📞 <strong>Direct communication:</strong> quickly contact your clients.</li>
<li>📋 <strong>Detailed information:</strong> record license plate, make, model, and phone details.</li>
<li>🔒 <strong>Transit security:</strong> data is encrypted during transmission.</li>
</ul>
<p>Transform the way you manage your workshop and provide exceptional service to your clients with iGarage. Discover efficiency and organization today!</p>""",
    },
    {
        "slug": "socialfit-social-fitness",
        "name": "Social Gym: Workout Tracker",
        "short": "The social network for people who lift. Find your next routine, train guided with timed rests, and compete with your friends for XP.",
        "cats": ["iOS Apps"], "new": True,
        "icon": "app-socialgym-icon.png",
        "screens": [f"app-socialgym-shot{i}.png" for i in range(1, 6)],
        "apple": "https://apps.apple.com/app/id1614796934", "google": None,
        "category": "HealthApplication",
        "meta": "Social Gym is the social network for people who lift. Find your next routine, train guided with timed rests, and compete with your friends for XP.",
        "body": """<p>Social Gym is the social network for people who lift. Find your next routine, train guided with timed rests, and compete with your friends for XP.</p>
<h2>Find your routine</h2>
<ul>
<li>💪 Thousands of community routines, filtered by goal, level, days and equipment.</li>
<li>🧍 Muscle analysis with an interactive 3D body: see what each routine works before you start.</li>
<li>🔀 Remix any routine and make it yours.</li>
</ul>
<h2>Train guided</h2>
<ul>
<li>⏰ Sets, reps and timed rests with lock-screen alerts.</li>
<li>📈 Set-by-set weight logging and automatic personal records.</li>
<li>💓 Apple Health sync.</li>
</ul>
<h2>Progress like a game</h2>
<ul>
<li>✨ Earn XP with every workout, level up and protect your weekly streak.</li>
<li>🏅 Achievements, history with charts and a home-screen widget.</li>
</ul>
<h2>Compete with your community</h2>
<ul>
<li>🥊 Weekly 1v1 duels: whoever earns more XP wins.</li>
<li>🏆 Monthly XP race with a podium and champion.</li>
<li>🧱 The Wall: share your wins with your gym and community.</li>
</ul>
<h2>AI Coach 24/7</h2>
<ul>
<li>🤖 Training, nutrition and recovery questions answered instantly.</li>
<li>🧠 AI routine generator tailored to you.</li>
</ul>
<h2>Elite Plan — one-time purchase, no subscription</h2>
<ul>
<li>🚀 Everything unlimited: saves, AI Coach and generator.</li>
<li>📊 Advanced analytics, CSV export, pro calculators and zero ads.</li>
</ul>
<p>Download Social Gym and train with your community.</p>""",
    },
    {
        "slug": "car-parking-app",
        "name": "Find My Car: Parked Car Finder",
        "short": "Never lose your parked car again. Save your spot with one tap and get guided straight back — offline, private, no subscriptions.",
        "cats": ["iOS Apps", "Android Apps"], "new": False,
        "icon": "app-findmycar-icon.png",
        "screens": [f"app-findmycar-shot{i}.png" for i in range(1, 6)],
        "apple": "https://apps.apple.com/app/id1605937769",
        "google": "https://play.google.com/store/apps/details?id=com.lontylegames.simpleparkingappfree",
        "category": "UtilitiesApplication",
        "meta": "Never lose your parked car again. Find My Car saves your parking spot with a single tap and guides you straight back — no GPS tracker, no monthly fees.",
        "body": """<p><strong>Never lose your parked car again.</strong> Find My Car saves your parking spot with a single tap and guides you straight back — no expensive GPS tracker, no monthly fees, no complicated setup. Just park, tap, and relax.</p>
<p>Whether you're in a massive mall parking lot, a crowded stadium, an airport, or an unfamiliar city, Find My Car remembers exactly where you left your vehicle so you don't have to.</p>
<h2>How it works</h2>
<ul>
<li>🚗 Park your car and tap once to save the location.</li>
<li>📍 A pin drops on the map with precise GPS coordinates.</li>
<li>🧭 When you return, the app guides you right back to your spot.</li>
</ul>
<h2>Key features</h2>
<ul>
<li>👆 One-tap save — the fastest way to mark your spot.</li>
<li>📡 Works fully offline — no signal needed.</li>
<li>🎯 Precise GPS coordinates for pinpoint accuracy.</li>
<li>🕓 Parking history to revisit previous spots.</li>
<li>⌚ Apple Watch support — find your car from your wrist.</li>
<li>👪 Share your location with family and friends.</li>
<li>🔋 Battery-friendly and lightweight.</li>
<li>📌 Save any location: your car, bike, or a spot at the mall.</li>
</ul>
<h2>Why Find My Car</h2>
<p>Unlike expensive GPS trackers or devices that charge monthly fees, Find My Car is simple, private, and works anywhere. No hardware, no subscriptions, no hassle.</p>
<p>Download Find My Car today and park with peace of mind.</p>""",
    },
    {
        "slug": "carkeep-vehicle-manager",
        "name": "CarKeep – Vehicle Manager",
        "short": "Your ultimate vehicle management tool. Track maintenance, log fuel expenses and set service reminders — effortlessly.",
        "cats": ["iOS Apps"], "new": False,
        "icon": "app-carkeep-icon.png",
        "screens": [f"app-carkeep-shot{i}.png" for i in range(1, 5)],
        "apple": "https://apps.apple.com/app/id6479198249", "google": None,
        "category": "UtilitiesApplication",
        "meta": "CarKeep is your ultimate vehicle management tool, designed to simplify car maintenance and expense tracking.",
        "body": """<p>CarKeep is your ultimate vehicle management tool, designed to simplify car maintenance and expense tracking. With powerful features and an intuitive design, CarKeep helps you stay on top of your car's health effortlessly.</p>
<h2>Key Features</h2>
<ul>
<li>🔧 <strong>Vehicle maintenance tracking:</strong> keep a record of your car's maintenance history, including services, repairs, and upcoming tasks.</li>
<li>⛽ <strong>Fuel expense management:</strong> easily log and monitor your fuel expenses and understand your vehicle's fuel economy.</li>
<li>⏰ <strong>Service reminders:</strong> set reminders for upcoming services so your car stays in top condition.</li>
<li>📱 <strong>User-friendly interface:</strong> clean and intuitive, manage your car's information on the go.</li>
</ul>
<p>Download CarKeep now and take control of your vehicle maintenance and expenses with ease! 🚀</p>""",
    },
]

# ---------------------------------------------------------------- archived games
GAMES = [
    {
        "slug": "big-city-roleplay",
        "name": "Big City Roleplay: Real Life Simulator City Game",
        "short": "Urban life like never before: choose your role, master your profession, and explore endless adventures in a living city.",
        "cats": ["Android Games"],
        "icon": "role-playing-icon-first-1-512x500.png",
        "screens": ["roleplay-game-1024x512.jpg", "real-life-simulator-1024x512.jpg", "roleplaying-1024x512.jpg",
                    "city-game-1024x512.jpg", "big-city-life-simulator-1024x512.jpg", "real-life-game-1024x512.jpg",
                    "real-life-simulator-game-1024x512.jpg"],
        "portrait": False,
        "json": "title_big-city-roleplay.json",
        "meta": "Big City Roleplay: Real Life Simulator City Game — a Unity city-life RP game by Lontyle Apps (archived).",
    },
    {
        "slug": "car-parking-driving-roleplaying-game",
        "name": "Car Parking & Driving: Roleplaying Game",
        "short": "A multiplayer driving simulator fused with role-play: 40+ cars, jobs, apartments and an open city to live a virtual life.",
        "cats": ["Android Games"],
        "icon": "car-game-icon_1-800x500.png",
        "screens": ["sports-1024x585.jpg", "procedural24h-1024x585.jpg", "jobs-1024x585.jpg", "flats-1024x585.jpg",
                    "charactercustomisation-1024x585.jpg", "cargarage-1024x585.jpg",
                    "carconcessionaire-1024x585.jpg", "activities-1024x585.jpg"],
        "portrait": False,
        "json": "title_car-parking-driving-roleplaying-game.json",
        "meta": "Car Parking & Driving: Roleplaying Game — a multiplayer driving and role-play simulator by Lontyle Apps (archived).",
    },
    {
        "slug": "building-stack-block-builder-game",
        "name": "Building Stack – Block Builder Game",
        "short": "Stack your way to the sky! An addictive 3D arcade block-stacking challenge, free and playable offline.",
        "cats": ["Android Games"],
        "icon": "image-1-800x500.png",
        "screens": ["embeddedimage-1.png", "embeddedimage-2.png"],
        "portrait": True,
        "json": "title_building-stack-block-builder-game.json",
        "meta": "Building Stack – Block Builder Game, an addictive 3D block-stacking arcade game by Lontyle Apps (archived).",
    },
]

ALL_TITLES = APPS + GAMES

ARTICLES = [
    ("privacy-policy", "privacy-policy.json"),
    ("big-city-roleplay-privacy-policy", "big-city-roleplay-privacy-policy.json"),
    ("big-city-roleplay-terms-conditions", "big-city-roleplay-terms-conditions.json"),
    ("big-multiplayer-city-roleplay-privacy-policy", "big-multiplayer-city-roleplay-privacy-policy.json"),
    ("carkeep-privacy-policy", "carkeep-privacy-policy.json"),
    ("code-tip-privacy-policy", "code-tip-privacy-policy.json"),
    ("igarage-privacy-policy", "igarage-privacy-policy.json"),
    ("simple-parking-app-privacy-policy", "simple-parking-app-privacy-policy.json"),
    ("simple-parking-app-terms-conditions", "simple-parking-app-terms-conditions.json"),
    ("simple-parking-app-free-privacy-policy", "simple-parking-app-free-privacy-policy.json"),
    ("simple-parking-app-free-terms-conditions", "simple-parking-app-free-terms-conditions.json"),
    ("simple-parking-app-ios-privacy-policy", "simple-parking-app-ios-privacy-policy.json"),
    ("social-gym-app-privacy-policy", "social-gym-app-privacy-policy.json"),
    ("social-gym-app-terms-conditions", "social-gym-app-terms-conditions.json"),
    ("how-to-play-big-city-roleplay", "how-to-play-big-city-roleplay.json"),
    ("how-to-play-little-city-island-roleplay", "how-to-play-little-city-island-roleplay.json"),
    ("best-parking-app-android-ios", "best-parking-app-android-ios.json"),
]

REDIRECTS = {
    "our-studio": "/about-us/",
    "contact-us": "/contact/",
    "get-in-touch": "/contact/",
    "shop": "/our-games/",
    "our-portfolio": "/our-games/",
    "our-services": "/about-us/",
    "title": "/our-games/",
    "title/codetip-daily-coding-tips": "/our-games/",
    "portfolio-category/android-apps": "/our-games/",
    "portfolio-category/android-games": "/our-games/",
    "portfolio-category/ios-apps": "/our-games/",
    "portfolio-category/new": "/our-games/",
}

PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.6 1.8 13.7 12 3.6 22.2c-.4-.3-.6-.8-.6-1.4V3.2c0-.6.2-1.1.6-1.4zm11.5 8.8 2.6-2.6 3.3 1.9c1 .6 1 2 0 2.6l-3.3 1.9-2.6-2.6-.6-.6.6-.6zM5.2 1.3l11 6.3-2.5 2.4L5.2 1.3zm0 21.4L13.7 14l2.5 2.4-11 6.3z"/></svg>'
APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.05 12.54c-.03-2.9 2.37-4.29 2.48-4.36-1.35-1.98-3.46-2.25-4.2-2.28-1.79-.18-3.5 1.05-4.4 1.05-.9 0-2.3-1.03-3.79-1-1.95.03-3.75 1.13-4.75 2.88-2.03 3.52-.52 8.72 1.46 11.58.97 1.4 2.12 2.96 3.63 2.9 1.46-.06 2.01-.94 3.77-.94s2.26.94 3.8.91c1.57-.03 2.57-1.42 3.53-2.83 1.11-1.62 1.57-3.19 1.6-3.27-.04-.02-3.07-1.18-3.13-4.64zM14.16 4.1c.8-.97 1.34-2.32 1.19-3.66-1.15.05-2.55.77-3.38 1.74-.74.86-1.39 2.23-1.22 3.55 1.29.1 2.6-.65 3.41-1.63z"/></svg>'

EXT = ' target="_blank" rel="noopener"'

MARQUEE_ITEMS = ["Unity", "Swift", "SwiftUI", "C#", "Android Studio", "iOS", "Java", "Multiplayer", "Game Design", "App Store"]


# ---------------------------------------------------------------- helpers
def read_json(name):
    with open(os.path.join(SRC, "extracted", name), encoding="utf-8") as f:
        return json.load(f)


def localize_url(url):
    url = url.replace("https://www.lontylegames.com", "").replace("http://www.lontylegames.com", "")
    return url or "/"


def render_inline(text):
    text = html.escape(text, quote=False)

    def img_sub(m):
        local = IMG_MAP.get(m.group(1))
        return f'<img src="/assets/img/{local}" alt="" loading="lazy">' if local else ""

    def a_open(m):
        url = m.group(1)
        if "lontylegames.com" in url or url.startswith("/"):
            return f'<a href="{localize_url(url)}">'
        return f'<a href="{url}"{EXT}>'

    text = re.sub(r"\[IMG:([^\]]+)\]", img_sub, text)
    text = re.sub(r"\[A:([^\]]+)\]", a_open, text)
    return text.replace("[/A]", "</a>")


def b_text(b):
    return re.sub(r"\s+", " ", b["text"]).strip()


def slice_content(blocks):
    start = 0
    for i, b in enumerate(blocks):
        if b["tag"] == "h1":
            start = i
            break
    end = len(blocks)
    for i in range(start + 1, len(blocks)):
        if b_text(blocks[i]) in ("MORE RELEASES", "Our Newsletter"):
            end = i
            break
    return blocks[start:end]


def render_blocks(blocks, skip_first_h1=True):
    out, in_list = [], False
    first_h1_done = False
    for b in blocks:
        tag, txt = b["tag"], render_inline(b["text"])
        if tag == "h1":
            if skip_first_h1 and not first_h1_done:
                first_h1_done = True
                continue
            tag = "h2"
        if tag == "li":
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{txt}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        out.append(f"<{tag}>{txt}</{tag}>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def clean_title(raw):
    return re.sub(r"\s*-\s*Lontyle (Apps & Games|Games|Apps)\s*$", "", raw).strip()


# ---------------------------------------------------------------- layout
def page(title, description, body, path="/", active="", og_image=None, jsonld=None, lang="en", extra_head=""):
    def nav_link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    esc_title = html.escape(title, quote=True)
    esc_desc = html.escape(description or "", quote=True)
    og_image = og_image or "/assets/img/tamano-personalizado-17.png"
    desc_tag = f'\n  <meta name="description" content="{esc_desc}">' if description else ""
    ld = ""
    if jsonld:
        blocks = jsonld if isinstance(jsonld, list) else [jsonld]
        for b in blocks:
            ld += f'\n  <script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
    app_links = "\n".join(
        f'        <li><a href="/title/{a["slug"]}/">{html.escape(a["name"], quote=False)}</a></li>' for a in APPS
    )
    game_links = "\n".join(
        f'        <li><a href="/title/{g["slug"]}/">{html.escape(g["name"], quote=False)}</a></li>' for g in GAMES
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc_title}</title>{desc_tag}
  <meta name="theme-color" content="#06070d">
  <meta name="author" content="Cristian Caride">
  <link rel="canonical" href="{DOMAIN}{path}">{extra_head}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{'es_ES' if lang == 'es' else 'en_US'}">
  <meta property="og:site_name" content="Lontyle Apps">
  <meta property="og:title" content="{esc_title}">
  <meta property="og:description" content="{esc_desc}">
  <meta property="og:url" content="{DOMAIN}{path}">
  <meta property="og:image" content="{DOMAIN}{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc_title}">
  <meta name="twitter:description" content="{esc_desc}">
  <meta name="twitter:image" content="{DOMAIN}{og_image}">{ld}
  <link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32">
  <link rel="icon" href="/assets/img/favicon-192.png" sizes="192x192">
  <link rel="apple-touch-icon" href="/assets/img/favicon-192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Unbounded:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<div class="bg-scene" aria-hidden="true">
  <i class="orb o1"></i><i class="orb o2"></i><i class="orb o3"></i><i class="orb o4"></i>
</div>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="bar">
    <a class="brand" href="/" aria-label="Lontyle Apps — Home">
      <span class="wordmark">Lontyle<em>Apps</em></span>
    </a>
    <nav class="site-nav" aria-label="Main navigation">
      {nav_link("/", "Home", "home")}
      {nav_link("/our-games/", "Games &amp; Apps", "games")}
      {nav_link("/about-us/", "About", "about")}
      {nav_link("/contact/", "Contact", "contact")}
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-cta" data-reveal>
      <h2>Got an idea? <span class="grad">Let's talk.</span></h2>
      <a class="btn primary" href="mailto:lontyle@gmail.com">lontyle@gmail.com</a>
    </div>
    <div class="cols">
      <div>
        <span class="wordmark big">Lontyle<em>Apps</em></span>
        <p>Indie studio with game-design roots, now crafting native iOS apps — designed, coded and shipped in-house.</p>
      </div>
      <div>
        <h4>Apps</h4>
        <ul>
{app_links}
        </ul>
      </div>
      <div>
        <h4>Game archive</h4>
        <ul>
{game_links}
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about-us/">About Us</a></li>
          <li><a href="/our-games/">Games &amp; Apps</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacy-policy/">Privacy Policy</a></li>
          <li><a href="{APPLE_DEV}"{EXT}>App Store profile</a></li>
        </ul>
      </div>
    </div>
    <p class="legal"><span>© Lontyle Apps — Cristian Caride. All rights reserved.</span><span>Handcrafted with Unity &amp; Swift.</span></p>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def write(path, content):
    dest = os.path.join(DOCS, path.lstrip("/"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)


def store_buttons(t):
    btns = []
    if t.get("apple"):
        btns.append(f'<a class="btn primary" href="{t["apple"]}"{EXT}>{APPLE_SVG} Download on the App Store</a>')
    if t.get("google"):
        btns.append(f'<a class="btn primary" href="{t["google"]}"{EXT}>{PLAY_SVG} Get it on Google Play</a>')
    return "\n      ".join(btns)


def badge_class(cat):
    return "cat-android" if "Android" in cat else "cat-ios"


def badges_html(t, archived=False):
    b = "".join(f'<span class="badge {badge_class(c)}">{c}</span>' for c in t["cats"])
    if t.get("new"):
        b += '<span class="badge new">NEW</span>'
    if archived:
        b += '<span class="badge archived">Archive</span>'
    return f'<div class="badges">{b}</div>'


def card(t, archived=False):
    name = html.escape(t["name"], quote=False)
    cats = t["cats"] + (["Archived"] if archived else [])
    return f"""    <article class="card" data-cats="{'|'.join(cats)}" data-reveal>
      <div class="thumb tile">
        <span class="tile-bg" style="background-image:url('/assets/img/{t['icon']}')" aria-hidden="true"></span>
        <img class="tile-icon" src="/assets/img/{t['icon']}" alt="" width="104" height="104" loading="lazy">
        {badges_html(t, archived)}
      </div>
      <div class="card-body">
        <h3><a href="/title/{t['slug']}/">{name}</a></h3>
        <p>{html.escape(t['short'], quote=False)}</p>
        <span class="more">{'View project →' if archived else 'Discover the app →'}</span>
      </div>
    </article>"""


def marquee():
    row = "".join(f"<span>{item}</span>" for item in MARQUEE_ITEMS)
    return f'''<div class="marquee" aria-hidden="true">
  <div class="track">{row}{row}</div>
</div>'''


def breadcrumbs(name, path):
    ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Games & Apps", "item": DOMAIN + "/our-games/"},
            {"@type": "ListItem", "position": 3, "name": name, "item": DOMAIN + path},
        ],
    }
    nav = f"""<nav class="crumbs" aria-label="Breadcrumb">
      <a href="/">Home</a> <span aria-hidden="true">/</span> <a href="/our-games/">Games &amp; Apps</a> <span aria-hidden="true">/</span> <span aria-current="page">{html.escape(name, quote=False)}</span>
    </nav>"""
    return nav, ld


ORG_LD = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Lontyle Apps",
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/assets/img/favicon-192.png",
    "founder": {"@type": "Person", "name": "Cristian Caride"},
    "email": "lontyle@gmail.com",
    "sameAs": [APPLE_DEV],
}


def app_ld(t, path):
    os_name = "iOS" if not t.get("google") else "iOS, Android"
    return {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": t["name"],
        "operatingSystem": os_name,
        "applicationCategory": t.get("category", "MobileApplication"),
        "description": t["meta"],
        "image": DOMAIN + "/assets/img/" + t["icon"],
        "url": DOMAIN + path,
        "author": {"@type": "Organization", "name": "Lontyle Apps"},
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "installUrl": t.get("apple") or t.get("google"),
    }


# ---------------------------------------------------------------- pages
def build_home():
    app_cards = "\n".join(card(a) for a in APPS)
    game_cards = "\n".join(card(g, archived=True) for g in GAMES)
    shelf = "\n    ".join(
        f'<a href="/title/{t["slug"]}/" title="{html.escape(t["name"], quote=True)}"><img src="/assets/img/{t["icon"]}" alt="{html.escape(t["name"], quote=True)}" width="86" height="86" loading="lazy"></a>'
        for t in ALL_TITLES
    )
    website_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Lontyle Apps",
        "url": DOMAIN + "/",
    }
    body = f"""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Indie iOS app studio</span>
    <h1 data-reveal>Native iOS apps, <span class="grad">crafted</span> one at a time.</h1>
    <p class="lead" data-reveal>Lontyle Apps is a one-developer studio with game-design roots, now focused exclusively on building polished native apps for iPhone — live on the App Store.</p>
    <div class="actions" data-reveal>
      <a class="btn primary" href="{APPLE_DEV}"{EXT}>{APPLE_SVG} View App Store profile</a>
      <a class="btn" href="/our-games/">Explore the collection</a>
    </div>
    <div class="stats" data-reveal>
      <div><b data-count="4">4</b><span>Apps live on the App Store</span></div>
      <div><b data-count="7" data-suffix="+">7+</b><span>Releases shipped since day one</span></div>
      <div><b data-count="100" data-suffix="%">100%</b><span>Designed &amp; coded by one dev</span></div>
    </div>
    <div class="shelf" data-reveal aria-label="Our releases">
    {shelf}
    </div>
  </div>
</section>
{marquee()}
<section class="block" id="flagship">
  <div class="wrap">
    <div class="flagship" data-reveal>
      <div class="flagship-copy">
        <span class="eyebrow">Flagship app</span>
        <h2>Social Gym: the social network for people who <span class="grad">lift</span></h2>
        <p>Thousands of community routines, guided training with timed rests, XP duels with your friends and a 24/7 AI coach. Training, turned into a game.</p>
        <div class="actions">
          <a class="btn primary" href="{SOCIALGYM_URL}"{EXT}>{APPLE_SVG} Download free</a>
          <a class="btn" href="/title/socialfit-social-fitness/">Discover Social Gym</a>
        </div>
      </div>
      <div class="flagship-shot">
        <img src="/assets/img/app-socialgym-shot1.png" alt="Social Gym app — home screen with routines and AI coach" loading="lazy" width="330">
      </div>
    </div>
  </div>
</section>
<section class="block" id="apps">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <h2>Live on the <span class="grad">App Store</span></h2>
      <p>Apps you can download right now — designed for everyday problems, polished for everyday people.</p>
    </div>
    <div class="grid">
{app_cards}
    </div>
  </div>
</section>
<section class="block" id="journey">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <h2>The <span class="grad">journey</span></h2>
      <p>Every studio has an origin story. Ours runs through three chapters — each one sharpened the craft.</p>
    </div>
    <ol class="timeline">
      <li data-reveal>
        <span class="tl-badge">Chapter 1</span>
        <h3>🎮 Unity games for Android</h3>
        <p>Multiplayer cities, driving role-play, arcade towers. Building open worlds solo taught us scope, performance and what makes people come back.</p>
      </li>
      <li data-reveal>
        <span class="tl-badge">Chapter 2</span>
        <h3>📱 Cross-platform apps</h3>
        <p>From games to utilities: parking finders and everyday tools for Android and iOS. We learned to ship simple products that solve real problems.</p>
      </li>
      <li data-reveal class="current">
        <span class="tl-badge now">Now</span>
        <h3>🍎 Native iOS, exclusively</h3>
        <p>Today all our energy goes into SwiftUI apps for iPhone — fewer projects, deeper focus, App Store quality. This is where Lontyle does its best work.</p>
      </li>
    </ol>
  </div>
</section>
<section class="block tight" id="games">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <h2>Where it all <span class="grad">began</span></h2>
      <p>The Unity worlds from Chapter 1, preserved with pride. Retired from the stores — never from the story.</p>
    </div>
    <div class="grid">
{game_cards}
    </div>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <h2>One studio, <span class="grad">full craft</span></h2>
      <p>From idea to the App Store — every Lontyle release is designed, coded and shipped in-house.</p>
    </div>
    <div class="features">
      <div class="feature" data-reveal>
        <span class="ico">🍎</span>
        <h3>Native Swift &amp; SwiftUI</h3>
        <p>No cross-platform shortcuts: every app is built with Apple's native tools for speed, polish and longevity.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">🎮</span>
        <h3>Game-design DNA</h3>
        <p>Years of building games show up in our apps: XP systems, streaks, delightful details that make utilities fun.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">🎯</span>
        <h3>Fewer, better</h3>
        <p>We'd rather ship one app people love than ten they forget. Deep focus on every release.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">🤝</span>
        <h3>Personal support</h3>
        <p>Write to us and the developer answers — not a ticket system. Every user talks to the person who built the app.</p>
      </div>
    </div>
  </div>
</section>"""
    write("index.html", page(
        "Lontyle Apps — Indie iOS App Studio by Cristian Caride",
        "Lontyle Apps is an indie iOS studio crafting native iPhone apps: Social Gym, iGarage, Find My Car and CarKeep. Designed, coded and shipped by one developer.",
        body, "/", "home", jsonld=[ORG_LD, website_ld]))


def build_our_games():
    app_cards = "\n".join(card(a) for a in APPS)
    game_cards = "\n".join(card(g, archived=True) for g in GAMES)
    body = f"""<section class="hero compact">
  <div class="wrap">
    <span class="eyebrow">Portfolio</span>
    <h1 data-reveal>Games &amp; <span class="grad">Apps</span></h1>
    <p class="lead" data-reveal>Our current iOS lineup, ready to download — plus the Unity games from the studio's first chapter.</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter by category" data-reveal>
      <button class="active" data-filter="all">All</button>
      <button data-filter="iOS Apps">iOS</button>
      <button data-filter="Android Apps">Android</button>
      <button data-filter="Archived">Game archive</button>
    </div>
    <div class="grid" id="games-grid">
{app_cards}
{game_cards}
    </div>
  </div>
</section>
<script>
document.querySelectorAll('.filters button').forEach(function (btn) {{
  btn.addEventListener('click', function () {{
    document.querySelectorAll('.filters button').forEach(function (b) {{ b.classList.remove('active'); }});
    btn.classList.add('active');
    var f = btn.dataset.filter;
    document.querySelectorAll('#games-grid .card').forEach(function (card) {{
      card.style.display = (f === 'all' || card.dataset.cats.split('|').indexOf(f) !== -1) ? '' : 'none';
    }});
  }});
}});
</script>"""
    write("our-games/index.html", page(
        "Games & Apps Portfolio — Lontyle Apps | iOS & Android",
        "Browse every Lontyle Apps release: iGarage, Social Gym, Find My Car, CarKeep and our Unity game archive for Android.",
        body, "/our-games/", "games", jsonld=ORG_LD))


def related_cards(current_slug, count=3):
    pool = [t for t in ALL_TITLES if t["slug"] != current_slug]
    picks = pool[:count]
    return "\n".join(card(p, archived=(p in GAMES)) for p in picks)


SOCIALGYM_URL = "https://apps.apple.com/app/id1614796934"

SOCIALGYM_FAQ_EN = [
    ("Is Social Gym free?",
     "Yes. Social Gym is free to download and use. The optional Elite plan is a one-time purchase — no subscriptions, ever — that unlocks unlimited saves, the AI Coach, advanced analytics and removes ads."),
    ("What makes Social Gym different from other workout trackers?",
     "Social Gym is a social network for lifters, not just a log. You can browse thousands of community routines, remix them, compete in weekly 1v1 XP duels, join a monthly XP race and share your progress on The Wall."),
    ("Can I create my own gym routine?",
     "Yes. Build routines from scratch with sets, reps and rest times, or remix any community routine to make it yours. The AI generator can also create a routine tailored to your goal, level and available equipment."),
    ("Does Social Gym work with Apple Health?",
     "Yes. Your workouts sync to Apple Health automatically (write-only), so your activity rings and health records stay up to date."),
    ("How does the XP system work?",
     "Every completed workout earns XP. Keep your weekly streak alive, level up, win 1v1 duels against friends and climb the monthly XP race podium."),
    ("Is Social Gym available on Android?",
     "Social Gym is currently an iOS exclusive, built natively with Swift for the best iPhone experience."),
]

SOCIALGYM_FAQ_ES = [
    ("¿Social Gym es gratis?",
     "Sí. Social Gym es gratis para descargar y usar. El plan Elite opcional es un pago único — sin suscripciones — que desbloquea guardados ilimitados, el Coach IA, analíticas avanzadas y elimina los anuncios."),
    ("¿Qué diferencia a Social Gym de otras apps de gimnasio?",
     "Social Gym es la red social de la gente que entrena, no solo un registro. Explora miles de rutinas de la comunidad, haz remix de cualquiera, compite en duelos 1v1 semanales por XP y comparte tus logros en El Muro."),
    ("¿Puedo crear mi propia rutina de gym?",
     "Sí. Crea rutinas desde cero con series, repeticiones y descansos cronometrados, o haz remix de cualquier rutina de la comunidad. El generador IA también crea una rutina a tu medida según tu objetivo, nivel y material."),
    ("¿Se sincroniza con Apple Health?",
     "Sí. Tus entrenamientos se registran automáticamente en Apple Health para que tus anillos de actividad estén siempre al día."),
    ("¿Cómo funciona el sistema de XP?",
     "Cada entrenamiento completado suma XP. Mantén tu racha semanal, sube de nivel, gana duelos 1v1 contra tus amigos y pelea por el podio de la carrera mensual de XP."),
    ("¿Está disponible en Android?",
     "De momento Social Gym es exclusiva de iOS, desarrollada de forma nativa en Swift para la mejor experiencia en iPhone."),
]


def faq_jsonld(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }


def faq_html(faq, heading):
    items = "\n".join(
        f"""      <details class="faq-item" data-reveal>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>"""
        for q, a in faq
    )
    return f"""<section class="block tight" id="faq">
  <div class="wrap">
    <div class="section-head" data-reveal><h2>{heading}</h2></div>
    <div class="faq">
{items}
    </div>
  </div>
</section>"""


def socialgym_sections_en():
    return f"""<section class="block tight">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <h2>The workout tracker that feels like a <span class="grad">game</span></h2>
      <p>Most gym apps are spreadsheets. Social Gym turns training into something you want to open every day.</p>
    </div>
    <div class="features">
      <div class="feature" data-reveal>
        <span class="ico">🔍</span>
        <h3>Find your gym routine</h3>
        <p>Thousands of community workout routines filtered by goal, level, training days and equipment — plus an interactive 3D muscle map that shows what each routine works.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">⏱️</span>
        <h3>Guided training mode</h3>
        <p>Sets, reps and timed rests with lock-screen alerts. Log your weight set by set and let the app detect your personal records automatically.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">⚡</span>
        <h3>XP, streaks &amp; duels</h3>
        <p>Earn XP every workout, protect your weekly streak, challenge friends to 1v1 duels and race the community in the monthly XP podium.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">🤖</span>
        <h3>AI Coach, 24/7</h3>
        <p>Instant answers on training, nutrition and recovery — and an AI routine generator that builds a plan around your goal and equipment.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">📊</span>
        <h3>Progress you can see</h3>
        <p>History with charts, achievements, a home-screen widget and Apple Health sync. Elite adds advanced analytics and CSV export.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">💎</span>
        <h3>One-time purchase, no subscription</h3>
        <p>The Elite plan is a single purchase, forever. No monthly fees, no paywalled basics, zero ads.</p>
      </div>
    </div>
  </div>
</section>
{faq_html(SOCIALGYM_FAQ_EN, 'Frequently asked <span class="grad">questions</span>')}
<section class="block tight">
  <div class="wrap">
    <div class="cta-band" data-reveal>
      <h2>Train with your <span class="grad">community</span></h2>
      <p>Join the social network for people who lift. Free on the App Store.</p>
      <a class="btn primary" href="{SOCIALGYM_URL}" target="_blank" rel="noopener">{APPLE_SVG} Download Social Gym</a>
      <p class="cta-alt"><a href="/es/social-gym/">🇪🇸 También disponible en español</a></p>
    </div>
  </div>
</section>"""


def build_apps():
    for a in APPS:
        path = f"/title/{a['slug']}/"
        crumbs, crumb_ld = breadcrumbs(a["name"], path)
        shots = "\n    ".join(
            f'<img src="/assets/img/{s}" alt="{html.escape(a["name"], quote=True)} — screenshot {n}" loading="lazy">'
            for n, s in enumerate(a["screens"], 1)
        )
        body = f"""<section class="app-hero">
  <div class="backdrop" style="background-image:url('/assets/img/{a['icon']}')"></div>
  <div class="wrap layout">
    <img class="icon" src="/assets/img/{a['icon']}" alt="{html.escape(a['name'], quote=True)} app icon" width="148" height="148">
    <div>
      {crumbs}
      {badges_html(a)}
      <h1>{html.escape(a['name'], quote=False)}</h1>
      <p class="tagline">{html.escape(a['short'], quote=False)}</p>
      <div class="store-buttons">
      {store_buttons(a)}
      </div>
    </div>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="gallery" aria-label="Screenshots" data-reveal>
    {shots}
    </div>
    <div class="prose mt-0">
{a['body']}
    </div>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="section-head" data-reveal><h2>More from <span class="grad">Lontyle</span></h2></div>
    <div class="grid">
{related_cards(a['slug'])}
    </div>
  </div>
</section>"""
        title = f"{a['name']} — iOS App by Lontyle Apps"
        meta = a["meta"]
        jsonld = [app_ld(a, path), crumb_ld]
        extra_head = ""
        if a["slug"] == "socialfit-social-fitness":
            title = "Social Gym: Workout Tracker — Gym Routine App with AI Coach & XP"
            meta = ("Social Gym is the social fitness app for people who lift: thousands of gym routines, "
                    "guided workouts with timed rests, XP duels with friends and a 24/7 AI coach. Free on iOS.")
            body += socialgym_sections_en()
            jsonld.append(faq_jsonld(SOCIALGYM_FAQ_EN))
            extra_head = (f'\n  <link rel="alternate" hreflang="en" href="{DOMAIN}{path}">'
                          f'\n  <link rel="alternate" hreflang="es" href="{DOMAIN}/es/social-gym/">'
                          f'\n  <link rel="alternate" hreflang="x-default" href="{DOMAIN}{path}">')
        write(f"title/{a['slug']}/index.html", page(
            title, meta, body, path, "games",
            og_image=f"/assets/img/{a['icon']}",
            jsonld=jsonld, extra_head=extra_head))


def build_socialgym_es():
    a = next(x for x in APPS if x["slug"] == "socialfit-social-fitness")
    path = "/es/social-gym/"
    shots = "\n    ".join(
        f'<img src="/assets/img/{s}" alt="Social Gym — captura de pantalla {n}" loading="lazy">'
        for n, s in enumerate(a["screens"], 1)
    )
    body = f"""<section class="app-hero">
  <div class="backdrop" style="background-image:url('/assets/img/{a['icon']}')"></div>
  <div class="wrap layout">
    <img class="icon" src="/assets/img/{a['icon']}" alt="Icono de Social Gym" width="148" height="148">
    <div>
      <div class="badges"><span class="badge cat-ios">App para iPhone</span><span class="badge new">GRATIS</span></div>
      <h1>Social Gym — la red social de la gente que <span class="grad">entrena</span></h1>
      <p class="tagline">Encuentra tu próxima rutina de gym, entrena guiado con descansos cronometrados y compite con tus amigos por XP.</p>
      <div class="store-buttons">
      <a class="btn primary" href="{SOCIALGYM_URL}" target="_blank" rel="noopener">{APPLE_SVG} Descargar en el App Store</a>
      </div>
    </div>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="gallery" aria-label="Capturas de pantalla" data-reveal>
    {shots}
    </div>
    <div class="section-head" data-reveal>
      <h2>La app de rutinas de gym que se siente como un <span class="grad">juego</span></h2>
      <p>La mayoría de apps de gimnasio son hojas de cálculo. Social Gym convierte entrenar en algo que te apetece abrir cada día.</p>
    </div>
    <div class="features">
      <div class="feature" data-reveal>
        <span class="ico">🔍</span>
        <h3>Encuentra tu rutina</h3>
        <p>Miles de rutinas de la comunidad filtradas por objetivo, nivel, días y material — con un cuerpo 3D interactivo que muestra qué músculos trabaja cada rutina.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">⏱️</span>
        <h3>Entrenamiento guiado</h3>
        <p>Series, repeticiones y descansos cronometrados con avisos en la pantalla de bloqueo. Registra el peso serie a serie y detecta tus récords automáticamente.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">⚡</span>
        <h3>XP, rachas y duelos</h3>
        <p>Gana XP con cada entrenamiento, protege tu racha semanal, reta a tus amigos a duelos 1v1 y pelea por el podio de la carrera mensual.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">🤖</span>
        <h3>Coach IA 24/7</h3>
        <p>Respuestas al instante sobre entrenamiento, nutrición y descanso — y un generador de rutinas IA hecho a tu medida.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">📊</span>
        <h3>Progreso visible</h3>
        <p>Historial con gráficas, logros, widget para la pantalla de inicio y sincronización con Apple Health.</p>
      </div>
      <div class="feature" data-reveal>
        <span class="ico">💎</span>
        <h3>Pago único, sin suscripción</h3>
        <p>El plan Elite se compra una sola vez, para siempre. Sin cuotas mensuales y sin anuncios.</p>
      </div>
    </div>
  </div>
</section>
{faq_html(SOCIALGYM_FAQ_ES, 'Preguntas <span class="grad">frecuentes</span>')}
<section class="block tight">
  <div class="wrap">
    <div class="cta-band" data-reveal>
      <h2>Entrena con tu <span class="grad">comunidad</span></h2>
      <p>Únete a la red social de la gente que entrena. Gratis en el App Store.</p>
      <a class="btn primary" href="{SOCIALGYM_URL}" target="_blank" rel="noopener">{APPLE_SVG} Descargar Social Gym</a>
      <p class="cta-alt"><a href="/title/socialfit-social-fitness/">🇬🇧 Also available in English</a></p>
    </div>
  </div>
</section>"""
    extra_head = (f'\n  <link rel="alternate" hreflang="en" href="{DOMAIN}/title/socialfit-social-fitness/">'
                  f'\n  <link rel="alternate" hreflang="es" href="{DOMAIN}{path}">'
                  f'\n  <link rel="alternate" hreflang="x-default" href="{DOMAIN}/title/socialfit-social-fitness/">')
    write("es/social-gym/index.html", page(
        "Social Gym — App de Rutinas de Gym con Coach IA, XP y Duelos",
        "Social Gym es la red social de la gente que entrena: miles de rutinas de gym, entrenamiento guiado con descansos cronometrados, duelos de XP con amigos y Coach IA 24/7. Gratis para iPhone.",
        body, path, "games",
        og_image=f"/assets/img/{a['icon']}",
        jsonld=[app_ld(a, path), faq_jsonld(SOCIALGYM_FAQ_ES)],
        lang="es", extra_head=extra_head))


def build_games():
    for g in GAMES:
        path = f"/title/{g['slug']}/"
        data = read_json(g["json"])
        content = slice_content(data["blocks"])
        article = render_blocks(content)
        crumbs, crumb_ld = breadcrumbs(g["name"], path)
        shots = "\n    ".join(
            f'<img src="/assets/img/{s}" alt="{html.escape(g["name"], quote=True)} — screenshot {n}" loading="lazy">'
            for n, s in enumerate(g["screens"], 1)
        )
        orient = "" if g["portrait"] else " landscape"
        body = f"""<section class="app-hero">
  <div class="backdrop" style="background-image:url('/assets/img/{g['icon']}')"></div>
  <div class="wrap layout">
    <img class="icon" src="/assets/img/{g['icon']}" alt="{html.escape(g['name'], quote=True)} game icon" width="148" height="148">
    <div>
      {crumbs}
      {badges_html(g, archived=True)}
      <h1>{html.escape(g['name'], quote=False)}</h1>
      <p class="tagline">{html.escape(g['short'], quote=False)}</p>
    </div>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <p class="notice" data-reveal>🏛 <strong>Part of our origins.</strong> This Unity title belongs to the studio's first chapter and has been retired from the stores. The lessons it taught us live on in every iOS app we ship today — <a href="/our-games/">see what we're building now</a>.</p>
    <div class="gallery{orient}" aria-label="Screenshots" data-reveal>
    {shots}
    </div>
    <div class="prose mt-0">
{article}
    </div>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="section-head" data-reveal><h2>More from <span class="grad">Lontyle</span></h2></div>
    <div class="grid">
{related_cards(g['slug'])}
    </div>
  </div>
</section>"""
        write(f"title/{g['slug']}/index.html", page(
            f"{g['name']} — Lontyle Apps Archive",
            g["meta"], body, path, "games",
            og_image=f"/assets/img/{g['icon']}",
            jsonld=crumb_ld))


def build_articles():
    for slug, jname in ARTICLES:
        data = read_json(jname)
        content = slice_content(data["blocks"])
        h1 = next((b_text(b) for b in content if b["tag"] == "h1"), clean_title(data["title"]))
        article = render_blocks(content)
        body = f"""<section class="hero compact">
  <div class="wrap">
    <h1 data-reveal>{render_inline(h1)}</h1>
  </div>
</section>
<article class="wrap prose mt-0">
{article}
</article>"""
        title = clean_title(data["title"])
        desc = data.get("meta_description", "") or f"{title} — official document by Lontyle Apps."
        write(f"{slug}/index.html", page(f"{title} — Lontyle Apps", desc, body, f"/{slug}/", ""))


def build_about():
    person_ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Cristian Caride",
        "jobTitle": "Founder & Developer",
        "worksFor": {"@type": "Organization", "name": "Lontyle Apps"},
        "url": DOMAIN + "/about-us/",
        "sameAs": [APPLE_DEV],
    }
    body = """<section class="hero compact">
  <div class="wrap">
    <span class="eyebrow">About us</span>
    <h1 data-reveal>From open worlds to <span class="grad">everyday apps</span></h1>
    <p class="lead" data-reveal>One developer, three chapters, and a single obsession: crafting things people enjoy using.</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap prose mt-0">
    <h2>Welcome to Lontyle Apps</h2>
    <p>Lontyle Apps started where many indie stories do: building videogames. Multiplayer cities in Unity, driving role-play, arcade towers — worlds made for the joy of making them. That first chapter taught us how to design, optimize and ship complete experiences solo.</p>
    <p>The craft evolved into mobile apps, and with it came a discovery: the same care that makes a game fun makes an app delightful. Today the studio works exclusively on <strong>native iOS apps</strong> — fewer projects, deeper focus, built with Swift and SwiftUI and shipped on the App Store.</p>
    <p>The games? They're retired from the stores, but we keep them here with pride. They're the reason our apps feel the way they do.</p>
    <img src="/assets/img/chillout2-1024x547.png" alt="Lontyle Apps artwork" loading="lazy">
  </div>
</section>
<section class="block">
  <div class="wrap">
    <div class="section-head" data-reveal><h2>How we <span class="grad">work</span></h2></div>
    <div class="features">
      <div class="feature" data-reveal><span class="num">1</span>
        <h3>Real problems first</h3>
        <p>Every app starts with a need we've felt ourselves — losing a parked car, managing a workshop, staying consistent at the gym.</p>
      </div>
      <div class="feature" data-reveal><span class="num">2</span>
        <h3>Native or nothing</h3>
        <p>Swift and SwiftUI, no shortcuts. Native apps feel faster, last longer and respect the platform people love.</p>
      </div>
      <div class="feature" data-reveal><span class="num">3</span>
        <h3>Focus over volume</h3>
        <p>Going iOS-only was a choice: mastering one platform deeply beats spreading thin across many.</p>
      </div>
      <div class="feature" data-reveal><span class="num">4</span>
        <h3>Game-design heritage</h3>
        <p>XP, streaks, satisfying interactions — years of making games taught us how to make apps people want to open.</p>
      </div>
    </div>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="section-head" data-reveal><h2>Meet the <span class="grad">creator</span></h2></div>
    <div class="features">
      <div class="feature" data-reveal>
        <span class="ico">💻</span>
        <h3>Cristian Caride — Founder / Developer</h3>
        <p>Designer and developer behind every Lontyle release — a journey from Unity multiplayer worlds to native SwiftUI apps on the App Store.</p>
      </div>
    </div>
  </div>
</section>"""
    write("about-us/index.html", page(
        "About Lontyle Apps — Indie iOS Studio by Cristian Caride",
        "Lontyle Apps is a one-developer indie studio by Cristian Caride: born making Unity games, now crafting native iOS apps with Swift and SwiftUI.",
        body, "/about-us/", "about", jsonld=[ORG_LD, person_ld]))


def build_contact():
    body = """<section class="hero compact">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1 data-reveal>Get in <span class="grad">touch</span></h1>
    <p class="lead" data-reveal>Reach out for general and business enquiries — we answer personally.</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="contact-card" data-reveal>
      <h2>General Enquiries</h2>
      <p>Questions about our apps and games, support, business or press:</p>
      <a class="mail" href="mailto:lontyle@gmail.com">lontyle@gmail.com</a>
    </div>
  </div>
</section>"""
    write("contact/index.html", page(
        "Contact Lontyle Apps — Support & Business Enquiries",
        "Contact Lontyle Apps for app support, general and business enquiries: lontyle@gmail.com.",
        body, "/contact/", "contact", jsonld=ORG_LD))


def build_redirects():
    for src, dest in REDIRECTS.items():
        write(f"{src}/index.html", f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={dest}">
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{DOMAIN}{dest}">
  <title>Redirecting…</title>
</head>
<body><p>This page has moved. <a href="{dest}">Continue to {dest}</a></p></body>
</html>
""")


def build_misc():
    from datetime import date
    today = date.today().isoformat()
    urls = ["/", "/our-games/", "/about-us/", "/contact/", "/es/social-gym/"]
    urls += [f"/title/{t['slug']}/" for t in ALL_TITLES]
    urls += [f"/{slug}/" for slug, _ in ARTICLES]
    entries = "\n".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls)
    write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
""")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    write("CNAME", "www.lontylegames.com\n")
    write(".nojekyll", "")
    body = """<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Error 404</span>
    <h1>Lost in the <span class="grad">open world</span>.</h1>
    <p class="lead">The page you're looking for doesn't exist or has moved.</p>
    <div class="actions">
      <a class="btn primary" href="/">Respawn at home</a>
      <a class="btn" href="/our-games/">Games &amp; Apps</a>
    </div>
  </div>
</section>"""
    write("404.html", page("Page not found — Lontyle Apps", "", body, "/404.html", ""))


def main():
    # remove stale codetip page dir if present
    import shutil
    stale = os.path.join(DOCS, "title", "codetip-daily-coding-tips")
    if os.path.isdir(stale):
        shutil.rmtree(stale)
    build_home()
    build_our_games()
    build_apps()
    build_socialgym_es()
    build_games()
    build_articles()
    build_about()
    build_contact()
    build_redirects()
    build_misc()
    n = sum(len(files) for _, _, files in os.walk(DOCS))
    print(f"Built site into docs/ ({n} files)")


if __name__ == "__main__":
    main()
