#!/usr/bin/env python3
import os, glob, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# ---------------------------------------------------------------- shared chrome
TOPBAR = '''<div class="topbar">
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
</div>'''

# The 3-column mega dropdown (base indent = 10 spaces to match existing markup)
MEGA = '''          <div class="dropdown wide mega">
            <div class="drop-col">
              <a href="packaged-explosives.html" class="drop-head">Packaged Explosives</a>
              <a href="packaged-explosives.html?filter=slurry">Slurry Explosives</a>
              <a href="packaged-explosives.html?filter=emulsion">Emulsion Explosives</a>
              <a href="packaged-explosives.html?filter=seismic">Seismic Explosives</a>
            </div>
            <div class="drop-col">
              <a href="bulk.html" class="drop-head">Bulk Explosives</a>
              <a href="bulk.html?filter=bulk-emulsion">Bulk Emulsion</a>
            </div>
            <div class="drop-col">
              <a href="initiating-systems.html" class="drop-head">Initiating Systems</a>
              <a href="initiating-systems.html?filter=non-electric">Non-Electric Detonator</a>
              <a href="initiating-systems.html?filter=copper-delay">Copper Delay Detonator</a>
              <a href="initiating-systems.html?filter=electronic">Electronic Detonator</a>
              <a href="initiating-systems.html?filter=ordinary">Ordinary Detonator</a>
              <a href="initiating-systems.html?filter=cast-booster">Cast Booster</a>
              <a href="initiating-systems.html?filter=detonating-fuse">Detonating Fuse</a>
            </div>
            <div class="drop-col">
              <a href="defense.html" class="drop-head">Defense</a>
              <a href="defense.html?filter=tnt">TNT</a>
              <a href="defense.html?filter=hmx">HMX</a>
              <a href="defense.html?filter=rdx">RDX</a>
              <a href="defense.html?filter=pyro">Pyro Devices</a>
            </div>
            <div class="drop-col">
              <a href="chemicals.html" class="drop-head">Chemicals</a>
              <a href="chemicals.html?filter=petn">PETN</a>
              <a href="chemicals.html?filter=ammonium-nitrate">Ammonium Nitrate</a>
            </div>
          </div>'''

# Mega with Defense but no Chemicals — replaced across already-built pages.
OLD_MEGA3 = '''          <div class="dropdown wide mega">
            <div class="drop-col">
              <a href="packaged-explosives.html" class="drop-head">Packaged Explosives</a>
              <a href="packaged-explosives.html?filter=slurry">Slurry Explosives</a>
              <a href="packaged-explosives.html?filter=emulsion">Emulsion Explosives</a>
              <a href="packaged-explosives.html?filter=seismic">Seismic Explosives</a>
            </div>
            <div class="drop-col">
              <a href="bulk.html" class="drop-head">Bulk Explosives</a>
              <a href="bulk.html?filter=bulk-emulsion">Bulk Emulsion</a>
            </div>
            <div class="drop-col">
              <a href="initiating-systems.html" class="drop-head">Initiating Systems</a>
              <a href="initiating-systems.html?filter=non-electric">Non-Electric Detonator</a>
              <a href="initiating-systems.html?filter=copper-delay">Copper Delay Detonator</a>
              <a href="initiating-systems.html?filter=electronic">Electronic Detonator</a>
              <a href="initiating-systems.html?filter=ordinary">Ordinary Detonator</a>
              <a href="initiating-systems.html?filter=cast-booster">Cast Booster</a>
              <a href="initiating-systems.html?filter=detonating-fuse">Detonating Fuse</a>
            </div>
            <div class="drop-col">
              <a href="defense.html" class="drop-head">Defense</a>
              <a href="defense.html?filter=tnt">TNT</a>
              <a href="defense.html?filter=hmx">HMX</a>
              <a href="defense.html?filter=rdx">RDX</a>
              <a href="defense.html?filter=pyro">Pyro Devices</a>
            </div>
          </div>'''

