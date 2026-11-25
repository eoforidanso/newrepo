"""Builds the Enterprise Foundation Solutions website.

Edit the text in this file, then run:  python3 build.py
Every page in the site/ folder is regenerated from it.
Publish with:  npx wrangler deploy
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"  # the folder that gets published

# Version tags so browsers fetch the new CSS/JS after every change.
import hashlib
def _ver(name):
    return hashlib.md5((OUT / "assets" / name).read_bytes()).hexdigest()[:8]
import art
art.generate(OUT / "assets" / "art")
CSS_VER, JS_VER = _ver("site.css"), _ver("site.js")
SITE_URL = "https://thepowerofus.us"

NAME = "Enterprise Foundation Solutions"
DESCRIPTOR = "Sales, Distribution and Business Growth Services"
EMAIL = "Kofiyeboah05@yahoo.com"
PHONE_DISPLAY = "0244 802 816"
PHONE_TEL = "+233244802816"
FOUNDER = "Kofi Obiri Yeboah"
YEAR = 2026

SERVICES = [
    {
        "slug": "sales-strategy-and-performance",
        "title": "Sales strategy and performance improvement",
        "short": "Sales strategy",
        "benefit": "Know where your next growth will come from",
        "card": "A sales review and a plan to hit your targets.",
        "for": "Businesses missing targets or unsure where growth will come from.",
        "problem": "Sales are flat, effort is spread thin and follow-up is inconsistent.",
        "do": [
            "Review sales, customers and where revenue comes from",
            "Check how pricing works in practice",
            "Review team activity and follow-up",
            "Build a sales plan with targets and owners",
        ],
        "get": ["Sales assessment", "Priority action plan", "Territory targets", "A simple performance dashboard"],
        "cta": "Request a Sales Assessment",
        "wa": "sales strategy",
        "seo": "Sales consultancy in Ghana: sales assessments, sales plans, targets and performance dashboards for growing businesses.",
    },
    {
        "slug": "distribution-and-market-expansion",
        "title": "Distribution and market expansion",
        "short": "Distribution",
        "benefit": "Reach more outlets and new territories",
        "card": "Plan your route to market and find the right dealers.",
        "for": "Manufacturers, importers and distributors seeking wider coverage.",
        "problem": "Products miss outlets, dealers underperform and new areas launch without a plan.",
        "do": [
            "Assess target locations",
            "Map routes and outlet coverage",
            "Find and assess dealers",
            "Improve distributor onboarding",
        ],
        "get": ["Route-to-market plan", "Territory and outlet priorities", "Distributor selection criteria", "Launch checklist"],
        "cta": "Discuss Market Expansion",
        "wa": "distribution and market expansion",
        "seo": "Distribution strategy in Ghana: route-to-market plans, dealer selection, territory priorities and market launch support.",
    },
    {
        "slug": "sales-training-and-coaching",
        "title": "Sales training and manager coaching",
        "short": "Sales training",
        "benefit": "A stronger, more confident sales team",
        "card": "Training for salespeople. Coaching for their managers.",
        "for": "Teams that need stronger selling skills or supervision.",
        "problem": "Deals stall, objections go unanswered and managers are unsure how to coach.",
        "do": [
            "Prospecting",
            "Handling objections and closing",
            "Follow-up and repeat business",
            "Target planning and leadership",
            "Field coaching, where agreed",
        ],
        "get": ["Training needs assessment", "Tailored workshop", "Practical sales tools", "Follow-up coaching plan"],
        "cta": "Request Team Training",
        "wa": "sales training",
        "seo": "Sales training in Ghana: practical workshops on prospecting, objection handling and closing, plus coaching for sales managers.",
    },
    {
        "slug": "part-time-sales-leadership",
        "title": "Part-time sales leadership",
        "short": "Sales leadership",
        "benefit": "Experienced direction without a full-time hire",
        "card": "Experienced direction for your sales team, on an agreed schedule.",
        "for": "Growing businesses not yet ready for a full-time sales director.",
        "problem": "The owner runs sales alongside everything else, so targets and reviews slip.",
        "do": [
            "Set clear targets with the team",
            "Run weekly sales reviews",
            "Coach your sales managers",
            "Monitor the sales pipeline",
            "Report to the owner",
        ],
        "get": ["Agreed management schedule", "Team scorecard", "Regular review meetings", "Monthly action report"],
        "cta": "Discuss Sales Management Support",
        "wa": "part-time sales leadership",
        "seo": "Part-time sales director support in Ghana: target setting, weekly reviews, pipeline monitoring and sales manager coaching.",
    },
    {
        "slug": "retail-operations-and-systems",
        "title": "Retail operations and business systems",
        "short": "Operations",
        "benefit": "Run the business the same way every day",
        "card": "Simple routines for stock, reporting and responsibilities.",
        "for": "Businesses with weak stock control, reporting or accountability.",
        "problem": "Stock goes missing, reports arrive late and responsibilities are unclear.",
        "do": [
            "Tighten stock allocation",
            "Set up reliable sales reporting",
            "Add customer follow-up routines",
            "Write clear operating procedures",
        ],
        "get": ["Operating procedures", "Stock and sales tracking templates", "Clear staff responsibilities", "Reporting calendar"],
        "cta": "Improve Our Operations",
        "wa": "retail operations",
        "seo": "Retail operations support in Ghana: stock control routines, sales reporting, operating procedures and staff responsibilities.",
    },
]

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("about.html", "About Us"),
    ("how-we-work.html", "How We Work"),
    ("contact.html", "Contact"),
]


def consult(service=None, label="Request a Consultation", cls="btn btn-primary"):
    href = "contact.html#enquiry-form"
    if service:
        href = f"contact.html?service={service}#enquiry-form"
    return f'<a class="{cls} cta-consult" href="{href}">{escape(label)}</a>'


def wa(topic="", label="Chat on WhatsApp", cls="btn btn-wa"):
    # site.js fills in the real wa.me link and draft message
    return f'<a class="{cls}" data-wa="{escape(topic)}" href="https://wa.me/233244802816">{escape(label)}</a>'


def page(filename, title, description, body, form=False):
    svc_files = {s["slug"] + ".html" for s in SERVICES}
    current = ' aria-current="page"'
    nav = "".join(
        f'<a href="{h}"{current if h == filename or (filename in svc_files and h == "services.html") else ""}>{t}</a>'
        for h, t in NAV
    )
    svc_links = "".join(f'<li><a href="{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    full_title = f"{title} | {NAME}" if filename != "index.html" else f"{NAME} | {DESCRIPTOR} in Ghana"
    url = f"{SITE_URL}/{'' if filename == 'index.html' else filename}"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0f2a47">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="EFS">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="stylesheet" href="assets/site.css?v={CSS_VER}">
</head>
<body{' class="has-form"' if form else ''}>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="mark" aria-hidden="true">EFS</span><span class="brand-text"><strong>{NAME}</strong><span>{DESCRIPTOR}</span></span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span><span></span></button>
    <nav id="site-nav" class="nav" aria-label="Main">{nav}
      <span class="header-cta">{consult(cls="btn btn-primary btn-sm")}</span>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>{NAME}</h4>
        <p>{DESCRIPTOR}. Practical support for growing businesses in Ghana.</p>
        <ul>
          <li>Phone / WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc_links}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="how-we-work.html">How We Work</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="privacy.html">Privacy notice</a></li>
        </ul>
      </div>
    </div>
    <div class="copy">&copy; {YEAR} {NAME}. All rights reserved. Photos: <a href="https://unsplash.com" rel="noopener">Unsplash</a>.</div>
  </div>
</footer>
<div class="mobile-bar">
  {consult(label="Request a Consultation", cls="btn btn-primary")}
  <a class="btn btn-wa" data-wa="" href="https://wa.me/233244802816"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 2.9 2.9 0 0 0-.9 2.2 5 5 0 0 0 1 2.7 11.6 11.6 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>WhatsApp</a>
</div>
<script src="assets/site.js?v={JS_VER}"></script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    return filename


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{escape(i)}</li>" for i in items) + "</ul>"


SERVICE_ART = {
    "sales-strategy-and-performance": "growth",
    "distribution-and-market-expansion": "network",
    "sales-training-and-coaching": "people",
    "part-time-sales-leadership": "compass",
    "retail-operations-and-systems": "grid",
}


# Stock photos (Unsplash License: free to use, credit appreciated). See CREDITS.md.
# name -> (alt text, width, height of the 1200px file)
PHOTOS = {
    "home-markets": ("Aerial view of a busy open-air market with rows of stalls and umbrellas", 1200, 900),
    "home-routes": ("A loaded blue truck on a city road", 1200, 800),
    "home-shop": ("A shopkeeper standing at the entrance of his shop", 1200, 845),
    "sales-strategy": ("A team around a meeting table with laptops", 1200, 801),
    "distribution": ("A motorised cart piled high with goods on a busy street", 1200, 784),
    "training": ("Colleagues looking at a laptop together", 1200, 800),
    "leadership": ("A small group in discussion in a modern room", 1200, 1546),
    "retail": ("A shop assistant at the counter of a well-stocked store", 1200, 800),
}
SERVICE_PHOTO = {
    "sales-strategy-and-performance": "sales-strategy",
    "distribution-and-market-expansion": "distribution",
    "sales-training-and-coaching": "training",
    "part-time-sales-leadership": "leadership",
    "retail-operations-and-systems": "retail",
}


def photo_img(name, sizes="(max-width: 760px) 100vw, 600px", eager=False):
    alt, w, h = PHOTOS[name]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="assets/photos/{name}.jpg" srcset="assets/photos/{name}-sm.jpg 640w, assets/photos/{name}.jpg 1200w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" {load} decoding="async">')


def service_tabs():
    """Homepage services as 3D tabs over a glass panel.
    Without JavaScript every panel shows, one after another."""
    tabs, panels = [], []
    for i, s in enumerate(SERVICES, 1):
        sel = "true" if i == 1 else "false"
        tabs.append(
            f'<button class="svc-tab" role="tab" id="tab-{s["slug"]}" aria-controls="panel-{s["slug"]}" '
            f'aria-selected="{sel}" tabindex="{0 if i == 1 else -1}">'
            f'<span class="svc-tab-num">{i:02d}</span><span class="svc-tab-name">{escape(s["short"])}</span></button>')
        chips = "".join(f"<li>{escape(g)}</li>" for g in s["get"])
        does = "".join(f"<li>{escape(d)}</li>" for d in s["do"])
        panels.append(f"""<div class="svc-panel art-{SERVICE_ART[s['slug']]}" role="tabpanel" id="panel-{s['slug']}" aria-labelledby="tab-{s['slug']}" tabindex="0">
  <div class="svc-panel-main">
    <p class="svc-panel-kicker">{escape(s['benefit'])}</p>
    <h3>{escape(s['title'].capitalize())}</h3>
    <p class="svc-panel-for">{escape(s['for'])}</p>
    <p class="svc-panel-label">You receive</p>
    <ul class="svc-chips">{chips}</ul>
    <div class="btn-row">{consult(s['slug'], s['cta'])}<a class="btn btn-light" href="{s['slug']}.html">View Service</a></div>
  </div>
  <div class="svc-panel-side">
    <p class="svc-panel-label">What we do</p>
    <ul class="ticks svc-does">{does}</ul>
  </div>
