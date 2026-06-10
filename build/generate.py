#!/usr/bin/env python3
"""Generate static HTML pages for SBL Energy site from shared template + page data."""
import os, textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ============================================================================
# SHARED PARTIALS
# ============================================================================

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="{desc}" />
<title>{title}</title>
<link rel="icon" type="image/png" href="images/logo/sbl-energy-mark.png" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css" />
</head>
<body>"""

TOPBAR = """
<div class="topbar">
  <div class="container topbar-inner">
    <div class="topbar-left">
      <span>Nagpur, Maharashtra, India</span>
      <span class="divider"></span>
      <span>Mon–Fri 9:00–18:00  •  Sat 9:00–16:00</span>
    </div>
    <div class="topbar-right">
      <a href="mailto:info@sblenergy.com">info@sblenergy.com</a>
      <span class="divider"></span>
      <a href="tel:+917122542357">+91-712-2542357</a>
      <span class="divider"></span>
      <a href="https://www.facebook.com/SBLEnergyLimited" target="_blank">Facebook</a>
      <a href="https://www.linkedin.com/company/sbl-energy-ltd" target="_blank">LinkedIn</a>
    </div>
  </div>
</div>"""

def navbar(active=""):
    def cls(name): return ' class="active"' if name == active else ''
    def acls(name): return ' class="active"' if name == active else ''
    return f"""
<header class="navbar" id="navbar">
  <div class="container nav-inner">
    <a href="index.html" class="logo">
      <img src="images/logo/sbl-energy-wordmark.png" alt="SBL Energy Limited" class="logo-img" />
    </a>

    <nav class="nav-menu">
      <ul>
        <li><a href="index.html"{cls('home')}>Home</a></li>
        <li class="has-drop">
          <a href="about.html"{cls('about')}>About Us <span class="caret">▾</span></a>
          <div class="dropdown">
            <a href="about.html">Company Profile</a>
            <a href="people-clients.html">People &amp; Clients</a>
          </div>
        </li>
        <li class="has-drop">
          <a href="#"{cls('products')}>Products <span class="caret">▾</span></a>
          <div class="dropdown wide">
            <div class="drop-col">
              <h4>Industrial / Mining Explosives</h4>
              <a href="slurry-explosives.html">Slurry Explosives</a>
              <a href="emulsion-explosives.html">Emulsion Explosives</a>
              <a href="bulk-explosives.html">Bulk Emulsion Explosives</a>
              <a href="low-column-charge.html">Low Column Charge</a>
              <a href="seismic-explosives.html">Seismic Explosives</a>
            </div>
            <div class="drop-col">
              <h4>Explosives Accessories</h4>
              <a href="ordinary-detonator.html">Ordinary Detonator</a>
              <a href="electric-detonator.html">Electric Detonator</a>
              <a href="non-electric-detonator.html">Non-Electric Detonator</a>
              <a href="copper-delay-detonator.html">Copper Delay Detonator</a>
              <a href="electronic-detonator.html">Electronic Detonator</a>
              <a href="detonating-fuse.html">Detonating Fuse</a>
              <a href="cast-booster.html">Cast Booster</a>
            </div>
          </div>
        </li>
        <li><a href="services.html"{cls('services')}>Services</a></li>
        <li><a href="career.html"{cls('career')}>Career</a></li>
        <li><a href="contact.html"{cls('contact')}>Contact</a></li>
      </ul>
    </nav>

    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary btn-sm">Get an Estimate <span class="arrow">→</span></a>
      <button class="burger" id="burger" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>"""

FOOTER = """
<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-logo-card">
          <img src="images/logo/sbl-energy-wordmark.png" alt="SBL Energy Limited" />
        </div>
        <p>SBL Energy Limited is an acclaimed manufacturer of industrial &amp; mining explosives, incorporated in 2002 and based in Nagpur, Maharashtra, India.</p>
        <div class="socials">
          <a href="https://www.linkedin.com/company/sbl-energy-ltd" target="_blank" aria-label="LinkedIn"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M19 0H5C2.2 0 0 2.2 0 5v14c0 2.8 2.2 5 5 5h14c2.8 0 5-2.2 5-5V5c0-2.8-2.2-5-5-5zM8 19H5V8h3v11zM6.5 6.7c-1 0-1.7-.7-1.7-1.7s.7-1.7 1.8-1.7 1.7.7 1.7 1.7-.7 1.7-1.8 1.7zM20 19h-3v-5.6c0-1.5-.6-2-1.5-2-1 0-1.5.6-1.5 2V19h-3V8h3v1.2c.5-.8 1.4-1.4 2.7-1.4 2.4 0 3.3 1.7 3.3 4V19z"/></svg></a>
          <a href="https://www.facebook.com/SBLEnergyLimited" target="_blank" aria-label="Facebook"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M22 12c0-5.5-4.5-10-10-10S2 6.5 2 12c0 5 3.7 9.1 8.4 9.9V15h-2.5v-3h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 3h-2.3v6.9C18.3 21.1 22 17 22 12z"/></svg></a>
          <a href="https://g.page/sbl-energy-limited?share" target="_blank" aria-label="Google Business"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 2C7.6 2 4 5.6 4 10c0 6 8 12 8 12s8-6 8-12c0-4.4-3.6-8-8-8zm0 11a3 3 0 110-6 3 3 0 010 6z"/></svg></a>
        </div>
      </div>

      <div class="footer-col">
        <h4>Company</h4>
        <a href="about.html">About Us</a>
        <a href="about.html">Company Profile</a>
        <a href="people-clients.html">People &amp; Clients</a>
        <a href="career.html">Career</a>
        <a href="services.html">Services</a>
      </div>
      <div class="footer-col">
        <h4>Products</h4>
        <a href="slurry-explosives.html">Slurry Explosives</a>
        <a href="emulsion-explosives.html">Emulsion Explosives</a>
        <a href="bulk-explosives.html">Bulk Explosives</a>
        <a href="detonating-fuse.html">Detonating Fuse</a>
        <a href="electronic-detonator.html">Electronic Detonator</a>
        <a href="cast-booster.html">Cast Booster</a>
      </div>
      <div class="footer-col">
        <h4>Reach Us</h4>
        <a href="mailto:info@sblenergy.com">info@sblenergy.com</a>
        <a href="tel:+917122542357">+91-712-2542357</a>
        <p class="addr">230, Hill Road, Da Rock Building, 2nd Floor, Shivaji Nagar, Nagpur — 440010, MH, India</p>
      </div>
    </div>

    <div class="footer-bottom">
      <p>© 2026 SBL Energy Limited. All rights reserved.</p>
      <div class="footer-links">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Use</a>
        <a href="contact.html">Contact</a>
      </div>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>"""

# ============================================================================
# PRODUCT PAGE TEMPLATE
# ============================================================================

def _render_badge(p):
    """Render the product badge — accepts brand as a string or a list of names.

    With a list, the front-end JS cycles through the names one at a time.
    """
    import json
    brand = p.get('brand', '')
    if isinstance(brand, (list, tuple)):
        names = [str(b).strip() for b in brand if b]
    else:
        names = [s.strip() for s in str(brand).split('/')] if '/' in str(brand) else [str(brand)]
    first = names[0] if names else ''
    if len(names) > 1:
        data_attr = f' data-brands=\'{json.dumps(names)}\''
    else:
        data_attr = ''
    return (
        f'<div class="prod-img-badge"{data_attr}>'
        f'<span class="badge-tag">SBL ENERGY</span>'
        f'<span class="badge-name">{first}</span>'
        f'</div>'
    )


def product_page(p):
    """Render a single product detail page."""
    adv_html = '\n'.join(f'        <li><span class="check">✓</span>{a}</li>' for a in p['advantages'])
    safety_html = '\n'.join(f'        <li><span class="check">!</span>{s}</li>' for s in p['safety'])
    apps_html = ''  # The red applications band has been removed in favour of
                    # a uniform bullet-point APPLICATION extra-section on every
                    # product page (defined in specs.py).
    # --- TECHNICAL SPECIFICATIONS ---
    spec_html = ''
    spec_inner = ''

    # 1. HTML data table (always preferred) — auto-merges consecutive cells
    # with identical values into rowspans for cleaner presentation
    if p.get('spec_table'):
        st = p['spec_table']
        header_row = ''.join(f'<th>{h}</th>' for h in st['headers'])
        rows_data = st['rows']
        n_cols = len(st['headers'])

        # Compute rowspan map: for each (r, c) data cell, count consecutive
        # subsequent rows (within the same group segment) that share the value.
        # Cells absorbed into a rowspan above are recorded as "skip".
        rowspan = {}   # (r,c) -> int rowspan to render
        skip = set()   # (r,c) cells to skip during render
        for r, row in enumerate(rows_data):
            if isinstance(row, dict):
                continue
            for c in range(n_cols):
                if (r, c) in skip:
                    continue
                span = 1
                for rr in range(r + 1, len(rows_data)):
                    rrow = rows_data[rr]
                    if isinstance(rrow, dict):
                        break  # hit a group divider — segment ends
                    if str(rrow[c]) != str(row[c]):
                        break
                    span += 1
                    skip.add((rr, c))
                rowspan[(r, c)] = span

        body_rows = ''
        for r, row in enumerate(rows_data):
            if isinstance(row, dict) and row.get('group'):
                body_rows += f'<tr class="group-row"><td colspan="{n_cols}">{row["group"]}</td></tr>'
                continue
            cells = ''
            for c in range(n_cols):
                if (r, c) in skip:
                    continue
                span = rowspan.get((r, c), 1)
                attr = f' rowspan="{span}"' if span > 1 else ''
                cls = ' class="merged-cell"' if span > 1 else ''
                cells += f'<td{attr}{cls}>{row[c]}</td>'
            body_rows += f'<tr>{cells}</tr>'
        caption = st.get('caption','')
        spec_inner += f"""
        <div class="spec-table-wrap reveal">
          {f'<div class="spec-caption">{caption}</div>' if caption else ''}
          <div class="spec-table-scroll">
            <table class="spec-table">
              <thead><tr>{header_row}</tr></thead>
              <tbody>{body_rows}</tbody>
            </table>
          </div>
        </div>