# Previous mega variants (without Defense) — replaced across already-built pages.
# v1: with Low Column Charge.  v2: after Low Column Charge removed.
OLD_MEGA = '''          <div class="dropdown wide mega">
            <div class="drop-col">
              <a href="packaged-explosives.html" class="drop-head">Packaged Explosives</a>
              <a href="packaged-explosives.html?filter=slurry">Slurry Explosives</a>
              <a href="packaged-explosives.html?filter=emulsion">Emulsion Explosives</a>
              <a href="packaged-explosives.html?filter=low-column">Low Column Charge</a>
              <a href="packaged-explosives.html?filter=seismic">Seismic Explosives</a>
            </div>
            <div class="drop-col">
              <a href="bulk.html" class="drop-head">Bulk Explosives</a>
              <a href="bulk.html?filter=bulk-emulsion">Bulk Emulsion</a>
            </div>
            <div class="drop-col">
              <a href="initiating-systems.html" class="drop-head">Initiating Systems</a>
              <a href="initiating-systems.html?filter=non-electric">Non-Electric Detonator</a>
              <a href="initiating-systems.html?filter=copper-delay">Copper Delay Detonator</a>
              <a href="initiating-systems.html?filter=electronic">Electronic Detonator</a>
              <a href="initiating-systems.html?filter=ordinary">Ordinary Detonator</a>
              <a href="initiating-systems.html?filter=cast-booster">Cast Booster</a>
              <a href="initiating-systems.html?filter=detonating-fuse">Detonating Fuse</a>
            </div>
          </div>'''

OLD_MEGA2 = '''          <div class="dropdown wide mega">
            <div class="drop-col">
              <a href="packaged-explosives.html" class="drop-head">Packaged Explosives</a>
              <a href="packaged-explosives.html?filter=slurry">Slurry Explosives</a>
              <a href="packaged-explosives.html?filter=emulsion">Emulsion Explosives</a>
              <a href="packaged-explosives.html?filter=seismic">Seismic Explosives</a>
            </div>
            <div class="drop-col">
              <a href="bulk.html" class="drop-head">Bulk Explosives</a>
              <a href="bulk.html?filter=bulk-emulsion">Bulk Emulsion</a>
            </div>
            <div class="drop-col">
              <a href="initiating-systems.html" class="drop-head">Initiating Systems</a>
              <a href="initiating-systems.html?filter=non-electric">Non-Electric Detonator</a>
              <a href="initiating-systems.html?filter=copper-delay">Copper Delay Detonator</a>
              <a href="initiating-systems.html?filter=electronic">Electronic Detonator</a>
              <a href="initiating-systems.html?filter=ordinary">Ordinary Detonator</a>
              <a href="initiating-systems.html?filter=cast-booster">Cast Booster</a>
              <a href="initiating-systems.html?filter=detonating-fuse">Detonating Fuse</a>
            </div>
          </div>'''

def navbar(active_products=True):
    cls = ' class="active"' if active_products else ''
    return '''<header class="navbar" id="navbar">
  <div class="container nav-inner">
    <a href="index.html" class="logo">
      <img src="images/logo/sbl-energy-wordmark.png" alt="SBL Energy Limited" class="logo-img" />
    </a>

    <nav class="nav-menu">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li class="has-drop">
          <a href="about.html">About Us <span class="caret">▾</span></a>
          <div class="dropdown">
            <a href="about.html">Company Profile</a>
            <a href="people-clients.html">People &amp; Clients</a>
          </div>
        </li>
        <li class="has-drop">
          <a href="#"''' + cls + ''' >Products <span class="caret">▾</span></a>
''' + MEGA + '''
        </li>
        <li><a href="services.html">Services</a></li>
        <li><a href="career.html">Career</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>

    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary btn-sm">Get an Estimate <span class="arrow">→</span></a>
      <button class="burger" id="burger" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>'''

FOOTER = '''<footer class="footer">
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
        <a href="people-clients.html">People &amp; Clients</a>
        <a href="career.html">Career</a>
        <a href="services.html">Services</a>
      </div>
      <div class="footer-col">
        <h4>Products</h4>
        <a href="packaged-explosives.html">Packaged Explosives</a>
        <a href="bulk.html">Bulk Explosives</a>
        <a href="initiating-systems.html">Initiating Systems</a>
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
</footer>'''