</div>""")
    return f"""<div class="svc-tabs" data-tabs>
  <div class="svc-tablist" role="tablist" aria-label="Our services">{''.join(tabs)}</div>
  <div class="svc-stage">{''.join(panels)}</div>
  <p class="svc-unsure">Not sure where to start? <a class="cta-consult" href="contact.html?service=not-sure#enquiry-form">Tell us your challenge &rarr;</a></p>
</div>"""


def service_cards():
    cards = "".join(
        f"""<div class="card svc-card">
  <span class="svc-num">{i:02d}</span>
  <p class="benefit">{escape(s['benefit'])}</p>
  <h3>{escape(s['title'].capitalize())}</h3>
  <p>{escape(s['card'])}</p>
  <a class="more" href="{s['slug']}.html">View Service &rarr;</a>
</div>"""
        for i, s in enumerate(SERVICES, 1)
    )
    # Sixth tile fills the 3-column grid and catches visitors who are unsure.
    cards += f"""<div class="card card-cta">
  <h3>Not sure where to start?</h3>
  <p>Tell us your challenge. We will point you to the right support.</p>
  {consult("not-sure", "Request a Consultation", cls="btn btn-primary")}
</div>"""
    return cards


STEPS = [
    ("Understand your business", "A first conversation about your challenge."),
    ("Agree a practical plan", "A proposal, with scope, fees and timing agreed upfront."),
    ("Support implementation", "Training, coaching and hands-on field support."),
    ("Review progress", "Regular reviews against agreed measures."),
]

ENGAGE = [
    ("Focused assessment", "A short review of one area, with clear priorities."),
    ("Improvement project", "Agreed deliverables over a set timeframe."),
    ("Ongoing monthly support", "Ongoing hands-on support, reviewed monthly."),
]


def steps_html(detail=False):
    return "".join(
        f'<div class="card"><span class="num">{i}</span><h3>{escape(t)}</h3>{f"<p>{escape(d)}</p>" if detail else ""}</div>'
        for i, (t, d) in enumerate(STEPS, 1)
    )


ENGAGE_ICONS = ["search", "flag", "calendar"]


def engage_html():
    # ICONS is defined further down; this runs only when pages are built.
    return "".join(
        f'<div class="card"><span class="icon">{ICONS[ic]}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></div>'
        for (t, d), ic in zip(ENGAGE, ENGAGE_ICONS)
    )


BIO = (f"{FOUNDER} is a sales and operations leader with more than 17 years of experience across FMCG, "
       "telecommunications, PAYGO technology, renewable energy and mobility in Ghana. His experience includes "
       "leading regional teams, strengthening distribution, coaching sales managers and improving commercial "
       "execution. He holds a Commonwealth Executive MBA from KNUST and a BSc in Mathematics and Statistics "
       "from the University of Cape Coast.")

SHORT_BIO = ("Sales and operations leader with more than 17 years of experience improving commercial "
             "execution, strengthening distribution networks and developing sales teams across Ghana's FMCG, "
             "telecoms, PAYGO, renewable energy and mobility sectors.")

# Simple line icons (inline SVG, inherit the text colour).
_svg = '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>'
ICONS = {
    "briefcase": _svg.format('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>'),
    "pin": _svg.format('<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
    "target": _svg.format('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'),
    "check": _svg.format('<path d="M3 20h18"/><path d="M6 16v-4M11 16V9M16 16v-3"/><path d="M14 6l2 2 4-4"/>'),
    "users": _svg.format('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/>'),
    "alert": _svg.format('<path d="M12 3 2 20h20L12 3z"/><path d="M12 10v4"/><path d="M12 17h.01"/>'),
    "doc": _svg.format('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/><path d="M8 13h8M8 17h5"/>'),
    "search": _svg.format('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>'),
    "flag": _svg.format('<path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/>'),
    "calendar": _svg.format('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
    "tool": _svg.format('<path d="M14.5 6.5a4 4 0 0 0 5 5L12 19a2.1 2.1 0 0 1-3-3l7.5-7.5"/><path d="m5 5 4 4"/><path d="M3 7l4-4"/>'),
    "text": _svg.format('<path d="M4 6h16M4 12h16M4 18h10"/>'),
    "chart": _svg.format('<path d="M3 20h18"/><path d="M7 16v-5M12 16V6M17 16v-8"/>'),
    "chev": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>',
}

# Founder photo: put a file at assets/founder.jpg and set this to True.
HAS_PHOTO = (OUT / "assets" / "founder.jpg").exists()


def photo():
    if HAS_PHOTO:
        return f'<div class="photo"><img src="assets/founder.jpg" alt="{FOUNDER}, founder of {NAME}"></div>'
    return '<div class="photo" aria-hidden="true">KOY</div>'


# ---------------------------------------------------------------- pages
built = []

built.append(page("index.html", "Home",
    "Enterprise Foundation Solutions helps growing businesses in Ghana improve sales, expand distribution and strengthen daily operations through practical advice, sales training and hands-on support.",
    f"""