"""

    # 2. Product image gallery — skip if empty (most accessory products only have the
    #    overview image, which is already shown at the top of the page)
    gallery_html = ''
    gallery = p.get('gallery') or []
    if gallery:
        items = ''.join(
            f'<figure class="gallery-item"><img src="{g["src"]}" alt="{g["alt"]}"/><figcaption>{g["alt"]}</figcaption></figure>'
            for g in gallery
        )
        gallery_html = f"""
        <div class="gallery-wrap reveal">
          <h3 class="gallery-title">Product Imagery</h3>
          <div class="gallery-grid">{items}</div>
        </div>
"""

    if spec_inner or gallery_html:
        spec_html = f"""
    <section class="section spec-section">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-tag"><span class="tag-line"></span> TECHNICAL SPECIFICATIONS</div>
          <h2 class="section-title">Specifications &amp; <span class="accent">Performance Data.</span></h2>
          <p class="lead" style="margin-top:18px;max-width:780px">Detailed technical data, dimensions and packaging information for {p['name']}.</p>
        </div>
        {spec_inner}
        {gallery_html}
      </div>
    </section>
"""
    extra_html = ''
    if p.get('extra_sections'):
        for s in p['extra_sections']:
            items = '\n'.join(f'        <li><span class="check">✓</span>{i}</li>' for i in s.get('items', []))
            extra_html += f"""
    <section class="section section-alt">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-tag"><span class="tag-line"></span> {s['tag']}</div>
          <h2 class="section-title">{s['title']}</h2>
          <p class="lead" style="margin-top:18px;max-width:780px">{s.get('desc','')}</p>
        </div>
        {f'<ul class="adv-list reveal">{items}</ul>' if items else ''}
      </div>
    </section>
"""

    related_html = ''
    if p.get('related'):
        rel_cards = ''
        for r in p['related']:
            rel_cards += f"""
          <a href="{r['url']}" class="related-card">
            <img src="{r['img']}" alt="{r['name']}"/>
            <div class="related-body">
              <h4>{r['name']}</h4>
              <span class="related-link">View product →</span>
            </div>
          </a>
"""
        related_html = f"""
    <section class="section related-section">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-tag"><span class="tag-line"></span> RELATED PRODUCTS</div>
          <h2 class="section-title">You may also be<br/><span class="accent">interested in.</span></h2>
        </div>
        <div class="related-grid">{rel_cards}</div>
      </div>
    </section>
"""

    return f"""{head(p['title'], p['desc'])}
{TOPBAR}
{navbar('products')}

<!-- ============ PRODUCT HERO ============ -->
<section class="prod-hero">
  <div class="prod-hero-bg" style="background-image:url('{p['hero_bg']}')"></div>
  <div class="prod-hero-overlay"></div>
  <div class="container prod-hero-content">
    <nav class="breadcrumb">
      <a href="index.html">Home</a>
      <span>›</span>
      <a href="#">Products</a>
      <span>›</span>
      <span class="current">{p['name']}</span>
    </nav>
    <div class="prod-hero-tag"><span class="dot"></span> {p['category']}</div>
    <h1 class="prod-hero-title">{p['display_name']}</h1>
    <p class="prod-hero-sub">{p['tagline']}</p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary">Request a Quote <span class="arrow">→</span></a>
      <a href="https://www.sblenergy.com/_files/ugd/06db74_7aba56dcc5c9456fbe8bcffc8c9c3cb6.pdf" target="_blank" class="btn btn-ghost">Download E-Brochure</a>
    </div>
  </div>