def head(title, desc):
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="''' + desc + '''" />
<title>''' + title + '''</title>
<link rel="icon" type="image/png" href="images/logo/sbl-energy-mark.png" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css" />
</head>
<body>'''

FILTER_JS = '''<script>
(function(){
  var checks = Array.prototype.slice.call(document.querySelectorAll('.filter-check input'));
  var cards  = Array.prototype.slice.call(document.querySelectorAll('.prod-card'));
  var empty  = document.querySelector('.catalog-empty');
  var clear  = document.getElementById('clearFilters');
  function selected(){ return checks.filter(function(c){return c.checked;}).map(function(c){return c.getAttribute('data-filter');}); }
  function apply(updateUrl){
    var sel = selected(), shown = 0;
    cards.forEach(function(card){
      var ok = sel.length === 0 || sel.indexOf(card.getAttribute('data-cat')) > -1;
      card.classList.toggle('is-hidden', !ok);
      if(ok) shown++;
    });
    if(empty) empty.classList.toggle('show', shown === 0);
    if(clear) clear.classList.toggle('show', sel.length > 0);
    if(updateUrl){
      var u = new URL(window.location.href);
      if(sel.length) u.searchParams.set('filter', sel.join(',')); else u.searchParams.delete('filter');
      window.history.replaceState(null, '', u);
    }
  }
  var params = new URLSearchParams(window.location.search);
  var pre = (params.get('filter') || '').split(',').filter(Boolean);
  checks.forEach(function(c){ if(pre.indexOf(c.getAttribute('data-filter')) > -1) c.checked = true; });
  checks.forEach(function(c){ c.addEventListener('change', function(){ apply(true); }); });
  if(clear) clear.addEventListener('click', function(){ checks.forEach(function(c){ c.checked = false; }); apply(true); });
  apply(false);
})();
</script>'''

def cat_tabs(active):
    items = [('packaged-explosives.html','Packaged Explosives','packaged'),
             ('bulk.html','Bulk Explosives','bulk'),
             ('initiating-systems.html','Initiation Systems','initiating'),
             ('defense.html','Defense','defense'),
             ('chemicals.html','Chemicals','chemicals')]
    out = ['    <nav class="cat-tabs">']
    for href,label,key in items:
        a = ' active' if key==active else ''
        out.append('      <a class="cat-tab%s" href="%s">%s</a>' % (a, href, label))
    out.append('    </nav>')
    return '\n'.join(out)

def cta(h2, p):
    return '''<section class="cta-strip">
  <div class="container cta-inner">
    <div class="cta-text">
      <h2>''' + h2 + '''</h2>
      <p>''' + p + '''</p>
    </div>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-white">Get an Estimate <span class="arrow">→</span></a>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------- product data
# (cat key, label, count image used for all of its products)
TYPES_INIT = [
    ('non-electric',  'Non-Electric',    'images/products/non-electric-detonator.png'),
    ('copper-delay',  'Copper Delay',    'images/products/copper-delay-detonator.jpg'),
    ('electronic',    'Electronic',      'images/products/electronic-detonator.jpg'),
    ('ordinary',      'Ordinary',        'images/products/ordinary-detonator.png'),
    ('cast-booster',  'Cast Booster',    'images/products/cast-booster.jpg'),
    ('detonating-fuse','Detonating Fuse','images/products/detonating-fuse.jpg'),
]

# slug, name, cat, desc
PRODUCTS_INIT = [
    ('neo-det','NEO DET','non-electric','Twin Det combining a down-the-hole and a surface delay detonator in a single set.'),
    ('neo-dts','NEO DTS','non-electric','Down-the-hole shock-tube delay detonator for in-hole initiation.'),
    ('neo-stl','NEO STL','non-electric','Surface trunk-line delay detonator for noiseless surface hook-up.'),
    ('neo-cdd','NEO CDD','copper-delay','Copper-shell delay detonator for delay initiation in underground coal mines.'),
    ('neo-ced','NEO CED','copper-delay','Copper electric detonator variant for gassy underground conditions.'),
    ('neo-e-det','NEO E-DET','electronic','Fully programmable electronic detonator for precise, secure timing.'),
    ('neo-od','NEO OD','ordinary','Aluminium plain ordinary detonator of No. 8 strength for cap-sensitive explosives.'),
    ('neo-boost','NEO BOOST','cast-booster','High-density PETN + TNT cast booster — available in 25, 100, 250 and 500 g sizes.'),
    ('neo-cord','NEO CORD','detonating-fuse','PETN-cored detonating fuse — available in 8, 12 and 20 g/m core loads.'),
]