<section class="hero art-network">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">{DESCRIPTOR}</span>
      <h1>We help businesses in Ghana sell more and reach more outlets.</h1>
      <p class="lead">Sales plans, distribution, team training and part-time sales leadership, led by a founder with 17+ years in sales across FMCG, telecoms and energy.</p>
      <ul class="hero-chips" aria-label="What we do">
        <li><a href="sales-strategy-and-performance.html">{ICONS['target']}Sales plan &amp; targets</a></li>
        <li><a href="distribution-and-market-expansion.html">{ICONS['pin']}Distribution &amp; dealers</a></li>
        <li><a href="sales-training-and-coaching.html">{ICONS['users']}Sales team training</a></li>
        <li><a href="part-time-sales-leadership.html">{ICONS['flag']}Part-time sales leadership</a></li>
      </ul>
      <div class="btn-row">
        {consult()}
        <a class="btn btn-light" href="services.html">Explore Our Services</a>
      </div>
      <p class="hero-wa">Prefer to chat? {wa(label="Message us on WhatsApp", cls="")}</p>
      <p class="hero-for">For business owners, manufacturers, importers and distributors.</p>
    </div>
    <figure class="hero-founder">
      {photo()}
      <figcaption>
        <strong>{FOUNDER}</strong>
        <span class="hf-role">Founder</span>
        <span class="hf-line">17+ years improving sales execution and distribution across Ghana.</span>
        <span class="hf-sectors">FMCG &middot; Telecoms &middot; PAYGO &middot; Energy &middot; Mobility</span>
        <span class="hf-badges"><span>17+ years</span><span>Executive MBA</span><span>Market expansion</span></span>
      </figcaption>
    </figure>
  </div>