</section>

<!-- ============ PRODUCT OVERVIEW ============ -->
<section class="section prod-overview">
  <div class="container prod-overview-grid">
    <div class="prod-img-wrap reveal">
      <div class="prod-img-frame">
        <img src="{p['product_image']}" alt="{p['name']}" />
      </div>
      {_render_badge(p)}
    </div>
    <div class="prod-text reveal">
      <div class="section-tag"><span class="tag-line"></span> OVERVIEW</div>
      <h2 class="section-title">{p['overview_title']}</h2>
      {''.join(f'<p class="prod-para">{para}</p>' for para in p['overview'])}
    </div>
  </div>
</section>

{apps_html}

<!-- ============ ADVANTAGES ============ -->
<section class="section adv-section">
  <div class="container">
    <div class="adv-grid">
      <div class="adv-col reveal">
        <div class="section-tag"><span class="tag-line"></span> KEY ADVANTAGES</div>
        <h2 class="section-title">Why our <span class="accent">{p['name']}</span> stand out.</h2>
      </div>
      <ul class="adv-list reveal">
{adv_html}
      </ul>
    </div>
  </div>
</section>

{spec_html}
{extra_html}

<!-- ============ SAFETY ============ -->
<section class="section safety-section section-dark">
  <div class="container">
    <div class="adv-grid">
      <div class="adv-col reveal">
        <div class="section-tag light"><span class="tag-line"></span> SAFETY GUIDELINES</div>
        <h2 class="section-title light">Handling, storage<br/>&amp; <span class="accent">transport.</span></h2>
        <p class="lead" style="color:rgba(255,255,255,.65)">Always follow local PESO regulations and SBL Energy's product-specific safety guidance.</p>
      </div>
      <ul class="adv-list light reveal">
{safety_html}
      </ul>
    </div>
  </div>
</section>

{related_html}

<!-- ============ CTA ============ -->
<section class="cta-strip">
  <div class="container cta-inner">
    <div class="cta-text">
      <h2>Need a quote for {p['name']}?</h2>
      <p>Our technical team will help you choose the right specification for your site.</p>
    </div>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-white">Get an Estimate <span class="arrow">→</span></a>
    </div>
  </div>
</section>