TYPES_BULK = [('bulk-emulsion','Bulk Emulsion','images/products/bulk-truck-user.jpg')]
PRODUCTS_BULK = [
    ('neo-bulk','NEO BULK','bulk-emulsion','Site-mixed bulk emulsion sensitised on loading — for shovel and dragline bench blasting.'),
]

TYPES_PKG = [
    ('slurry',   'Slurry',   'images/products/slurry-explosives.jpg'),
    ('emulsion', 'Emulsion', 'images/products/emulsion-explosives.jpg'),
    ('seismic',  'Seismic',  'images/products/seismic-neogel-box.png'),
]
PRODUCTS_PKG = [
    ('neo-col-special',  'NEO COL (Special)',  'slurry','Cartridged slurry (water-gel) explosive.'),
    ('neo-base-special', 'NEO BASE (Special)', 'slurry','Cartridged slurry (water-gel) explosive.'),
    ('neo-prime-special','NEO PRIME (Special)','slurry','Cartridged slurry (water-gel) explosive.'),
    ('neo-blast-special','NEO BLAST (Special)','slurry','Cartridged slurry (water-gel) explosive.'),
    ('neo-prime',        'NEO PRIME',          'emulsion','Cartridged emulsion explosive.'),
    ('neo-blast',        'NEO BLAST',          'emulsion','Cartridged emulsion explosive.'),
    ('neo-base',         'NEO BASE',           'emulsion','Cartridged emulsion explosive.'),
    ('neo-column',       'NEO COLUMN',         'emulsion','Cartridged emulsion explosive.'),
    ('dyno-power-90',    'DYNO POWER-90',      'emulsion','Cartridged emulsion explosive.'),
    ('neo-gel-90',       'NEO GEL 90',         'emulsion','Cartridged emulsion explosive.'),
    ('neo-gel-901',      'NEO GEL 901',        'emulsion','Cartridged emulsion explosive.'),
    ('neo-dyne',         'NEO DYNE',           'emulsion','Cartridged emulsion explosive.'),
    ('neo-gel-90-cpt',   'NEO GEL-90 CPT',     'seismic','Seismic emulsion explosive for exploration.'),
]

DEF_IMG = 'images/products/defense-placeholder.svg'
TYPES_DEF = [
    ('tnt',  'TNT',          DEF_IMG),
    ('hmx',  'HMX',          DEF_IMG),
    ('rdx',  'RDX',          DEF_IMG),
    ('pyro', 'Pyro Devices', DEF_IMG),
]
PRODUCTS_DEF = [
    ('tnt',          'TNT',          'tnt', 'Trinitrotoluene — high-explosive fill for defence applications.'),
    ('hmx',          'HMX',          'hmx', 'High-melting explosive (octogen) for defence applications.'),
    ('rdx',          'RDX',          'rdx', 'Research Department Explosive (cyclonite) for defence applications.'),
    ('pyro-devices', 'Pyro Devices', 'pyro','Pyrotechnic devices for defence applications.'),
]

CHEM_IMG = 'images/products/chemical-placeholder.svg'
TYPES_CHEM = [
    ('petn',             'PETN',             CHEM_IMG),
    ('ammonium-nitrate', 'Ammonium Nitrate', CHEM_IMG),
]
PRODUCTS_CHEM = [
    ('petn',             'PETN',             'petn',            'Pentaerythritol tetranitrate — high-explosive base chemical.'),
    ('ammonium-nitrate', 'Ammonium Nitrate', 'ammonium-nitrate','Ammonium nitrate — oxidiser and key explosives feedstock.'),
]

IMG_BY_CAT = {}
for tlist in (TYPES_INIT, TYPES_BULK, TYPES_PKG, TYPES_DEF, TYPES_CHEM):
    for key,label,img in tlist:
        IMG_BY_CAT[key] = img

def product_card(slug, name, cat, desc):
    img = IMG_BY_CAT[cat]
    return ('''          <a class="prod-card" data-cat="''' + cat + '''" href="''' + slug + '''.html">
            <div class="prod-card-img"><img src="''' + img + '''" alt="''' + name + '''" /></div>
            <div class="prod-card-body">
              <h3>''' + name + '''</h3>
              <p>''' + desc + '''</p>
              <span class="discover">Discover <span class="tri">→</span></span>
            </div>
          </a>''')