</section>

<div class="proof">
  <div class="wrap proof-grid">
    <div><strong>17+ years</strong><span>in sales and operations leadership</span></div>
    <div><strong>5 sectors</strong><span>FMCG, telecoms, PAYGO, renewable energy, mobility</span></div>
    <div><strong>Field-tested</strong><span>regional teams, dealers and distribution</span></div>
    <div><strong>Executive MBA</strong><span>Commonwealth Executive MBA, KNUST</span></div>
  </div>
</div>

<section>
  <div class="wrap">
    <h2>Does this sound like your business?</h2>
    <div class="grid g3" style="margin-top:24px">
      <a class="problem" href="{SERVICES[0]['slug']}.html"><strong>Are sales below target?</strong><span>Effort is high, but results are not.</span><em>Sales strategy and performance &rarr;</em></a>
      <a class="problem" href="{SERVICES[1]['slug']}.html"><strong>Is your distribution limited?</strong><span>Products are not reaching enough outlets.</span><em>Distribution and market expansion &rarr;</em></a>
      <a class="problem" href="{SERVICES[3]['slug']}.html"><strong>Does your team need stronger direction?</strong><span>Salespeople need skills; managers need support.</span><em>Training and sales leadership &rarr;</em></a>
    </div>
  </div>
</section>