{FOOTER}"""

# ============================================================================
# PRODUCT DATA
# ============================================================================

ALL_PRODUCTS = [
    # (slug, name, image_for_related)
    ('slurry-explosives', 'Slurry Explosives', 'images/products/packaged-explosives-chart.jpg'),
    ('emulsion-explosives', 'Emulsion Explosives', 'images/hero/coal.jpg'),
    ('bulk-explosives', 'Bulk Explosives', 'images/hero/bulk-truck.jpg'),
    ('low-column-charge', 'Low Column Charge', 'images/hero/blast-mountain.jpg'),
    ('seismic-explosives', 'Seismic Explosives', 'images/hero/blast-panoramic.jpg'),
    ('ordinary-detonator', 'Ordinary Detonator', 'images/products/ordinary-detonator.png'),
    ('electric-detonator', 'Electric Detonator', 'images/products/electric-detonator.jpg'),
    ('non-electric-detonator', 'Non-Electric Detonator', 'images/products/non-electric-detonator.png'),
    ('copper-delay-detonator', 'Copper Delay Detonator', 'images/products/copper-delay-detonator.jpg'),
    ('electronic-detonator', 'Electronic Detonator', 'images/products/electronic-detonator.jpg'),
    ('detonating-fuse', 'Detonating Fuse', 'images/products/detonating-fuse.jpg'),
    ('cast-booster', 'Cast Booster', 'images/products/cast-booster.jpg'),
]

def related_for(slug, count=3):
    """Get 3 related products excluding self."""
    others = [p for p in ALL_PRODUCTS if p[0] != slug]
    # cycle through nearby products
    idx = next(i for i, p in enumerate(ALL_PRODUCTS) if p[0] == slug)
    pick = []
    for i in range(1, count + 1):
        nxt = ALL_PRODUCTS[(idx + i) % len(ALL_PRODUCTS)]
        pick.append({'name': nxt[1], 'img': nxt[2], 'url': nxt[0] + '.html'})
    return pick


PRODUCTS = {
    # ========== Industrial / Mining Explosives ==========
    'slurry-explosives': {
        'title': 'Slurry Explosives Manufacturer & Supplier in India | SBL Energy Limited',
        'desc': 'SBL Energy manufactures water-resistant cap-sensitive and non-cap-sensitive slurry cartridge explosives — NEO PRIME, NEO BLAST, NEO BASE, NEO COL, DYNO PRIME, DYNO COLUMN. PESO approved.',
        'name': 'Slurry Explosives',
        'display_name': 'Slurry Explosives.',
        'category': 'INDUSTRIAL / MINING EXPLOSIVES',
        'tagline': 'The 3rd generation of commercial explosives — water-resistant, high-energy slurry cartridges for surface and underground mining.',
        'brand': ['NEO COL (Special)', 'NEO BASE (Special)', 'NEO PRIME (Special)', 'NEO BLAST (Special)', 'DYNO PRIME', 'DYNO COLUMN'],
        'hero_bg': 'images/hero/blast-mountain.jpg',
        'product_image': 'images/products/slurry-cartridges.png',
        'overview_title': 'Blasting Equipment Suppliers in <span class="accent">Pan India.</span>',
        'overview': [
            'Slurry Explosives or Water gels are known as the <strong>3rd generation of commercial explosives</strong> that has taken over traditional explosives like ANFO &amp; Gun Powder. Slurry explosive is a mixture of ammonium nitrate or other nitrates and fuel sensitizers which can either be a hydrocarbon or hydrocarbons and aluminum. Slurries are made water-resistant through the use of gum, waxes, cross-linking agents or emulsifiers.',
            '<strong>SBL Energy Limited</strong> has an upper hand among the various Blasting Equipment Suppliers in Pan India. We are one of the quality suppliers who dedicatedly engineer, design and manufacture the blasting equipment that are made as per your specifications and the need for the application of your operation. The blasting equipment offered here by SBL Energy are efficient and cost-effective and that is why we stand among the best Blasting Equipment Suppliers in Pan India.',
            'Blasting equipment need strong quality control process to ensure that all the malfunctions are eliminated, and a high-effective model is delivered. We take all the onus of the quality control checks right from the production process till the final product gets delivered to the client, making sure that there are no delays.',
        ],
        'advantages': [
            'Excellent water resistance',
            'Cost efficient, easy to use and safe',
            'They provide high degree of safety from Mechanical Impact friction',
            'They have exceptional bore hole coupling and transfer maximum energy',
            'Density of slurry explosives can be controlled',
        ],
        'safety': [
            'Should be kept away from flame &amp; excessive heat',
            'Should be handled with care and stored in a cool and dry place',
            'Do not subject product to heavy impact or friction',
            'During charging ensure that cartridges are charged in a continuous column in the bore hole',
        ],
        'applications': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying and hill cutting — used as Booster / Primer charges (cap-sensitive) and as Column charges (non-cap-sensitive) with excellent water resistance.',
        'related': related_for('slurry-explosives'),
    },

    'emulsion-explosives': {
        'title': 'Emulsion Explosives Manufacturer in India | SBL Energy Limited',
        'desc': 'SBL Energy is a leading emulsion explosives company in India — large-diameter and small-diameter cartridge emulsions: NEO PRIME, NEO BLAST, NEO BASE, NEO COLUMN, NEO GEL 90/901, NEO DYNE.',
        'name': 'Emulsion Explosives',
        'display_name': 'Emulsion Explosives.',
        'category': 'INDUSTRIAL / MINING EXPLOSIVES',
        'tagline': 'The most recent generation of industrial explosives — more efficient, safer and higher performing than slurries and water-gels.',
        'brand': ['NEO PRIME', 'NEO BLAST', 'NEO BASE', 'NEO COLUMN', 'DYNO POWER-90', 'NEO GEL 90', 'NEO GEL 901', 'NEO DYNE'],
        'hero_bg': 'images/hero/blast-panoramic.jpg',
        'product_image': 'images/products/emulsion-cartridges.png',
        'overview_title': 'Emulsion Explosive Company <span class="accent">in India.</span>',
        'overview': [
            'Emulsion is the most recent discovery in the industrial explosives industry &amp; is extensively used for commercial blasting all over the world since they are <strong>more efficient, more safe &amp; deliver better performance</strong> than slurries / water gels. There has been a significant rise in the usage of emulsion explosives due to greater advantages as compared to other explosives.',
            'Depending upon the need of the client, we are one of the leading Emulsion Explosives Companies in India as we cater to various emulsion package explosives. Emulsion explosives have come more in demand lately as it is a new technology in industrial explosives and is highly preferred for the commercial blasting as it is extremely efficient, safer and deliver good results as compared to the water gels and slurries.',
            'Most of the Emulsion Explosive Companies in India, including <strong>SBL Energy</strong>, has seen huge demand and usage of the emulsion explosives as it comes with some great benefits including its high resistance to water, low sensitivity to heat, high viscosity and rigidity and its high velocity of detonation.',
        ],
        'advantages': [
            'Highly safe in manufacturing, transporting, storage and handling — the emulsion is classified as an oxidizer, so transport and storage does not lead to danger of explosion',
            'Excellent resistance to water',
            'High velocity of detonation &amp; Weight strength',
            'Savings in drilling operations',
            'Low sensitivity to heat',
            'High viscosity and rigidity',
        ],
        'safety': [
            'The emulsion is stable and does not explode in the standard striking tests or while burning',
            'However, it acts in contact with materials such as detonators, dynamites or aluminium powder',
            'SBL Energy offers a complete range of Emulsion packaged Explosives — procurable in both bulk and packaged forms depending on the application',
            'Emulsions are widely used in both bulk and cartridge emulsifier systems for underground and surface mining',
        ],
        'applications': 'Cap-sensitive and booster-sensitive emulsion cartridges for Deep / Long-hole blasting in opencast mines, quarrying, hill cutting and underground metal mines. Available in both large-diameter (booster / primer / column) and small-diameter (well-sinking, shaft-sinking, tunneling) formats.',
        'related': related_for('emulsion-explosives'),
    },

    'bulk-explosives': {
        'title': 'Bulk Emulsion Manufacturing Company India | SBL Energy Limited',
        'desc': 'SBL Energy — leading bulk emulsion manufacturing company in India. Site-mixed re-pumpable doped / straight emulsion (NEO BULK) for quarry & open-pit mining.',
        'name': 'Bulk Explosives',
        'display_name': 'Bulk Explosives.',
        'category': 'INDUSTRIAL / MINING EXPLOSIVES',
        'tagline': 'Site-mixed, on-borehole-loaded bulk emulsion for quarry and open-pit mining — safer transport, faster loading, lower inventory.',
        'brand': 'NEO BULK',
        'hero_bg': 'images/hero/manufacturing-floor.jpg',
        'product_image': 'images/products/bulk-truck-user.jpg',
        'overview_title': 'Bulk Emulsion Manufacturing <span class="accent">Company India.</span>',
        'overview': [
            'Bulk explosives systems / Site-mixed system is suitable to customers who require <strong>large quantities of explosives</strong>. The materials, often mixed on the job by the supplier in the delivery truck, are directly drawn into the drill hole by trained workers. This is intended for quarry and open-pit mining tasks to enhance blast execution, security and environmental conditions. The material is transported as an oxidiser and is sensitised using emulsion processing technology during borehole loading. At SBL, we have bulk system only for emulsion explosives.',
            'Coming from a well-established network of Bulk Emulsion Manufacturing India, <strong>SBL Energy Limited</strong> has ensured a continuous improvement in its services that have the most demand in the market. With our highly advanced bulk explosives emulsion, you have an upper hand as it offers a solid combination of the explosives and the rock that facilitate the performance of your product and as a result, the operations of blasting, down streaming and drilling are carried out in the most optimized manner.',
            'If you are looking for larger quantities of explosives, then you must watch out for Bulk Emulsion Manufacturing Company India and trustfully choose <strong>SBL Energy</strong>. The bulk system is only for the emulsion explosives at SBL, and the rest of the equipment is carefully transported as an oxidizer and is induced with the help of the emulsion processing technology at the time of borehole loading.',
        ],
        'advantages': [
            'Re-pumpable Doped Emulsion / Straight Emulsion',
            'Extremely Safe and Simple',
            'Ambient Temperature System',
            'Long Sleeping Time',
            'Highly Stable Product',
            'Fast Loading',
            'Minimum Manpower Requirement',
            'Reduced Inventory / Mine Bench Handling',
            'Nominal Site Facility Needed',
            'Costs would be less than that of cartridge explosives',
            'Bulk explosives fill-up the blast holes completely without gaps / voids',
            'Allows widening of drill pattern, hence, cost efficient',
            'Waterproof',
            'Better performance since lot of non-productive activities are eliminated',
        ],
        'safety': [
            'Should be kept away from heat / sparks / open flames / hot surfaces',
            'Eliminate all potential sources of ignition — avoid activities that could create an impact, friction, spark or a sudden rise in temperature',
            'Avoid spilling on the ground other than pumping into authorised shot holes — keep away from drains &amp; other water courses',
            'Keep product clean &amp; free from contamination',
            'Not intended to be stored — only loaded at point of use. If loaded holes are left overnight, a guard should be placed',
        ],
        'applications': 'Bulk Emulsion explosive sensitised by chemical gassing agents and stabilisers. NEO Bulk-901 is ideally suitable for Shovel as well as Dragline bench blasting in large-scale opencast and quarry operations.',
        'related': related_for('bulk-explosives'),
    },

    'low-column-charge': {
        'title': 'Low Column Charge Explosives — OPTIGEL | SBL Energy Limited',
        'desc': 'OPTIGEL — low density non-cap sensitive Class II emulsion explosive for large-dia dry/damp holes. PESO 1140. ANFO-equivalent heave energy.',
        'name': 'Low Column Charge Explosives',
        'display_name': 'Low Column Charge Explosives.',
        'category': 'INDUSTRIAL / MINING EXPLOSIVES',
        'tagline': 'OPTIGEL — a low density Class II non-cap sensitive emulsion explosive, manufactured by mixing emulsion matrix with ammonium nitrate prills and HSD.',
        'brand': 'OPTIGEL',
        'hero_bg': 'images/hero/blast-mountain.jpg',
        'product_image': 'images/products/optigel-cartridge-clean.png',
        'overview_title': 'OPTIGEL — engineered <span class="accent">column charging.</span>',
        'overview': [
            'It is a <strong>low density non-cap sensitive Class 2 emulsion explosive</strong> manufactured by mixing Emulsion matrix with ammonium Nitrate prills with HSD having Brand name OPTIGEL.',
            'Our group company M/s <strong>SBL ENERGY LIMITED</strong> is manufacturing Non-Cap Sensitive Class II Explosive — manufactured by mixing Emulsion matrix doped with ammonium Nitrate prills with HSD having Brand name OPTIGEL.',
            '<strong>Application:</strong> Optigel Cartridge is suitable for use in large dia holes, of 100 mm or more &amp; where the blast holes are dry or damp with little presence of water. The product is Non-cap sensitive explosive &amp; is to be used as a column charge in open-cut mining, quarrying and for general blasting. For charging, Optigel Cartridge would be dumped inside the bore hole as the case with similar cartridge products.',
        ],
        'advantages': [
            'Reliable and easy to use, provides consistent result',
            'Low density product — hence high column height with minimum explosive charge',
            'Cost effective explosive for dry hole or damp holes',
            'Higher heave energy compared to Slurry / Emulsion Cartridge Explosives — results in better fragmentation with less vibration',
            'Heave energy equivalent to ANFO',
        ],
        'safety': [
            'Should be kept away from heat / sparks / open flames / hot surfaces',
            'Avoid shock / friction / grinding',
            'Avoid dust accumulation',
            'Wear protective equipments',
            'Should only be handled by qualified and authorised persons',
            'Should be stored in a cool, well ventilated and dry area',
        ],
        'applications': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying and hill cutting — used as Column Charge in dry holes of 100 mm diameter and above.',
        'related': related_for('low-column-charge'),
    },

    'seismic-explosives': {
        'title': 'Seismic Explosives Manufacturer in India — NEO GEL-90 CPT | SBL Energy',
        'desc': 'NEO GEL-90 CPT — Seismic Emulsion Explosive. PESO 915, density 1.20 g/cc, VOD 5000 m/s, hydrostatic head 58 m. For seismic exploration.',
        'name': 'Seismic Explosives',
        'display_name': 'Seismic Explosives.',
        'category': 'INDUSTRIAL / MINING EXPLOSIVES',
        'tagline': 'NEO GEL-90 CPT — high strength, high VOD seismic emulsion explosive engineered to sink in water and deliver consistent shock signatures.',
        'brand': 'NEO GEL - 90 CPT',
        'hero_bg': 'images/hero/blast-panoramic.jpg',
        'product_image': 'images/products/seismic-neogel-box.png',
        'overview_title': 'Seismic explosive engineered to <span class="accent">sink in water.</span>',
        'overview': [
            'SBL Energy manufactures <strong>NEO GEL-90 CPT</strong>, a Seismic Emulsion Explosive designed specifically for seismic exploration.',
            'The product density is engineered so that the cartridge <strong>sinks in water</strong>, making it ideal for sub-surface and water-filled borehole seismic surveys.',
            'Packed in couplable tube format, it delivers high strength, high VOD and excellent water resistance — meeting the demanding requirements of oil &amp; gas seismic exploration.',
        ],
        'advantages': [
            'High strength explosive — consistent energy delivery',
            'High Velocity of Detonation (5,000 m/s) — strong shock signature',
            'Excellent water resistance — hydrostatic head of 58 metres',
            'Packed in couplable tubes for easy field deployment',
            'Density designed so cartridge sinks in water — suitable for water-filled holes',
        ],
        'safety': [
            'Initiation is done by No. 8 strength Seismic detonator',
            'Sleeping time is approximately 8 weeks',
            'Should be handled by trained seismic blasting professionals only',
            'Store and transport according to PESO regulations',
        ],
        'applications': 'Seismic explosive used for seismic exploration. The product density is designed in a way that the cartridge sinks in water — suitable for oil &amp; gas geophysical surveys and sub-surface mapping.',
        'related': related_for('seismic-explosives'),
    },

    # ========== Accessories ==========
    'ordinary-detonator': {
        'title': 'Ordinary Detonator (NEO OD) Manufacturer in India | SBL Energy Limited',
        'desc': 'NEO OD — Aluminium plain Ordinary Detonator, No. 8 strength, 37 mm length, 3.7 mm shell diameter. PESO 1106. For boulder blasting, secondary blasting, quarry & non-gassy underground.',
        'name': 'Ordinary Detonators',
        'display_name': 'Ordinary Detonator.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'NEO OD — Aluminium plain ordinary detonator of No. 8 strength, commonly used with safety fuse. Effective initiation of cap-sensitive explosives.',
        'brand': 'NEO OD',
        'hero_bg': 'images/hero/blast-mountain.jpg',
        'product_image': 'images/products/ordinary-detonator-100.png',
        'overview_title': 'Ordinary Detonator — for safe initiation with <span class="accent">safety fuse.</span>',
        'overview': [
            '<strong>SBL Energy</strong> is manufacturing Ordinary Detonators under the brand name <strong>NEO OD</strong>. The PESO ID of the product is <strong>1106</strong>. The Aluminium Plain Ordinary Detonator, non-electric in nature, is commonly used with Safety fuse.',
            'These detonators are of <strong>No. 8 strength</strong>. The Detonators have <strong>37 mm length</strong> and Diameter of Shell is <strong>3.7 mm</strong>. These Detonators are manufactured in an extremely modern plant using highly sophisticated techniques.',
            'Detonator of No. 8 strength ensures effective initiation of Cap Sensitive Explosive. It is initiated when a piece of safety fuse is inserted into the cap.',
        ],
        'advantages': [
            'Aluminium plain shell, non-electric in nature',
            'No. 8 strength — ensures effective initiation of Cap-Sensitive Explosives',
            '37 mm length, 3.7 mm shell diameter — standard form factor',
            'Commonly used with Safety fuse',
            'Manufactured in an extremely modern plant using highly sophisticated techniques',
            'PESO Brand ID: 1106',
        ],
        'safety': [
            'Use standard quality of Crimper to ensure proper crimping of Detonator',
            'Plain Detonators contain sensitive ingredients and must be handled with care and respect at all times',
            'Use adequate length of Safety fuse to allow escape of shot-firer to safe distance in sufficient time',
            'Store at moderate temperatures and dry conditions',
        ],
        'applications': 'Detonators are more effective in Dry holes. They can be used for Boulder blasting, Secondary blasting, Safe initiation in quarry blasting and in non-gassy underground, open-cast mines, surface excavations, well sinking, road construction, civil works etc.',
        'related': related_for('ordinary-detonator'),
    },

    'electric-detonator': {
        'title': 'Electric Detonator (NEO ED / MSDD) Manufacturer in India | SBL Energy',
        'desc': 'NEO ED & MSDD — Instantaneous and Delay Electric Detonators. No.8 strength, aluminium shell, ASA + PETN charge, PVC-plug waterproofed. PESO 630 / 631.',
        'name': 'Electric Detonators',
        'display_name': 'Electric Detonator.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'Electric detonators with electricity as the source of initiation — instantaneous (IED), short-delay (SDD) and long-delay (LDD) variants.',
        'brand': ['NEO ED', 'MSDD'],
        'hero_bg': 'images/hero/blast-panoramic.jpg',
        'product_image': 'images/products/electric-detonator-bundles.png',
        'overview_title': 'Accurate delay timing — engineered for <span class="accent">precision blasting.</span>',
        'overview': [
            'Electric Detonator — the source of initiation for these detonators is <strong>electricity</strong>. There are three types of electric detonators produced, namely: <strong>instantaneous electrical detonators (IED), short delay detonators (SDD) and long delay detonators (LDD)</strong>. SDDs are measured in milliseconds and LDDs are measured in seconds.',
            'Electric detonators are sensitive to heat, shock, static electricity, radio frequency energy, and electromagnetic radiation — they must be handled with appropriate care.',
            '<strong>NEO ED</strong> is a No. 8 Strength Instantaneous Detonator. The Shell of the Detonator is made of <strong>Aluminium</strong> which consists of <strong>ASA as primary charge and PETN as secondary Charge</strong>. The PVC plug makes the detonator moisture-proof and water-proof.',
        ],
        'advantages': [
            'Accurate delay timing',
            'Waterproof',
            'Abrasion-resistant insulation',
            'NEO ED is a No. 8 Strength Instantaneous Detonator',
            'Shell of Detonator made of Aluminium — ASA primary charge &amp; PETN secondary charge',
            'PVC plug makes the detonator moisture-proof and water-proof',
        ],
        'safety': [
            'Electric detonators are sensitive to heat, shock, static electricity, radio frequency energy and electromagnetic radiation',
            'Always keep ends of leg wires shunted until just prior to connections',
            'Disconnect firing cable from the exploder if the circuit requires re-checking',
            'Handle with care and store per PESO guidelines',
        ],
        'applications': 'Instantaneous Electric Detonators (IED) are used for blasting in quarries, opencast and non-gassy underground mines. The IEDs are connected with Detonating Fuse / Explosive in series and is connected with Exploder for firing.',
        'related': related_for('electric-detonator'),
    },

    'non-electric-detonator': {
        'title': 'Non Electric Detonator (NEO DET / DTS / STL) — SBL Energy Limited',
        'desc': 'NEO DET, NEO DTS & NEO STL non-electric detonators. Shock-tube initiation system — insensitive to electricity, RF energy & EM radiation. PESO 632/635/636.',
        'name': 'Non-Electric Detonators',
        'display_name': 'Non-Electric Detonator.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'Shock-tube initiation system — used worldwide for both commercial and military operations. Wide operational flexibility and superior safety.',
        'brand': ['NEO DET', 'NEO DTS', 'NEO STL'],
        'hero_bg': 'images/hero/blast-mountain.jpg',
        'product_image': 'images/products/non-electric-detonator-bundles.png',
        'overview_title': 'Shock-tube initiation — flexibility &amp; <span class="accent">superior safety.</span>',
        'overview': [
            'These are widely used across the world. The source of initiation for these detonators is a <strong>shock wave</strong> which circulates in a tube from one detonator to another. Besides being used for commercial operations, these are also used for military operations. This initiation system consists of shock tubes connected to down-the-hole detonators and surface connectors. These can also use chemical reactions such as rapid burning or violent detonations, to initiate explosive charges.',
            'Apart from all the benefits of an electric detonator, these offer a <strong>wide operational flexibility</strong> (easier to design larger initiation sequences, theoretically with an unlimited number of delays) and <strong>more safety</strong> (insensitivity to electricity, radio frequency energy, and electromagnetic radiation). Less interruption as they provide better safety: accidental initiation by static electricity, stray electrical currents, etc.',
            '<strong>NEO DET</strong> is a non-electric initiating device used in Blasting, comprising of both DTHD and STLD in one set (Twin Det). It consists in one coil of shock tube, one end of which is crimped with DTHD and the other end is crimped with STLD. Thus, it is useful for down-the-hole delay initiation and also surface initiation in the blast. It is used in those mines where the drilling and charge loading patterns are fixed. This enables to reduce the waste of shock tube in the usages of DTHD and STLD separately. STLD is housed in a suitable connector, which has a provision to connect 6 shock tubes for initiation. Each NEODET has length-indicating stickers and delay-time indicating stickers for DTHD and STLD separately for easy identification and handling. The delay detonator is of No. 8 strength. NEO DET provides unlimited delay periods and sequences to conduct large-scale blasts. It is available as per the customer\'s requirement up to 50 meter lengths.',
        ],
        'advantages': [
            'Apart from all the benefits of an electric detonator, these offer a wide operational flexibility (easier to design larger initiation sequences, theoretically with an unlimited number of delays)',
            'More safety — insensitivity to electricity, radio frequency energy, and electromagnetic radiation',
            'Less interruption — better safety from accidental initiation by static electricity, stray electrical currents, etc.',
            'STLD is used for surface hook-up — totally eliminates the air-blast noise',
            'Provides necessary relief delay to reduce the back-break and provides a good free face for the next drilling operation',
            'No disturbance of stemming column; no desensitisation of explosive column — higher explosive efficiency achieved',
            'Bottom initiation and ground vibration can be controlled',
            'Ultimate number of delays — particularly helpful in large blasts',
            'Leakage current in conductive ore bodies and watery hole will not cause misfire',
        ],
        'safety': [
            'Less prone to accidental initiation than electric detonators',
            'Insensitive to electricity, RF energy &amp; electromagnetic radiation',
            'Handle with care and store per PESO guidelines',
            'Keep ends of shock tube protected from contamination',
        ],
        'applications': 'Suitable for surface and underground blasting where complex delay patterns are needed. Recommended in environments with electrical interference, RF activity, conductive ore bodies and watery holes — including commercial and military operations.',
        'related': related_for('non-electric-detonator'),
    },

    'copper-delay-detonator': {
        'title': 'Copper Delay Detonator (NEO CDD / NEO CED) | SBL Energy Limited',
        'desc': 'NEO CDD & NEO CED — Permitted Copper Delay & Instantaneous Detonators. Copper shells with PETN base charge, PVC-coated leg wires. PESO 634 / 633.',
        'name': 'Copper Delay Detonators',
        'display_name': 'Copper Delay Detonator.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'Copper shells filled with PETN as the base charge mixed with a primary charge — fitted to an electric fuse head with PVC-coated leg wires.',
        'brand': ['NEO CDD', 'NEO CED'],
        'hero_bg': 'images/hero/coal.jpg',
        'product_image': 'images/products/copper-delay-detonator-bundles.png',
        'overview_title': 'Reliable delay initiation for <span class="accent">underground coal mines.</span>',
        'overview': [
            'This detonator is made of <strong>copper shells filled with PETN as the base charge mixed with a primary charge</strong>. The shells are crimped with a pair of PVC-coated wires and are fitted to an electric fuse head.',
            'Available as <strong>NEO CDD (PESO 634)</strong> — Permitted Copper Delay Detonator — and <strong>NEO CED (PESO 633)</strong> — Permitted Copper Instantaneous Detonator. Both are PESO-approved for use in coal mines.',
        ],
        'advantages': [
            'Reliable means of delay initiation in underground coal mines',
            'Provides required free face for successive rows of holes in solid blasting',
            'Copper shells with PETN base charge — consistent performance',
            'PVC-coated leg wires — moisture resistant',
            'Both permitted delay (NEO CDD) and permitted instantaneous (NEO CED) variants',
            'Multiple package sizes: DBD, DBF, DBI, DBL',
        ],
        'safety': [
            'Always keep the ends of wires shunted and open just prior to connections — disconnect the firing cable from the exploder if the circuit requires re-checking',
            'Delay Detonators contain sensitive components and must be handled with care at all times',
            'While using, the total circuit resistance is to be monitored to ensure recommended flow of current',
        ],
        'applications': 'Reliable means of delay initiation in underground coal mines, which provides required free face for successive rows of holes in solid blasting.',
        'related': related_for('copper-delay-detonator'),
    },

    'electronic-detonator': {
        'title': 'Electronic Detonator (NEO E-DET) Manufacturer in India | SBL Energy',
        'desc': 'NEO E-DET — fit-for-purpose electronic detonator blasting system. 1 ms increments, 15,000 ms max delay, 3000+ modules. Highest quality, security and precise timing.',
        'name': 'Electronic Detonators',
        'display_name': 'Electronic Detonator.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'NEO E-DET — fit-for-purpose electronic detonator-based blasting system providing the highest level of quality, security, control and precise timing.',
        'brand': 'NEO E-DET',
        'hero_bg': 'images/hero/blast-panoramic.jpg',
        'product_image': 'images/products/electronic-detonator-system.png',
        'overview_title': 'Electronic Detonator <span class="accent">Blasting System.</span>',
        'overview': [
            '<strong>NEO E-DET</strong> is a fit-for-purpose electronic detonator-based blasting system that provides the highest level of quality, security, control and precise timing to ensure compliant, consistent blasting results.',
            'It can be used in a variety of applications including quarrying, mining, demolition and other specialist areas. The high strength detonator is suitable for initiating most priming charges. Complex firing patterns can be easily transferred to the detonators through the use of computer-based software, when implemented properly the highly accurate initiation timings offer benefits in vibration control, fragmentation and general blast optimisation.',
            'The digital firing system used for initiation means each firing circuit and individual detonator is tested and a record retained in the software prior to firing. The circuit can only be initiated by specialist firing equipment offering benefit in safety and security over traditional systems.',
            '<strong>Electronic Detonators contain a capacitor, a logic and timing circuit, and explosives within a copper shell. Every detonator is equipped with a connector.</strong>',
        ],
        'advantages': [
            'Communication — Fully testable 2-way',
            'Timing — programmable, re-programmable, pre-programmable',
            'Traceability — Unique ID number per detonator',
            'Maximum time delay: 15,000 ms',
            'Minimum increment: 1 ms',
            'Delay accuracy: 0.1% ± 0.5 ms',
            'Operating temperature: −20 °C to +80 °C',
            'Immunity to ESD: 30 kVKV &amp; 2500 PF',
            'Anti AC/DC — AC 220 V no damage, DC 48 V no damage',
            'ESD resistance compliant to EN 13763-13',
            'Maximum number of modules: 3,000+ (Master-Slave Mode)',
        ],
        'safety': [
            'Each firing circuit and individual detonator is tested and a record retained in the software prior to firing',
            'Circuit can only be initiated by specialist firing equipment — secure by design',
            'Inherent safety advantages over traditional detonator systems',
            'Follow PESO regulations for electronic detonator handling, storage and use',
        ],
        'applications': 'Can be used in a variety of applications including quarrying, mining, demolition and other specialist areas. The high strength detonator is suitable for initiating most priming charges. Highly accurate initiation timings offer benefits in vibration control, fragmentation and general blast optimisation.',
        'related': related_for('electronic-detonator'),
    },

    'detonating-fuse': {
        'title': 'Detonating Fuse (NEO CORD) Manufacturer | SBL Energy Limited',
        'desc': 'NEO CORD detonating fuse / cord — PETN core, water & abrasion resistant, high tensile strength. PESO 1031, 1153, 1154, 1155. UN 0065, Class 1.1 D.',
        'name': 'Detonating Fuse',
        'display_name': 'Detonating Fuse.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'A core of high explosives (PETN) enclosed in PP yarn, plastic sheathing and synthetic fibre — for safe and quick initiation of detonator-sensitive industrial explosives.',
        'brand': ['NEO CORD', 'NEO CORD 8', 'NEO CORD 12', 'NEO CORD 20'],
        'hero_bg': 'images/hero/blast-mountain.jpg',
        'product_image': 'images/products/detonating-fuse-spools.png',
        'overview_title': 'PETN at the core — safe &amp; quick <span class="accent">non-electric initiation.</span>',
        'overview': [
            'Detonating cord or fuse is a <strong>core of high explosives, normally PETN (pentaerythritol tetranitrate)</strong>, enclosed in PP yarn, plastic sheathing (polyethene jacket) &amp; natural &amp; synthetic fibre for waterproofing. It is basically PETN in covering of textile, plastic &amp; waterproofing material.',
            'The degree of tensile strength, abrasion resistance, &amp; flexibility of each covering varies. It acts as a means for <strong>safe &amp; quick initiation of detonator-sensitive industrial explosives</strong> &amp; provides a path for initiation of non-electric detonators.',
            'Available in four variants — NEO CORD (10 g/m), NEO CORD 8 (8 g/m), NEO CORD 12 (12 g/m) and NEO CORD 20 (20 g/m) — with PESO Brand IDs 1031, 1153, 1154 and 1155 respectively.',
        ],
        'advantages': [
            'Relatively insensitive to detonation by heat, electrostatic discharge or other forms of electricity',
            'Excellent resistance to side penetration by oil or water — water &amp; abrasion resistant',
            'High tensile strength',
            'Easy to handle and to tie into knots',
            'Flexible',
            'Easy identification due to different colours',
            'Electronically &amp; mechanically inspected',
            'Assures reliable non-electric initiation',
            'Safer to use as compared to any other blasting cap — less risk in handling &amp; loading',
            'Easy to connect branch lines',
        ],
        'safety': [
            'Should be kept protected from water in a wet environment — detonating cord does not initiate if it\'s wet, since PETN absorbs water and becomes insensitive to detonation. However, it can be initiated from the dry end',
            'Detonating cord is an explosive, thus, should be handled and transported carefully at all times',
            'It is sensitive to direct lightning strike and intense impact or friction while handling and being exposed with extremely high temperatures (mostly above 70°C)',
        ],
        'applications': 'The product is used for trunkline and downline for initiating explosive. Suitable for opencast mines, quarries, trenching and tunneling work. Initiation by Number 6 Detonator.',
        'related': related_for('detonating-fuse'),
    },

    'cast-booster': {
        'title': 'Cast Booster (NEO BOOST) Manufacturer in India | SBL Energy Limited',
        'desc': 'NEO BOOST — Cast Boosters in 25g, 100g, 250g, 500g. PETN + TNT in plastic shell. VOD 6500 m/s, density 1.55 g/cc, 24-month shelf life. PESO Class 3 Div 2.',
        'name': 'Cast Boosters',
        'display_name': 'Cast Booster.',
        'category': 'EXPLOSIVES ACCESSORIES',
        'tagline': 'NEO BOOST — high-density PETN + TNT cast boosters in a plastic shell, designed to provide high initiation / detonation pressure to a wide range of explosives.',
        'brand': ['NEO BOOST 25 gms', 'NEO BOOST 100 gms', 'NEO BOOST 250 gms', 'NEO BOOST 500 gms'],
        'hero_bg': 'images/hero/blast-mountain.jpg',
        'product_image': 'images/products/cast-booster-sizes.png',
        'overview_title': 'High-strength PETN + TNT <span class="accent">cast boosters.</span>',
        'overview': [
            'Cast boosters are designed to provide <strong>high initiation / detonation pressure</strong> to a wide range of explosives / blasting agents. They consist of high density molecular explosive (<strong>PETN AND TNT</strong>) which are sensitive to intense impact, heat or friction, in a plastic shell.',
            'Each booster has two longitudinal passages that accommodate a detonator or detonating cord. Cast boosters are needed when a detonator doesn\'t have an adequate amount of energy to directly initiate an explosive. It detonates a cast booster which then delivers the shock waves to the explosive or blasting agent. A recessed well at the base of the booster provides protection to the Detonating cord, signal tube or lead wires from any damage.',
            '<strong>SBL Energy Limited</strong> comes from the family of some of the prominent Cast Booster Manufacturers in India that offers high detonation pressure to a wide range of explosives and blasting agents. The reason why our clients have chosen us for the cast boosters because it not only has a long storage life, but it also has an easy operation. Right from its good shelf life to its high resistance for water and oil, the cast boosters are extremely convenient to use and assemble.',
            '<strong>SBL Energy offers cast boosters in 25 gms, 100 gms, 250 gms &amp; 500 gms as per the needs of our clients.</strong>',
        ],
        'advantages': [
            'Cast Boosters have long storage life since it has no liquid ingredients and can be operated easily',
            'Excellent shelf life, highly resistant to water and oil',
            'Convenient to use and assemble',
            'Do not contain Nitro-Glycerin, hence, less sensitive to shock and friction',
            'High density and a high velocity of detonation maximises performance and makes them good primers and boosters',
        ],
        'safety': [
            'Should be transported, stored and handled with care',
            'Avoid impact with solid surfaces or other Cast Boosters — this may lead damage that could lead to a misfire, or a premature initiation',
            'Should be transported, stored and handled with care',
            'Also, usage of boosters with detonators that cannot be completely fitted within the boosters should be strictly avoided as the protected wire might be harmed during charging if not watched — this could lead to untimely detonation',
            'Cast boosters may be used at temperatures up to 65 °C',
        ],
        'applications': 'Initiation of non-cap sensitive charges in a bore hole, at any fixed point in a column of explosives charge. Used with ANFO, cartridges and bulk explosives to prime the boreholes.',
        'related': related_for('cast-booster'),
    },
}

# ============================================================================
# MERGE SPEC DATA + WRITE PAGES
# ============================================================================

def write(filename, html_text):
    path = ROOT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_text)
    print(f"  wrote {filename}  ({len(html_text)} bytes)")

# Merge per-product spec tables and galleries from specs.py
try:
    from specs import SPECS
    for slug, extras in SPECS.items():
        if slug in PRODUCTS:
            PRODUCTS[slug].update(extras)
except ImportError:
    print("WARN: specs.py not found — pages will render without spec tables")

print(f"\n=== Writing {len(PRODUCTS)} product pages ===")
for slug, data in PRODUCTS.items():
    write(f"{slug}.html", product_page(data))

print("\nDone.")