def filter_sidebar(types, products):
    counts = {}
    for _,_,cat,_ in products:
        counts[cat] = counts.get(cat,0)+1
    rows = []
    for key,label,_ in types:
        rows.append('          <label class="filter-check"><input type="checkbox" data-filter="%s"><span class="box"></span> %s <span class="count">(%d)</span></label>' % (key,label,counts.get(key,0)))
    return '\n'.join(rows)

# ---------------------------------------------------------------- category page
def build_category(filename, title, hero_title, hero_sub, hero_bg, tag, active_tab,
                   types, products, cta_h2, cta_p, meta):
    cards = '\n'.join(product_card(*p) for p in products)
    html = head(title, meta) + '''

''' + TOPBAR + '''

''' + navbar() + '''

<section class="prod-hero">
  <div class="prod-hero-bg" style="background-image:url('""" + hero_bg + """')"></div>
  <div class="prod-hero-overlay"></div>
  <div class="container prod-hero-content">
    <nav class="breadcrumb">
      <a href="index.html">Home</a>
      <span>›</span>
      <a href="#">Products</a>
      <span>›</span>
      <span class="current">''' + hero_title + '''</span>
    </nav>
    <div class="prod-hero-tag"><span class="dot"></span> ''' + tag + '''</div>
    <h1 class="prod-hero-title">''' + hero_title + '''.</h1>
    <p class="prod-hero-sub">''' + hero_sub + '''</p>
  </div>
</section>

<section class="section">
  <div class="container">
''' + cat_tabs(active_tab) + '''

    <div class="catalog-layout">
      <aside class="catalog-aside">
        <a href="https://www.sblenergy.com/_files/ugd/06db74_7aba56dcc5c9456fbe8bcffc8c9c3cb6.pdf" target="_blank" class="download-chip">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download Brochure
        </a>
        <div class="filter-title">Product Type</div>
        <div class="filter-list">
''' + filter_sidebar(types, products) + '''
        </div>
        <span class="filter-clear" id="clearFilters">Clear filters ✕</span>
      </aside>

      <div class="catalog-main">
        <div class="prod-card-grid">
''' + cards + '''
        </div>
        <div class="catalog-empty">No products match the selected filters.</div>
      </div>
    </div>
  </div>
</section>

''' + cta(cta_h2, cta_p) + '''

''' + FOOTER + '''

<script src="js/main.js"></script>
''' + FILTER_JS + '''
</body>
</html>'''
    # fix the hero_bg interpolation (used a different quoting above)
    html = html.replace('""" + hero_bg + """', hero_bg)
    with open(filename,'w') as f:
        f.write(html)
    print('wrote', filename)

# ---------------------------------------------------------------- stub page
CAT_PAGE = {'non-electric':'initiating-systems.html?filter=non-electric',
            'copper-delay':'initiating-systems.html?filter=copper-delay',
            'electronic':'initiating-systems.html?filter=electronic',
            'ordinary':'initiating-systems.html?filter=ordinary',
            'cast-booster':'initiating-systems.html?filter=cast-booster',
            'detonating-fuse':'initiating-systems.html?filter=detonating-fuse',
            'bulk-emulsion':'bulk.html',
            'slurry':'packaged-explosives.html?filter=slurry',
            'emulsion':'packaged-explosives.html?filter=emulsion',
            'seismic':'packaged-explosives.html?filter=seismic',
            'tnt':'defense.html?filter=tnt','hmx':'defense.html?filter=hmx',
            'rdx':'defense.html?filter=rdx','pyro':'defense.html?filter=pyro',
            'petn':'chemicals.html?filter=petn','ammonium-nitrate':'chemicals.html?filter=ammonium-nitrate'}
CAT_NAME = {'non-electric':'Non-Electric Detonators','copper-delay':'Copper Delay Detonators',
            'electronic':'Electronic Detonators','ordinary':'Ordinary Detonators',
            'cast-booster':'Cast Boosters','detonating-fuse':'Detonating Fuse',
            'bulk-emulsion':'Bulk Explosives',
            'slurry':'Slurry Explosives','emulsion':'Emulsion Explosives','seismic':'Seismic Explosives',
            'tnt':'TNT','hmx':'HMX','rdx':'RDX','pyro':'Pyro Devices',
            'petn':'PETN','ammonium-nitrate':'Ammonium Nitrate'}