<section class="scenes">
  <div class="wrap">
    <h2>Where the work happens</h2>
    <div class="scene-grid">
      <figure class="scene">{photo_img("home-markets", "(max-width: 760px) 100vw, 380px")}<figcaption>Markets and outlets</figcaption></figure>
      <figure class="scene">{photo_img("home-routes", "(max-width: 760px) 100vw, 380px")}<figcaption>Routes and distribution</figcaption></figure>
      <figure class="scene">{photo_img("home-shop", "(max-width: 760px) 100vw, 380px")}<figcaption>Shops and counters</figcaption></figure>
    </div>
  </div>
</section>

<section class="svc-tabs-section">
  <div class="wrap">
    <h2>Our services</h2>
    {service_tabs()}
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why work with us</span>
      <h2>Advice from someone who has done the work</h2>
    </div>
    <div class="trust-grid">
      <div class="founder-visual">{photo()}</div>
      <div class="founder-copy">
        <h3 class="founder-name">{FOUNDER}</h3>
        <p class="founder-sub">Founder &middot; 17+ years across five sectors in Ghana</p>
        <ul class="badges">
          <li>17+ years experience</li>
          <li>Executive MBA, KNUST</li>
          <li>Regional sales leadership</li>
          <li>Distribution &amp; market expansion</li>
        </ul>
        <ul class="ticks ticks-2">
          <li>Led regional sales teams</li>
          <li>Strengthened distribution</li>
          <li>Coached sales managers</li>
          <li>Improved commercial execution</li>
        </ul>
      </div>
    </div>
    <div class="grid g4 benefits">
      <div class="card"><span class="icon">{ICONS['briefcase']}</span><h3>Practical field experience</h3><p>Learned leading real sales teams.</p></div>
      <div class="card"><span class="icon">{ICONS['pin']}</span><h3>Ghanaian market knowledge</h3><p>Five sectors, hands-on.</p></div>
      <div class="card"><span class="icon">{ICONS['target']}</span><h3>Clear plans</h3><p>Targets and routines your team can follow.</p></div>
      <div class="card"><span class="icon">{ICONS['check']}</span><h3>Ongoing accountability</h3><p>Regular reviews against agreed measures.</p></div>
    </div>
    <div class="btn-row trust-cta">
      {consult(label="Discuss your growth challenges →")}
      <a class="btn btn-outline" href="about.html">More about Kofi</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>How we work</h2>
    <div class="grid g4 steps" style="margin-top:24px">{steps_html(detail=True)}</div>
    <p style="margin-top:20px"><a href="how-we-work.html">See our full approach &rarr;</a></p>
  </div>
</section>

<!-- Evidence / client stories: add approved founder achievements or genuine client stories here.
     Say clearly whether results come from previous employment or from Enterprise Foundation Solutions engagements. -->

<section class="dark">
  <div class="wrap">
    <h2>What is holding your business back?</h2>
    <p class="lead">Tell us your main challenge and the support you need.</p>
    <div class="btn-row">{consult()} {wa(cls="btn btn-light")}</div>
  </div>
</section>
"""))

built.append(page("services.html", "Services",
    "Sales strategy, distribution and market expansion, sales training, part-time sales leadership and retail operations support for growing businesses in Ghana.",
    f"""
<section class="page-hero art-network">
  <div class="wrap">
    <span class="eyebrow">Services</span>
    <h1>Practical support for growing businesses</h1>
    <p class="lead">Each starts with a problem and ends with clear deliverables.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="grid g3">{service_cards()}</div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <h2>Three ways to work with us</h2>
    <p class="lead">Scope and fees follow a conversation about your needs.</p>
    <div class="grid g3 benefits" style="margin-top:28px">{engage_html()}</div>
    <div class="btn-row">{consult()}</div>
  </div>
</section>
"""))

for n, s in enumerate(SERVICES, 1):
    others = "".join(
        f'<li><a href="{o["slug"]}.html"><span>{escape(o["title"].capitalize())}</span>{ICONS["chev"]}</a></li>'
        for o in SERVICES if o is not s)
    do_list = "".join(f'<li><span class="do-num">{i}</span><span>{escape(d)}</span></li>' for i, d in enumerate(s["do"], 1))
    tiles = "".join(f'<div class="tile"><span class="tile-icon">{ICONS["doc"]}</span><span>{escape(g)}</span></div>' for g in s["get"])
    built.append(page(f"{s['slug']}.html", s["title"].capitalize(), s["seo"],
        f"""
<section class="page-hero art-{SERVICE_ART[s['slug']]}">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="services.html">Services</a><span aria-hidden="true">/</span><span>{n:02d} of {len(SERVICES):02d}</span></nav>
    <h1>{escape(s['title'].capitalize())}</h1>
    <p class="lead">{escape(s['benefit'])}.</p>
    <div class="btn-row">{consult(s['slug'], s['cta'])} {wa(s['wa'], cls="btn btn-light")}</div>
  </div>
</section>
<section>
  <div class="wrap svc-body">
    <div class="svc-main">
      <figure class="svc-photo">{photo_img(SERVICE_PHOTO[s['slug']], "(max-width: 760px) 100vw, 720px")}</figure>
      <div class="grid g2 benefits svc-intro">
        <div class="card"><span class="icon">{ICONS['users']}</span><h3>Who it is for</h3><p>{escape(s['for'])}</p></div>
        <div class="card"><span class="icon">{ICONS['alert']}</span><h3>The problem</h3><p>{escape(s['problem'])}</p></div>
      </div>
      <div class="svc-block">
        <h2>What we do</h2>
        <ol class="do-list">{do_list}</ol>
      </div>
      <div class="svc-block">
        <h2>What you receive</h2>
        <p class="muted">Typical deliverables</p>
        <div class="tiles">{tiles}</div>
      </div>
      <div class="next-panel">
        <h2>Next step</h2>
        <p>Tell us what you want to improve. Scope, fees and timing are agreed before any work begins.</p>
        <div class="btn-row">{consult(s['slug'], s['cta'])} {wa(s['wa'], cls="btn btn-light")}</div>
      </div>
    </div>
    <aside class="aside">
      <div class="aside-cta">
        <h3>{escape(s['cta'])}</h3>
        <p class="note">A short form. No account, upload or payment needed.</p>
        {consult(s['slug'], s['cta'], cls="btn btn-primary")}
        <p class="note" style="margin:14px 0 0">Or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
      <h3 class="list-title">Other services</h3>
      <ul class="list-rows">{others}</ul>
    </aside>
  </div>
</section>
"""))

built.append(page("about.html", "About Us",
    f"About {NAME}: a practical business growth partner in Ghana founded by {FOUNDER}, a sales and operations leader with more than 17 years of experience.",
    f"""
<section class="page-hero art-compass">
  <div class="wrap">
    <span class="eyebrow">About us</span>
    <h1>A practical business growth partner</h1>
    <p class="lead">Stronger sales, wider distribution and better day-to-day execution.</p>
  </div>
</section>
<section>
  <div class="wrap grid g2 about-intro">
    <div>
      <h2>Our purpose</h2>
      <p>Many Ghanaian businesses have good products but weak sales structures. We build the routines that turn effort into results.</p>
      <p class="callout">We are not a charity. "Foundation" means the commercial foundations we help build.</p>
    </div>
    <div class="card serve-card">
      <h2>Who we serve</h2>
      {ticks(["Growing businesses with inconsistent sales",
              "Manufacturers, importers and distributors",
              "Companies needing training or part-time sales leadership"])}
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <h2>Our approach</h2>
    <div class="grid g3 benefits" style="margin-top:28px">
      <div class="card"><span class="icon">{ICONS['tool']}</span><h3>Hands-on</h3><p>In the field with your team, not just the meeting room.</p></div>
      <div class="card"><span class="icon">{ICONS['text']}</span><h3>Simple and clear</h3><p>Plain-language plans and tools.</p></div>
      <div class="card"><span class="icon">{ICONS['chart']}</span><h3>Measured</h3><p>Measures agreed upfront, reviewed regularly.</p></div>
    </div>
  </div>
</section>
<section class="trust">
  <div class="wrap trust-grid">
    <div class="founder-visual">{photo()}</div>
    <div class="founder-copy">
      <span class="eyebrow">Founder</span>
      <h2 class="founder-name">{FOUNDER}</h2>
      <p class="founder-sub">17+ years in FMCG, telecoms, PAYGO, renewable energy and mobility</p>
      <ul class="badges">
        <li>17+ years experience</li>
        <li>Executive MBA, KNUST</li>
        <li>Regional sales leadership</li>
        <li>Distribution &amp; market expansion</li>
      </ul>
      <p>{BIO}</p>
      <h3 class="quals-title">Qualifications</h3>
      {ticks(["Commonwealth Executive MBA, Kwame Nkrumah University of Science and Technology (KNUST)",
              "BSc Mathematics and Statistics, University of Cape Coast"])}
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <h2>Let us talk about your business</h2>
    <div class="btn-row">{consult()} {wa(cls="btn btn-light")}</div>
  </div>