GROUP_PAGE = {'non-electric':'initiating-systems.html','copper-delay':'initiating-systems.html',
              'electronic':'initiating-systems.html','ordinary':'initiating-systems.html',
              'cast-booster':'initiating-systems.html','detonating-fuse':'initiating-systems.html',
              'bulk-emulsion':'bulk.html',
              'slurry':'packaged-explosives.html','emulsion':'packaged-explosives.html','seismic':'packaged-explosives.html',
              'tnt':'defense.html','hmx':'defense.html','rdx':'defense.html','pyro':'defense.html',
              'petn':'chemicals.html','ammonium-nitrate':'chemicals.html'}
GROUP_NAME = {'non-electric':'Initiating Systems','copper-delay':'Initiating Systems',
              'electronic':'Initiating Systems','ordinary':'Initiating Systems',
              'cast-booster':'Initiating Systems','detonating-fuse':'Initiating Systems',
              'bulk-emulsion':'Bulk Explosives',
              'slurry':'Packaged Explosives','emulsion':'Packaged Explosives','seismic':'Packaged Explosives',
              'tnt':'Defense','hmx':'Defense','rdx':'Defense','pyro':'Defense',
              'petn':'Chemicals','ammonium-nitrate':'Chemicals'}

def build_stub(slug, name, cat, desc):
    img = IMG_BY_CAT[cat]
    back = CAT_PAGE[cat]
    grp_page = GROUP_PAGE[cat]
    grp_name = GROUP_NAME[cat]
    catname = CAT_NAME[cat]
    title = name + ' — SBL Energy Limited'
    html = head(title, desc) + '''

''' + TOPBAR + '''

''' + navbar() + '''

<section class="prod-hero">
  <div class="prod-hero-bg" style="background-image:url('images/hero/blast-mountain.jpg')"></div>
  <div class="prod-hero-overlay"></div>
  <div class="container prod-hero-content">
    <nav class="breadcrumb">
      <a href="index.html">Home</a>
      <span>›</span>
      <a href="''' + grp_page + '''">''' + grp_name + '''</a>
      <span>›</span>
      <a href="''' + back + '''">''' + catname + '''</a>
      <span>›</span>
      <span class="current">''' + name + '''</span>
    </nav>
    <div class="prod-hero-tag"><span class="dot"></span> ''' + catname.upper() + '''</div>
    <h1 class="prod-hero-title">''' + name + '''.</h1>
    <p class="prod-hero-sub">''' + desc + '''</p>
  </div>
</section>

<section class="section">
  <div class="container stub-body">
    <div class="prod-overview-grid" style="grid-template-columns:1fr 1.2fr;gap:48px;align-items:center">
      <div class="prod-img-wrap">
        <div class="prod-img-frame">
          <img src="''' + img + '''" alt="''' + name + '''" />
        </div>
        <div class="prod-img-badge"><span class="badge-tag">SBL ENERGY</span><span class="badge-name">''' + name + '''</span></div>
      </div>
      <div class="prod-text">
        <div class="section-tag"><span class="tag-line"></span> PRODUCT</div>
        <h2 class="section-title">''' + name + '''</h2>
        <p class="prod-para">''' + desc + '''</p>
        <div class="stub-note">Detailed specifications, technical data and packaging information for ''' + name + ''' will be published here.</div>
        <div class="hero-actions" style="margin-top:26px">
          <a href="contact.html" class="btn btn-primary">Request a Quote <span class="arrow">→</span></a>
          <a href="''' + back + '''" class="btn btn-ghost">← Back to ''' + catname + '''</a>
        </div>
      </div>
    </div>
  </div>
</section>

''' + cta('Need a quote for ' + name + '?', 'Our technical team will help you choose the right specification for your site.') + '''

''' + FOOTER + '''

<script src="js/main.js"></script>
</body>
</html>'''
    with open(slug + '.html','w') as f:
        f.write(html)
    print('wrote', slug + '.html')