</section>
"""))

FAQ = [
    ("Who do you work with?", "Growing businesses, distributors, manufacturers and sales organisations that need stronger commercial execution."),
    ("Can you train our existing team?", "Yes. Training is tailored to your business need, with field coaching available where agreed."),
    ("Can we engage you for one project?", "Yes. You can choose a focused assessment, a defined improvement project or ongoing monthly support."),
    ("Where do you operate?", "We are based in Ghana and work with businesses across the country. Travel arrangements are agreed for field assignments."),
    ("How much does it cost?", "Fees depend on the scope, team size, location and duration of the work. Request a consultation and we will send you a proposal."),
    ("What happens after I enquire?", "We review your request and contact you to discuss the next step. Nothing is booked or charged until we have agreed it with you."),
]

built.append(page("how-we-work.html", "How We Work",
    "How Enterprise Foundation Solutions works with clients: initial discussion, assessment and proposal, practical implementation and coaching, and regular progress reviews.",
    f"""
<section class="page-hero art-growth">
  <div class="wrap">
    <span class="eyebrow">How we work</span>
    <h1>A clear process, agreed with you</h1>
    <p class="lead">Scope, fees, timing and responsibilities are agreed before work begins.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="grid g4 steps">{steps_html(detail=True)}</div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <h2>Ways to work with us</h2>
    <p class="lead">Scope and fees follow a conversation about your needs.</p>
    <div class="grid g3 benefits" style="margin-top:28px">{engage_html()}</div>
  </div>
</section>
<section>
  <div class="wrap" style="max-width:820px">
    <h2>Common questions</h2>
    <div class="faq">{"".join(f'<details><summary><span>{escape(q)}</span>{ICONS["chev"]}</summary><p>{escape(a)}</p></details>' for q, a in FAQ)}</div>
    <div class="btn-row">{consult()} {wa()}</div>
  </div>
</section>
"""))

options = "".join(f'<option value="{s["slug"]}">{escape(s["title"].capitalize())}</option>' for s in SERVICES)
built.append(page("contact.html", "Contact",
    f"Request a consultation with {NAME}. Call or WhatsApp {PHONE_DISPLAY}, email {EMAIL}, or tell us your challenge using the short enquiry form.",
    f"""
<section class="page-hero art-people">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Tell us how we can help</h1>
    <p class="lead">Tell us your challenge and we will be in touch. This is a request, not a booked appointment.</p>
  </div>
</section>
<section id="enquiry-form">
  <div class="wrap form-wrap">
    <div>
      <div id="form-status" class="alert" hidden tabindex="-1" role="status" aria-live="polite"></div>
      <form id="enquiry" novalidate>
        <div class="two">
          <div class="field"><label for="name">Full name</label><input id="name" name="name" autocomplete="name" required><div class="err">Please enter your name.</div></div>
          <div class="field"><label for="business">Business name</label><input id="business" name="business" autocomplete="organization" required><div class="err">Please enter your business name.</div></div>
        </div>
        <p class="hint" style="margin:-4px 0 10px">Give us at least one way to reach you: email, phone or both.</p>
        <div class="two">
          <div class="field"><label for="email">Email <span class="opt">(email or phone)</span></label><input id="email" name="email" type="email" autocomplete="email"><div class="err">Please enter a valid email address.</div></div>
          <div class="field"><label for="phone">Phone / WhatsApp <span class="opt">(email or phone)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"><div class="err">Please enter a valid phone number.</div></div>
        </div>
        <p id="contact-err" class="err" style="margin:-8px 0 14px">Please give an email address or a phone number.</p>
        <div class="field"><label for="service">Service needed</label>
          <select id="service" name="service" required>
            <option value="">Choose a service</option>{options}<option value="not-sure">Not sure yet</option>
          </select><div class="err">Please choose a service, or "Not sure yet".</div></div>
        <div class="field"><label for="challenge">Main challenge</label>
          <textarea id="challenge" name="challenge" required placeholder="What would you like to improve in your business?"></textarea>
          <div class="err">Please tell us briefly what you would like to improve.</div></div>
        <div class="two">
          <div class="field"><label for="location">Location <span class="opt">(optional)</span></label><input id="location" name="location" placeholder="Town or region"></div>
          <div class="field"><label for="contact_method">Preferred contact method <span class="opt">(optional)</span></label>
            <select id="contact_method" name="contact_method"><option value="">No preference</option><option>Call</option><option>Email</option><option>WhatsApp</option></select></div>
        </div>
        <div class="field"><label for="timing">When do you need support? <span class="opt">(optional)</span></label>
          <select id="timing" name="timing"><option value="">Choose one</option><option>As soon as possible</option><option>Within one month</option><option>Within three months</option><option>Just exploring options</option></select></div>
        <div class="hp" aria-hidden="true"><label for="website">Leave this empty</label><input id="website" name="website" tabindex="-1" autocomplete="off"></div>
        <input type="hidden" id="source" name="source_page">
        <p class="note">We use your details only to respond to this request. See our <a href="privacy.html">privacy notice</a>.</p>
        <button class="btn btn-primary" type="submit">Send my request</button>
      </form>
    </div>
    <aside class="aside">
      <h3 class="list-title">Prefer to talk?</h3>
      <ul class="list-rows contact-rows">
        <li><a href="tel:{PHONE_TEL}"><span><small>Call</small>{PHONE_DISPLAY}</span>{ICONS["chev"]}</a></li>
        <li><a data-wa="" href="https://wa.me/233244802816"><span><small>WhatsApp</small>{PHONE_DISPLAY}</span>{ICONS["chev"]}</a></li>
        <li><a href="mailto:{EMAIL}"><span><small>Email</small>{EMAIL}</span>{ICONS["chev"]}</a></li>
      </ul>
      <div class="privacy-box" style="margin-top:22px">
        <strong>Your privacy.</strong> We use your details only to reply to you, and never sell or share them. To have them removed, email <a href="mailto:{EMAIL}">{EMAIL}</a>.
      </div>
    </aside>
  </div>