# ---------------------------------------------------------------- run builds
build_category('initiating-systems.html',
    'Initiating Systems — SBL Energy Limited',
    'Initiating Systems',
    'Detonators, detonating fuse and cast boosters — the complete initiation range for surface and underground blasting.',
    'images/hero/blast-mountain.jpg',
    'OUR PRODUCTS', 'initiating', TYPES_INIT, PRODUCTS_INIT,
    'Need help choosing an initiation system?',
    'Our technical team will help you select the right detonator, fuse or booster for your site.',
    'NEO DET, NEO DTS, NEO E-DET, NEO CDD, NEO BOOST and NEO CORD — SBL Energy initiating systems: detonators, detonating fuse and cast boosters.')

build_category('bulk.html',
    'Bulk Explosives — SBL Energy Limited',
    'Bulk Explosives',
    'Site-mixed, on-borehole-loaded bulk emulsion for quarry and open-pit mining — safer transport, faster loading, lower inventory.',
    'images/hero/manufacturing-floor.jpg',
    'OUR PRODUCTS', 'bulk', TYPES_BULK, PRODUCTS_BULK,
    'Need a bulk emulsion solution?',
    'Our technical team will help you set up a site-mixed bulk system for your operation.',
    'NEO BULK site-mixed bulk emulsion explosives from SBL Energy — for shovel and dragline bench blasting.')

build_category('packaged-explosives.html',
    'Packaged Explosives — SBL Energy Limited',
    'Packaged Explosives',
    'Cartridged slurry, emulsion and seismic explosives — packaged and ready for surface and underground blasting.',
    'images/hero/manufacturing-floor.jpg',
    'OUR PRODUCTS', 'packaged', TYPES_PKG, PRODUCTS_PKG,
    'Need help choosing a packaged explosive?',
    'Our technical team will help you select the right cartridge product for your site.',
    'Slurry, emulsion and seismic cartridged explosives from SBL Energy — NEO COL, NEO PRIME, NEO GEL and DYNO range.')

build_category('defense.html',
    'Defense — SBL Energy Limited',
    'Defense',
    'High-explosive materials and pyrotechnic devices for defence applications.',
    'images/hero/blast-panoramic.jpg',
    'OUR PRODUCTS', 'defense', TYPES_DEF, PRODUCTS_DEF,
    'Looking for defence-grade explosives?',
    'Our technical team will help you with defence material requirements and specifications.',
    'TNT, HMX, RDX and pyrotechnic devices from SBL Energy — high-explosive materials for defence applications.')

build_category('chemicals.html',
    'Chemicals — SBL Energy Limited',
    'Chemicals',
    'Base chemicals and oxidisers — PETN and ammonium nitrate for explosives manufacturing.',
    'images/hero/manufacturing-floor.jpg',
    'OUR PRODUCTS', 'chemicals', TYPES_CHEM, PRODUCTS_CHEM,
    'Need explosives-grade chemicals?',
    'Our technical team will help you with PETN, ammonium nitrate and related chemical requirements.',
    'PETN and ammonium nitrate from SBL Energy — base chemicals and oxidisers for explosives manufacturing.')

for p in PRODUCTS_INIT + PRODUCTS_BULK + PRODUCTS_PKG + PRODUCTS_DEF + PRODUCTS_CHEM:
    build_stub(*p)

# ---------------------------------------------------------------- swap dropdown on existing pages
OLD_BLOCK = '''          <div class="dropdown wide">
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
              <a href="non-electric-detonator.html">Non-Electric Detonator</a>
              <a href="copper-delay-detonator.html">Copper Delay Detonator</a>
              <a href="electronic-detonator.html">Electronic Detonator</a>
              <a href="detonating-fuse.html">Detonating Fuse</a>
              <a href="cast-booster.html">Cast Booster</a>
            </div>
          </div>'''

swapped = 0
for fn in glob.glob('*.html'):
    with open(fn) as f:
        txt = f.read()
    new = txt
    for old in (OLD_BLOCK, OLD_MEGA, OLD_MEGA2, OLD_MEGA3):
        if old in new:
            new = new.replace(old, MEGA)
    if new != txt:
        with open(fn,'w') as f:
            f.write(new)
        swapped += 1
print('dropdown updated on', swapped, 'pages')