</section>
""", form=True))

built.append(page("privacy.html", "Privacy notice",
    f"How {NAME} collects, uses and protects the personal details you share with us.",
    f"""
<section class="page-hero art-grid">
  <div class="wrap"><h1>Privacy notice</h1></div>
</section>
<section>
  <div class="wrap" style="max-width:820px">
    <h2>What we collect</h2>
    <p>When you send an enquiry we collect your name, business name, email address and/or phone number, the service you are interested in, your message, and any optional details you choose to give (location, preferred contact method and timing).</p>
    <h2>Why we collect it</h2>
    <p>We use these details only to respond to your request and discuss how we can help. We do not add you to a mailing list unless you separately ask to join one.</p>
    <h2>Who sees it</h2>
    <p>Your enquiry is seen only by the {NAME} team. We do not sell your details or share them with third parties for marketing.</p>
    <h2>Website analytics</h2>
    <p>We may count page visits and button clicks to understand how the website is used. These counts never include your name, phone number, email address or message.</p>
    <h2>How long we keep it</h2>
    <p>We keep enquiry details for as long as needed to respond to you and manage any work we agree together.</p>
    <h2>Your choices</h2>
    <p>You can ask to see, correct or remove your details at any time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> or calling <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
    <p class="note">Last updated: November 2026.</p>
  </div>
</section>
"""))

# sitemap + robots
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE_URL}/{'' if f == 'index.html' else f}</loc></url>\n" for f in built)
    + "</urlset>\n", encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
(OUT / "assets" / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0f2a47"/>'
    '<text x="32" y="42" font-family="Arial,sans-serif" font-size="26" font-weight="700" fill="#fff" text-anchor="middle">EFS</text>'
    '<rect x="14" y="48" width="36" height="4" rx="2" fill="#1f8a86"/></svg>', encoding="utf-8")

# ---- Installable app (PWA) -------------------------------------------------
# Paths are relative so the site works at a domain root or under /newrepo/.
import json
(OUT / "manifest.webmanifest").write_text(json.dumps({
    "name": NAME,
    "short_name": "EFS",
    "description": DESCRIPTOR,
    "id": "./",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#0f2a47",
    "icons": [
        {"src": "assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "assets/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
    "shortcuts": [
        {"name": "Request a Consultation", "url": "contact.html#enquiry-form"},
        {"name": "Our Services", "url": "services.html"},
    ],
}, indent=2), encoding="utf-8")

# The service worker caches every page and asset so the site opens offline.
# Its cache name changes whenever any file changes, so visitors get updates.
precache = ["./"] + built + [
    f"assets/site.css?v={CSS_VER}", f"assets/site.js?v={JS_VER}",
    "assets/favicon.svg", "assets/icon-192.png", "assets/icon-512.png",
    "assets/apple-touch-icon.png", "manifest.webmanifest",
] + [f"assets/art/{n}.svg" for n in art.PIECES] + (["assets/founder.jpg"] if HAS_PHOTO else [])
h = hashlib.md5()
for f in sorted(p for p in OUT.rglob("*") if p.is_file() and p.name != "sw.js"):
    h.update(f.read_bytes())
(OUT / "sw.js").write_text(f"""/* Enterprise Foundation Solutions: offline support. Generated by build.py. */
const CACHE = 'efs-{h.hexdigest()[:10]}';
const FILES = {json.dumps(precache)};

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('efs-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  if (req.mode === 'navigate') {{
    // pages: newest from the network, cached copy when offline
    e.respondWith(fetch(req).then(res => {{
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(req, copy));
      return res;
    }}).catch(() => caches.match(req, {{ ignoreSearch: true }})
      .then(r => r || caches.match('./'))));
    return;
  }}
  // files: cached copy first (their names change when they change)
  e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {{
    // photos are cached the first time they are seen, so they work offline after
    if (res.ok && req.url.includes('/assets/photos/')) {{
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(req, copy));
    }}
    return res;
  }})));
}});
""", encoding="utf-8")

print("Built", len(built), "pages:", ", ".join(built))
