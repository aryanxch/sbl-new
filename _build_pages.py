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
              <a href="packaged-explosives.html?filter=emulsion">Emulsion Explosives</a>
              <a href="packaged-explosives.html?filter=slurry">Slurry Explosives</a>
              <a href="packaged-explosives.html?filter=seismic">Seismic Explosives</a>
            </div>
            <div class="drop-col">
              <a href="bulk.html" class="drop-head">Bulk Explosives</a>
              <a href="bulk.html?filter=bulk-emulsion">Bulk Emulsion</a>
            </div>
            <div class="drop-col">
              <a href="initiating-systems.html" class="drop-head">Initiating Systems</a>
              <a href="initiating-systems.html?filter=electronic">Electronic Detonator</a>
              <a href="initiating-systems.html?filter=non-electric">Non-Electric Detonator</a>
              <a href="initiating-systems.html?filter=copper-delay">Copper Delay Detonator</a>
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

# Previous mega (slurry-first, non-electric-first) — replaced across already-built pages.
OLD_MEGA4 = '''          <div class="dropdown wide mega">
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
  var qsa = function(s){ return Array.prototype.slice.call(document.querySelectorAll(s)); };
  // [checkbox attribute, card attribute, URL param]
  var GROUPS = [
    ['data-filter','data-cat','filter'],
    ['data-app','data-apps','app'],
    ['data-sens','data-sens','sens'],
    ['data-dia','data-dia','dia']
  ];
  var cards = qsa('.prod-card');
  var empty = document.querySelector('.catalog-empty');
  var clear = document.getElementById('clearFilters');
  var allInputs = [];
  GROUPS.forEach(function(g){ g.inputs = qsa('.filter-check input[' + g[0] + ']'); allInputs = allInputs.concat(g.inputs); });
  function sel(g){ return g.inputs.filter(function(c){return c.checked;}).map(function(c){return c.getAttribute(g[0]);}); }
  function apply(updateUrl){
    var picks = GROUPS.map(sel), shown = 0, active = 0;
    picks.forEach(function(p){ active += p.length; });
    cards.forEach(function(card){
      var ok = GROUPS.every(function(g, i){
        if(picks[i].length === 0) return true;
        var vals = (card.getAttribute(g[1]) || '').split(',').filter(Boolean);
        return vals.some(function(x){ return picks[i].indexOf(x) > -1; });
      });
      card.classList.toggle('is-hidden', !ok);
      if(ok) shown++;
    });
    if(empty) empty.classList.toggle('show', shown === 0);
    if(clear) clear.classList.toggle('show', active > 0);
    if(updateUrl){
      var u = new URL(window.location.href);
      GROUPS.forEach(function(g, i){ if(picks[i].length) u.searchParams.set(g[2], picks[i].join(',')); else u.searchParams.delete(g[2]); });
      window.history.replaceState(null, '', u);
    }
  }
  var params = new URLSearchParams(window.location.search);
  GROUPS.forEach(function(g){
    var pre = (params.get(g[2]) || '').split(',').filter(Boolean);
    g.inputs.forEach(function(c){ if(pre.indexOf(c.getAttribute(g[0])) > -1) c.checked = true; });
  });
  allInputs.forEach(function(c){ c.addEventListener('change', function(){ apply(true); }); });
  if(clear) clear.addEventListener('click', function(){ allInputs.forEach(function(c){ c.checked = false; }); apply(true); });
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
# Electronic detonator first — it is the most important initiating system.
TYPES_INIT = [
    ('electronic',    'Electronic',      'images/products/electronic-detonator.jpg'),
    ('non-electric',  'Non-Electric',    'images/products/non-electric-detonator.png'),
    ('copper-delay',  'Copper Delay',    'images/products/copper-delay-detonator.jpg'),
    ('ordinary',      'Ordinary',        'images/products/ordinary-detonator.png'),
    ('cast-booster',  'Cast Booster',    'images/products/cast-booster.jpg'),
    ('detonating-fuse','Detonating Fuse','images/products/detonating-fuse.jpg'),
]

# slug, name, cat, desc  — electronic detonator listed first (most important).
PRODUCTS_INIT = [
    ('neo-e-det','NEO E-DET','electronic','Fully programmable electronic detonator for precise, secure timing.'),
    ('neo-det-combidet','NEO DET COMBIDET','non-electric','Dual-delay twin detonator integrating an in-hole and a surface delay detonator in one unit.'),
    ('neo-det-dth','NEO DET DTH','non-electric','High-strength down-the-hole millisecond-delay detonator for in-hole initiation.'),
    ('neo-det-lpsp','NEO DET LP/SP','non-electric','In-hole delay detonator offered in Long-Period (LP) and Short-Period (SP) delay series.'),
    ('neo-det-stld','NEO DET STLD','non-electric','Surface trunkline delay detonator for hole-to-hole and row-to-row surface sequencing.'),
    ('neo-cdd','NEO CDD','copper-delay','Copper-shell delay detonator for delay initiation in underground coal mines.'),
    ('neo-ced','NEO CED','copper-delay','Copper electric detonator variant for gassy underground conditions.'),
    ('neo-od','NEO OD','ordinary','Aluminium plain ordinary detonator of No. 8 strength for cap-sensitive explosives.'),
    ('neo-boost','NEO BOOST','cast-booster','High-density PETN + TNT cast booster — available in 25, 100, 250 and 500 g sizes.'),
    ('neo-primex','NEO PRIMEX','cast-booster','High-density PETN–TNT cast booster for initiating ANFO, emulsions, watergels and other blasting agents.'),
    ('neo-cord','NEO CORD','detonating-fuse','Flexible, waterproof PETN-cored detonating cord for trunkline and downline initiation.'),
]

TYPES_BULK = [('bulk-emulsion','Bulk Emulsion','images/products/bulk-truck-user.jpg')]
PRODUCTS_BULK = [
    ('neo-bulk','NEO BULK','bulk-emulsion','Site-mixed bulk emulsion sensitised on loading — for shovel and dragline bench blasting.'),
]

# Emulsion listed before Slurry — emulsion products are more important.
TYPES_PKG = [
    ('emulsion', 'Emulsion', 'images/products/emulsion-explosives.jpg'),
    ('slurry',   'Slurry',   'images/products/slurry-explosives.jpg'),
    ('seismic',  'Seismic',  'images/products/seismic-neogel-box.png'),
]
# Emulsion first; within emulsion the priority products lead:
# NEO PRIME, NEO GEL 90, NEO GEL 901, NEO DYNE, DYNO POWER.
PRODUCTS_PKG = [
    ('neo-prime',        'NEO PRIME',          'emulsion','Cartridged emulsion explosive.'),
    ('neo-gel-90',       'NEO GEL 90',         'emulsion','Cap-sensitive, small-diameter cartridged emulsion explosive.'),
    ('neo-gel-901',      'NEO GEL 901',        'emulsion','Cartridged emulsion explosive.'),
    ('neo-dyne',         'NEO DYNE',           'emulsion','Cartridged emulsion explosive.'),
    ('dyno-power-90',    'DYNO POWER-90',      'emulsion','High-strength, cap-sensitive packaged emulsion explosive for priming and column charging.'),
    ('neo-blast',        'NEO BLAST',          'emulsion','Cap-sensitive, large-diameter cartridged emulsion explosive.'),
    ('neo-base',         'NEO BASE',           'emulsion','Booster-sensitive, large-diameter cartridged emulsion explosive.'),
    ('neo-column',       'NEO COLUMN',         'emulsion','Booster-sensitive, large-diameter cartridged emulsion explosive.'),
    ('neo-col-special',  'NEO COL (Special)',  'slurry','Booster-sensitive (non-cap) cartridged slurry (water-gel) explosive.'),
    ('neo-base-special', 'NEO BASE (Special)', 'slurry','Booster-sensitive (non-cap) cartridged slurry (water-gel) explosive.'),
    ('neo-prime-special','NEO PRIME (Special)','slurry','Cap-sensitive cartridged slurry (water-gel) explosive.'),
    ('neo-blast-special','NEO BLAST (Special)','slurry','Cap-sensitive cartridged slurry (water-gel) explosive.'),
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

# ---------------------------------------------------------------- applications
# Application filter taxonomy (slug, label), ordered. Derived from product TDS use cases.
APP_TYPES = [
    ('surface-mining', 'Surface Mining'),
    ('underground',    'Underground'),
    ('quarrying',      'Quarrying'),
    ('tunnelling',     'Tunnelling'),
    ('construction',   'Construction'),
    ('wet-holes',      'Wet / Watery Holes'),
    ('priming',        'Priming &amp; Initiation'),
    ('defence',        'Defence'),
]
# Only products with a TDS have known applications; everything else is untagged.
PRODUCT_APPS = {
    'neo-prime':        ['surface-mining','underground','quarrying','tunnelling','construction','wet-holes','priming'],
    'neo-gel-901':      ['surface-mining','underground','quarrying','tunnelling','construction','wet-holes','priming'],
    'neo-dyne':         ['surface-mining','underground','quarrying','tunnelling','construction','wet-holes','priming'],
    'dyno-power-90':    ['surface-mining','underground','quarrying','tunnelling','wet-holes','priming'],
    'neo-e-det':        ['surface-mining','underground','quarrying','construction'],
    'neo-cord':         ['priming','wet-holes'],
    'neo-det-combidet': ['surface-mining','underground','quarrying','construction'],
    'neo-det-dth':      ['surface-mining','underground','quarrying','construction','priming'],
    'neo-det-lpsp':     ['surface-mining','underground','quarrying','priming'],
    'neo-det-stld':     ['surface-mining','quarrying','construction'],
    'neo-primex':       ['priming','surface-mining','underground'],
    'petn':             ['priming','defence'],
    'tnt':              ['defence'],
}

# ---------------------------------------------------------------- sensitivity / diameter classification
# Two filter axes for packaged products: sensitivity (cap/booster) and cartridge diameter (large/small).
SENS_TYPES = [('cap', 'Cap-sensitive'), ('booster', 'Booster-sensitive')]
DIA_TYPES  = [('large', 'Large Diameter'), ('small', 'Small Diameter')]
# slug -> (sensitivity, diameter|None)
PRODUCT_CLASS = {
    # emulsion
    'neo-prime':        ('cap', 'large'),
    'neo-blast':        ('cap', 'large'),
    'neo-gel-901':      ('cap', 'small'),
    'neo-gel-90':       ('cap', 'small'),
    'neo-dyne':         ('cap', 'small'),
    'dyno-power-90':    ('cap', 'small'),
    'neo-column':       ('booster', 'large'),
    'neo-base':         ('booster', 'large'),
    # slurry (water-gel) — large-diameter cartridges (85/125/200 mm), tagged for filtering
    'neo-prime-special':('cap', 'large'),
    'neo-blast-special':('cap', 'large'),
    'neo-base-special': ('booster', 'large'),
    'neo-col-special':  ('booster', 'large'),
}
# Categories whose product pages should show the diameter in the displayed label.
DIA_LABEL_CATS = {'emulsion'}

def class_label(slug, cat=None):
    c = PRODUCT_CLASS.get(slug)
    if not c:
        return None
    sens, dia = c
    txt = 'Cap-sensitive' if sens == 'cap' else 'Booster-sensitive'
    if dia and (cat is None or cat in DIA_LABEL_CATS):
        txt += ' &middot; ' + ('Large' if dia == 'large' else 'Small') + ' diameter'
    return txt

def product_card(slug, name, cat, desc):
    # Use a dedicated product photo when one exists, else the category image.
    own = 'images/products/%s.png' % slug
    img = own if os.path.exists(own) else IMG_BY_CAT[cat]
    apps = ' data-apps="%s"' % ','.join(PRODUCT_APPS.get(slug, []))
    cls = PRODUCT_CLASS.get(slug)
    clsattr = ''
    if cls:
        clsattr = ' data-sens="%s"' % cls[0] + (' data-dia="%s"' % cls[1] if cls[1] else '')
    # Products with a TDS get a distinct one-line blurb ('card', else tagline) instead of a generic line.
    if slug in RICH:
        desc = RICH[slug].get('card', RICH[slug]['tagline'])
    return ('''          <a class="prod-card" data-cat="''' + cat + '''"''' + apps + clsattr + ''' href="''' + slug + '''.html">
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

def apps_sidebar(products):
    """Applications filter group — only the apps present among this page's products."""
    counts = {}
    for slug,_,_,_ in products:
        for a in PRODUCT_APPS.get(slug, []):
            counts[a] = counts.get(a,0)+1
    rows = []
    for key,label in APP_TYPES:
        if counts.get(key,0) > 0:
            rows.append('          <label class="filter-check"><input type="checkbox" data-app="%s"><span class="box"></span> %s <span class="count">(%d)</span></label>' % (key,label,counts[key]))
    if not rows:
        return ''
    return ('''        <div class="filter-title filter-title-apps">Applications</div>
        <div class="filter-list">
''' + '\n'.join(rows) + '''
        </div>''')

def class_sidebar(products):
    """Sensitivity + Diameter filter groups — only options present among this page's products."""
    sens_c, dia_c = {}, {}
    for slug,_,_,_ in products:
        c = PRODUCT_CLASS.get(slug)
        if not c:
            continue
        sens_c[c[0]] = sens_c.get(c[0],0)+1
        if c[1]:
            dia_c[c[1]] = dia_c.get(c[1],0)+1
    def group(title, attr, types, counts):
        rows = []
        for key,label in types:
            if counts.get(key,0) > 0:
                rows.append('          <label class="filter-check"><input type="checkbox" data-%s="%s"><span class="box"></span> %s <span class="count">(%d)</span></label>' % (attr,key,label,counts[key]))
        if not rows:
            return ''
        return ('''        <div class="filter-title filter-title-apps">''' + title + '''</div>
        <div class="filter-list">
''' + '\n'.join(rows) + '''
        </div>''')
    return (group('Sensitivity', 'sens', SENS_TYPES, sens_c) + '\n'
          + group('Diameter', 'dia', DIA_TYPES, dia_c)).strip('\n')

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
        <a href="assets/brochure/sbl-energy-brochure.pdf" target="_blank" class="download-chip" download>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download Brochure
        </a>
        <div class="filter-title">Product Type</div>
        <div class="filter-list">
''' + filter_sidebar(types, products) + '''
        </div>
''' + class_sidebar(products) + '''
''' + apps_sidebar(products) + '''
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
    html = html.replace('NEO ', 'NEO™ ')  # trademark after the NEO brand
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
    html = html.replace('NEO ', 'NEO™ ')  # trademark after the NEO brand
    with open(slug + '.html','w') as f:
        f.write(html)
    print('wrote', slug + '.html')

# ---------------------------------------------------------------- rich product page
# Full product pages (intro + key specs + use cases + downloadable TDS).
# Slugs listed in RICH are skipped by the stub loop and built here instead.
# Each entry: name, cat, tagline, meta, intro[], specs[(label,val,unit)], specs_note, use_cases[].
# img defaults to the category image; pdf defaults to assets/tds/<slug>-tds.pdf.
EMUL_USE = ['Priming &amp; initiating ANFO columns','Surface mining','Underground operations',
            'Quarrying','Tunnelling','Wet &amp; water-logged boreholes']
ANFO_NOTE = 'RWS &amp; RBS are calculated relative to ANFO at a density of 0.8 g/cc.'

RICH = {
  # ---------------------------------------------------------------- emulsion
  'neo-prime': {
    'name': 'NEO PRIME', 'cat': 'emulsion',
    'card': 'Cap-sensitive, large-diameter emulsion — our highest weight strength (RWS 118%, VOD 4400 m/s) for priming and column charging.',
    'tagline': 'High-strength, cap-sensitive packaged emulsion explosive for priming and column charging.',
    'meta': 'NEO PRIME — high-strength, cap-sensitive packaged emulsion explosive from SBL Energy for priming '
            'and column charging in surface mining, underground, quarrying and tunnelling.',
    'intro': [
      'NEO PRIME is a high-strength, cap-sensitive packaged emulsion explosive with a firm, putty-like consistency. '
      'It is sensitised using chemical gassing, microspheres, or a combination of both, providing a stable and reliable '
      'energy output, while its emulsion matrix offers excellent water resistance for dependable performance in wet or '
      'partially flooded boreholes.',
      'NEO PRIME is designed for priming duties as well as column charging in surface mining, underground operations, '
      'quarrying, tunnelling and general construction blasting. Its high detonation velocity makes it highly effective '
      'for initiating ANFO columns and other non-cap-sensitive bulk or packaged explosives.',
    ],
    'specs': [
      ('Density', '1.15 &plusmn; 0.05', 'g/cc'),
      ('Velocity of Detonation', '4400 &plusmn; 300', 'm/s'),
      ('Relative Weight Strength', '118', '%'),
      ('Relative Bulk Strength', '166', '%'),
    ],
    'specs_note': ANFO_NOTE, 'use_cases': EMUL_USE,
  },
  'neo-gel-901': {
    'name': 'NEO GEL 901', 'cat': 'emulsion',
    'card': 'Cap-sensitive, small-diameter emulsion (RWS 110%, VOD 4500 m/s) for priming and column work.',
    'tagline': 'High-strength, cap-sensitive packaged emulsion explosive for priming and column charging.',
    'meta': 'NEO GEL 901 — high-strength, cap-sensitive packaged emulsion explosive from SBL Energy for priming '
            'and column charging in surface mining, underground, quarrying and tunnelling.',
    'intro': [
      'NEO GEL 901 is a high-strength, cap-sensitive packaged emulsion explosive with a firm, putty-like consistency. '
      'It is sensitised using chemical gassing, microspheres, or a combination of both, providing a stable and reliable '
      'energy output, while its emulsion matrix offers excellent water resistance for dependable performance in wet or '
      'partially flooded boreholes.',
      'NEO GEL 901 is designed for priming duties as well as column charging in surface mining, underground operations, '
      'quarrying, tunnelling and general construction blasting. Its high detonation velocity makes it highly effective '
      'for initiating ANFO columns and other non-cap-sensitive bulk or packaged explosives.',
    ],
    'specs': [
      ('Density', '1.15 &plusmn; 0.05', 'g/cc'),
      ('Velocity of Detonation', '4500 &plusmn; 200', 'm/s'),
      ('Relative Weight Strength', '110', '%'),
      ('Relative Bulk Strength', '165', '%'),
    ],
    'specs_note': ANFO_NOTE, 'use_cases': EMUL_USE,
  },
  'neo-dyne': {
    'name': 'NEO DYNE', 'cat': 'emulsion',
    'card': 'Cap-sensitive, small-diameter column emulsion (RWS 108%, VOD 4300 m/s) — economical medium-strength option.',
    'tagline': 'Medium-strength, cap-sensitive packaged emulsion explosive for column charging.',
    'meta': 'NEO DYNE — medium-strength, cap-sensitive packaged emulsion explosive from SBL Energy for column '
            'charging in surface mining, underground, quarrying, tunnelling and general construction blasting.',
    'intro': [
      'NEO DYNE is a medium-strength, cap-sensitive packaged emulsion explosive with a firm, putty-like consistency. '
      'It is sensitised using chemical gassing, microspheres, or a combination of both, providing a stable and reliable '
      'energy output, while its emulsion matrix offers excellent water resistance for dependable performance in wet or '
      'partially flooded boreholes.',
      'NEO DYNE is designed for use as a column explosive in surface mining, underground operations, quarrying, '
      'tunnelling and general construction blasting. Its high detonation velocity makes it effective for initiating '
      'ANFO columns and other non-cap-sensitive bulk or packaged explosives.',
    ],
    'specs': [
      ('Density', '1.15 &plusmn; 0.05', 'g/cc'),
      ('Velocity of Detonation', '4300 &plusmn; 200', 'm/s'),
      ('Relative Weight Strength', '108', '%'),
      ('Relative Bulk Strength', '162', '%'),
    ],
    'specs_note': ANFO_NOTE,
    'use_cases': ['Column charging','Surface mining','Underground operations','Quarrying',
                  'Tunnelling','General construction blasting'],
  },
  'dyno-power-90': {
    'name': 'DYNO POWER-90', 'cat': 'emulsion',
    'card': 'Cap-sensitive, small-diameter emulsion — our highest VOD (4700 m/s, RWS 115%) for priming and initiating ANFO columns in hard rock.',
    'tagline': 'High-strength, cap-sensitive packaged emulsion explosive for priming and column charging.',
    'meta': 'DYNO POWER-90 — high-strength, cap-sensitive packaged emulsion explosive from SBL Energy. '
            'High VOD and excellent water resistance for priming and column charging in hard rock, underground, quarrying and tunnelling.',
    'intro': [
      'DYNO POWER-90 is a high-strength, cap-sensitive packaged emulsion explosive with a firm, putty-like '
      'consistency. It is sensitised using chemical gassing, microspheres, or a combination of both, providing a '
      'stable and reliable energy output. The emulsion matrix offers excellent water resistance, allowing dependable '
      'performance in wet or partially flooded boreholes.',
      'Designed mainly for priming duties, it can also be used as a column explosive in hard-rock surface mining, '
      'underground operations, quarrying and tunnelling. Its high detonation velocity and robust formulation make it '
      'highly effective for initiating ANFO columns and other non-cap-sensitive bulk or packaged explosives.',
    ],
    'specs': [
      ('Density', '1.15 &plusmn; 0.05', 'g/cc'),
      ('Velocity of Detonation', '4700 &plusmn; 200', 'm/s'),
      ('Relative Weight Strength', '115', '%'),
      ('Relative Bulk Strength', '172', '%'),
    ],
    'specs_note': ANFO_NOTE,
    'use_cases': ['Priming &amp; initiating ANFO columns','Hard-rock surface mining','Underground operations',
                  'Quarrying','Tunnelling','Wet &amp; water-logged boreholes'],
  },
  # ---------------------------------------------------------------- electronic
  'neo-e-det': {
    'name': 'NEO E-DET', 'cat': 'electronic',
    'tagline': 'Fully programmable electronic detonator system for precise, secure, two-wire digital blast initiation.',
    'meta': 'NEO E-DET (Neo-edet) — fully programmable electronic detonator system from SBL Energy for precise delay '
            'timing and secure two-wire digital blast initiation in mining, quarrying and construction.',
    'intro': [
      'NEO E-DET (Neo-edet) is an electronic detonator system designed for precise and reliable blast initiation in '
      'mining, quarrying and construction. It enables accurate control of delay timing, helping achieve consistent '
      'fragmentation, improved blast control and efficient use of explosives.',
      'The system operates on a digital two-wire communication network that allows straightforward field connection, '
      'blast programming and verification before firing. Integrated protection and safety controls — spark-gap '
      'protection, thermal-barrier encapsulation and hardware-plus-software interlocks — help prevent unintended '
      'initiation and ensure stable operation during handling and firing.',
    ],
    'specs': [
      ('Initiation Capacity', 'up to 500', 'det / blast'),
      ('Max Programmable Delay', '25,000', 'ms'),
      ('Timing Accuracy', '0.1%', '&plusmn; 0.5 ms'),
      ('Operating Range', '&minus;20 to 80', '&deg;C'),
    ],
    'specs_note': 'Used with the NEO-EDET&trade; Logger Cum Blaster. Full electrical, wire and shell specifications are in the datasheet.',
    'use_cases': ['Surface mining','Quarrying','Construction blasting','Precise delay sequencing',
                  'Large-scale blasts (up to 500 detonators)','Vibration &amp; fragmentation control'],
  },
  # ---------------------------------------------------------------- detonating fuse
  'neo-cord': {
    'name': 'NEO CORD', 'cat': 'detonating-fuse',
    'tagline': 'Flexible, waterproof PETN-cored detonating cord for trunkline and downline initiation.',
    'meta': 'NEO CORD — flexible, waterproof PETN-cored detonating cord from SBL Energy for trunkline and downline '
            'initiation, available in 8 to 40 g/m core loads.',
    'intro': [
      'NEO CORD is a flexible, waterproof detonating cord consisting of a continuous PETN explosive core enclosed '
      'within layers of high-strength textile fibres and a durable plastic jacket. The construction provides excellent '
      'tensile strength, abrasion resistance and stability under demanding field conditions.',
      'It serves as a reliable trunkline or downline for the rapid, simultaneous initiation of multiple charges, and '
      'for transferring initiation energy to detonator-sensitive explosives. NEO CORD can be initiated by standard '
      'plain, electric, non-electric or electronic detonators and is available in a range of PETN charge weights.',
    ],
    'specs': [
      ('Velocity of Detonation', '7000 &plusmn; 500', 'm/s'),
      ('PETN Core Load', '8 &ndash; 40', 'g/m'),
      ('Breaking Load', '55 &ndash; 95', 'kg'),
      ('Available Grades', '5', 'core loads'),
    ],
    'specs_note': 'Available as NEOCORD 8, 10, 12, 20 and 40 (g/m PETN). The full grade table is in the datasheet.',
    'use_cases': ['Surface trunklines','Borehole downlines','Initiating boosters &amp; primers',
                  'Simultaneous multi-charge initiation','Wet &amp; watery conditions'],
  },
  # ---------------------------------------------------------------- non-electric detonators
  'neo-det-combidet': {
    'name': 'NEO DET COMBIDET', 'cat': 'non-electric',
    'tagline': 'Dual-delay non-electric detonator integrating an in-hole and a surface delay detonator in one unit.',
    'meta': 'NEO DET COMBIDET — shock-tube based dual-delay non-electric detonator from SBL Energy combining an '
            'in-hole delay detonator and a colour-coded surface connector in a single unit.',
    'intro': [
      'NEO DET COMBIDET is a shock-tube based, dual-delay non-electric detonator that integrates an in-hole delay '
      'detonator and a surface connector detonator into a single unit. The in-hole end carries a long-delay element '
      'and a high-strength base charge for initiating emulsion and cast boosters and other cap-sensitive explosives.',
      'The other end is a colour-coded surface connector housing a low-strength precision delay detonator. The enclosed '
      'connector accepts up to six shock tubes with secure retention, enabling reliable, low-noise surface sequencing, '
      'while colour-coded delays allow quick, error-free identification in the field.',
    ],
    'specs': [
      ('Surface Delays', '17 / 25 / 42', 'ms'),
      ('In-hole Delays', '250 / 450 / 500', 'ms'),
      ('Tube Capacity', 'up to 6', 'tubes'),
      ('Detonator Strength', 'No. 8', ''),
    ],
    'specs_note': 'Aluminium shell, 7.5&nbsp;mm, with a 600&nbsp;mg PETN base charge. Full length and delay tables are in the datasheet.',
    'use_cases': ['Surface blasting','Underground blasting','Quarrying','Construction blasting',
                  'Simplified in-hole + surface hook-up'],
  },
  'neo-det-dth': {
    'name': 'NEO DET DTH', 'cat': 'non-electric',
    'tagline': 'High-strength down-the-hole non-electric millisecond-delay detonator for in-hole initiation.',
    'meta': 'NEO DET DTH — high-strength, non-electric millisecond-delay down-the-hole detonator from SBL Energy '
            'for reliable in-hole initiation across surface, underground, quarry and construction blasting.',
    'intro': [
      'NEO DET DTH is a high-strength, non-electric millisecond-delay detonator designed for reliable in-hole '
      'initiation across surface, underground, quarry and construction blasting. It consists of an abrasion-resistant '
      'shock tube crimped to a precision delay detonator, with the free end sealed for moisture protection.',
      'The system offers multiple delay intervals for flexible timing design and is compatible with detonating-cord '
      'trunklines and standard surface connectors, with selected lengths offering an optional J-hook. It is suitable '
      'for priming cap-sensitive explosives and boosters in a wide range of blasting environments.',
    ],
    'specs': [
      ('Delay Intervals', '250 / 450 / 500', 'ms'),
      ('Tube Lengths', '3 &ndash; 50', 'm'),
      ('Shell Diameter', '7.5', 'mm'),
      ('Detonator Strength', 'No. 8', ''),
    ],
    'specs_note': 'Aluminium shell with a 600&nbsp;mg PETN base charge; optional J-hook. Full length table is in the datasheet.',
    'use_cases': ['In-hole initiation','Priming cap-sensitive explosives &amp; boosters','Surface mining',
                  'Underground operations','Quarrying','Construction blasting'],
  },
  'neo-det-lpsp': {
    'name': 'NEO DET LP/SP', 'cat': 'non-electric',
    'tagline': 'In-hole non-electric delay detonator in Long-Period (LP) and Short-Period (SP) delay series.',
    'meta': 'NEO DET LP/SP — high-strength, non-electric in-hole delay detonator from SBL Energy, available in '
            'Long-Period (LP) and Short-Period (SP) delay series for flexible blast timing design.',
    'intro': [
      'NEO DET LP/SP is a high-strength, non-electric millisecond-delay detonator for reliable in-hole initiation '
      'across surface, underground, quarry and construction blasting. It consists of an abrasion-resistant shock tube '
      'crimped to a precision delay detonator, with the free end sealed for moisture protection.',
      'It is offered in a Long-Period (LP) series for inter-row timing and a Short-Period (SP) series for close-interval '
      'control, giving a wide range of delay steps for flexible blast design. The system is compatible with '
      'detonating-cord trunklines and standard surface connectors, with an optional J-hook on selected lengths.',
    ],
    'specs': [
      ('LP Delays', 'up to 9000', 'ms'),
      ('SP Delays', '25 &ndash; 400', 'ms'),
      ('Delay Steps', '19 LP / 10 SP', ''),
      ('Detonator Strength', 'No. 8', ''),
    ],
    'specs_note': 'Aluminium shell, 7.5&nbsp;mm, with a 600&nbsp;mg PETN base charge. Full LP and SP delay sequences are in the datasheet.',
    'use_cases': ['In-hole initiation','Long &amp; short period delay sequencing','Priming cap-sensitive explosives',
                  'Surface mining','Underground operations','Quarrying'],
  },
  'neo-det-stld': {
    'name': 'NEO DET STLD', 'cat': 'non-electric',
    'tagline': 'Non-electric surface trunkline delay detonator for hole-to-hole and row-to-row sequencing.',
    'meta': 'NEO DET STLD — non-electric surface trunkline delay detonator from SBL Energy for controlling '
            'millisecond delays between blast holes or rows through reliable surface sequencing.',
    'intro': [
      'NEO DET STLD is a non-electric surface trunkline detonator that controls millisecond delays between blast holes '
      'or rows through reliable surface sequencing. A durable shock tube is attached to a colour-coded plastic connector '
      'housing a low-strength precision delay detonator.',
      'The connector block accepts up to six shock tubes with secure retention and flexible routing across the blast '
      'field, enabling accurate hole-to-hole or row-to-row timing. It is compatible with standard non-electric in-hole '
      'detonators, providing versatility in complex surface initiation designs.',
    ],
    'specs': [
      ('Surface Delays', '17 / 25 / 42 / 67', 'ms'),
      ('Tube Capacity', 'up to 6', 'tubes'),
      ('Tube Lengths', '2 &ndash; 6', 'm'),
      ('Detonator Strength', 'No. 8', ''),
    ],
    'specs_note': 'Aluminium shell, 7.5&nbsp;mm, with a 600&nbsp;mg PETN base charge. Full length and delay tables are in the datasheet.',
    'use_cases': ['Surface delay sequencing','Hole-to-hole timing','Row-to-row timing','Surface mining',
                  'Quarrying','Construction blasting'],
  },
  # ---------------------------------------------------------------- chemicals
  'petn': {
    'name': 'PETN', 'cat': 'petn',
    'tagline': 'High-performance secondary explosive (Pentaerythritol Tetranitrate) for detonators, cords and boosters.',
    'meta': 'PETN (Pentaerythritol Tetranitrate) from SBL Energy — a high-performance secondary explosive with very '
            'high detonation velocity and strong brisance for detonators, detonating cord, boosters and primers.',
    'intro': [
      'PETN (Pentaerythritol Tetranitrate) is a high-performance secondary explosive supplied as a white crystalline '
      'material with uniform particle characteristics. It is known for its very high detonation velocity and strong '
      'brisance, making it highly effective for initiation and detonation-transfer applications.',
      'Because of its sensitivity characteristics, PETN is not used as a bulk explosive but is widely employed in '
      'detonators, detonating cords, boosters and primer compositions where reliable, instantaneous energy transfer is '
      'critical. Manufactured under controlled conditions, it delivers consistent, predictable performance for '
      'commercial and defence applications.',
    ],
    'specs': [
      ('Bulk Density (Tapped)', '1.00 &plusmn; 0.1', 'g/ml'),
      ('Nitrogen Content', '17.5', '% min'),
      ('Melting Point', '139 &ndash; 142', '&deg;C'),
      ('Flow Rate', '160', 'g/min'),
    ],
    'specs_note': 'Full purity, acidity and sieve-analysis specifications are in the datasheet.',
    'use_cases': ['Detonating cord core','Base charge in detonators','Cast primers &amp; boosters',
                  'Composite explosives','Shaped charges'],
  },
  # ---------------------------------------------------------------- defense
  'tnt': {
    'name': 'TNT', 'cat': 'tnt',
    'tagline': 'High-purity, melt-pourable secondary high explosive for defence and cast-booster applications.',
    'meta': 'TNT (Trinitrotoluene) from SBL Energy — a high-purity, melt-pourable secondary high explosive with high '
            'chemical stability and low sensitivity, for cast boosters, defence compositions and melt-pour manufacturing.',
    'intro': [
      'Trinitrotoluene (TNT) is a secondary high explosive known for its high chemical stability, predictable '
      'detonation behaviour and low sensitivity to mechanical stimuli. It is widely used in defence and controlled '
      'industrial applications where consistent performance and safe handling are critical.',
      'The product is supplied in high-purity crystalline form as light-yellow flakes, free from moisture and '
      'mechanical impurities, making it well suited for melt&ndash;pour operations and uniform casting. Its balance of '
      'stability, castability and performance has established TNT as a reference explosive for demanding, regulated '
      'environments.',
    ],
    'specs': [
      ('Density', '1.654', 'g/cm&sup3;'),
      ('Detonation Velocity', '7000', 'm/s'),
      ('Solidification Temp', '&ge; 80.2', '&deg;C'),
      ('Molecular Weight', '227.13', 'g/mol'),
    ],
    'specs_note': 'VOD measured at 1.62&nbsp;g/cm&sup3;. Full chemical specification is in the datasheet.',
    'use_cases': ['Pentolite cast boosters','Military explosive compositions','Melt-pour manufacturing',
                  'Munitions','Defence &amp; mining formulations'],
  },
  # ---------------------------------------------------------------- cast booster
  'neo-primex': {
    'name': 'NEO PRIMEX', 'cat': 'cast-booster',
    'tagline': 'High-density PETN–TNT cast booster for reliable initiation of bulk explosives, ANFO and emulsions.',
    'meta': 'NEO PRIMEX — high-density PETN–TNT cast (Pentolite) booster from SBL Energy delivering high detonation '
            'pressure to initiate ANFO, watergels, emulsions and other blasting agents that a detonator cannot fire directly.',
    'intro': [
      'NEO PRIMEX is a high-density cast booster made from a PETN–TNT explosive composition, moulded into a durable '
      'cylindrical shell. It is engineered to deliver high detonation pressure and a strong shock front needed to '
      'initiate bulk explosives, ANFO, watergels, emulsions and other blasting agents that cannot be initiated directly '
      'by a detonator.',
      'The booster contains two longitudinal tunnels to accommodate a detonator or detonating cord — one straight, the '
      'other with a stepped detonator-retention feature for secure placement. Its high density and high velocity of '
      'detonation maximise initiation performance, with excellent resistance to water and oil.',
    ],
    'specs': [
      ('Density', '1.65', 'g/cm&sup3;'),
      ('Velocity of Detonation', '7000', 'm/s'),
      ('Water Resistance', 'Excellent', ''),
      ('Available Sizes', '100&ndash;400', 'g'),
    ],
    'specs_note': 'Available in 100, 150, 250 and 400&nbsp;g. Full dimensions, hole sizes and packaging are in the datasheet.',
    'use_cases': ['Initiating ANFO','Initiating emulsions &amp; watergels','Priming bulk explosives',
                  'Surface mining','Underground operations'],
  },
}

def build_rich(slug, d):
    cat = d['cat']
    back = CAT_PAGE[cat]
    grp_page = GROUP_PAGE[cat]
    grp_name = GROUP_NAME[cat]
    catname = CAT_NAME[cat]
    name = d['name']
    title = name + ' — SBL Energy Limited'
    own = 'images/products/%s.png' % slug
    img = d.get('img', own if os.path.exists(own) else IMG_BY_CAT[cat])
    pdf = d.get('pdf', 'assets/tds/' + slug + '-tds.pdf')
    cl = class_label(slug, cat)
    cls_html = ('\n        <div class="class-pill">' + cl + '</div>') if cl else ''

    specs = '\n'.join(
        '''            <div class="key-spec">
              <span class="ks-val">''' + val + ''' <span class="ks-unit">''' + unit + '''</span></span>
              <span class="ks-label">''' + label + '''</span>
            </div>''' for (label, val, unit) in d['specs'])

    use_cases = '\n'.join(
        '              <li>' + uc + '</li>' for uc in d['use_cases'])

    intro = '\n'.join(
        '        <p class="prod-para">' + p + '</p>' for p in d['intro'])

    html = head(title, d['meta']) + '''

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
    <p class="prod-hero-sub">''' + d['tagline'] + '''</p>
  </div>
</section>

<section class="section prod-overview">
  <div class="container">
    <div class="prod-overview-grid" style="grid-template-columns:1fr 1.15fr;gap:56px;align-items:start">
      <div class="prod-img-wrap">
        <div class="prod-img-frame">
          <img src="''' + img + '''" alt="''' + name + '''" />
        </div>
        <div class="prod-img-badge"><span class="badge-tag">SBL ENERGY</span><span class="badge-name">''' + name + '''</span></div>
      </div>
      <div class="prod-text">
        <div class="section-tag"><span class="tag-line"></span> ''' + catname.upper() + '''</div>
        <h2 class="section-title">''' + name + '''</h2>''' + cls_html + '''
''' + intro + '''
        <div class="key-spec-grid">
''' + specs + '''
        </div>
        <p class="key-spec-note">''' + d['specs_note'] + '''</p>
        <div class="hero-actions" style="margin-top:28px">
          <a href="''' + pdf + '''" class="btn btn-primary" download>Download TDS <span class="arrow">↓</span></a>
          <a href="contact.html" class="btn btn-ghost">Request a Quote <span class="arrow">→</span></a>
        </div>
        <a href="''' + back + '''" class="back-link" onclick="if(history.length>1){history.back();return false;}">← Back to ''' + catname + '''</a>
      </div>
    </div>

    <div class="use-case-block">
      <div class="section-tag"><span class="tag-line"></span> RECOMMENDED APPLICATIONS</div>
      <h2 class="section-title">Where it is used</h2>
      <ul class="use-case-list">
''' + use_cases + '''
      </ul>
      <p class="use-case-foot">For full technical details — packaging, safety &amp; storage, transport classification and recommendations for use — please <a href="''' + pdf + '''" download>download the Technical Datasheet</a>.</p>
    </div>
  </div>
</section>

''' + cta('Need a quote for ' + name + '?', 'Our technical team will help you choose the right specification for your site.') + '''

''' + FOOTER + '''

<script src="js/main.js"></script>
</body>
</html>'''
    html = html.replace('NEO ', 'NEO™ ')  # trademark after the NEO brand
    with open(slug + '.html', 'w') as f:
        f.write(html)
    print('wrote (rich)', slug + '.html')

# ---------------------------------------------------------------- run builds
build_category('initiating-systems.html',
    'Initiating Systems — SBL Energy Limited',
    'Initiating Systems',
    'Detonators, detonating fuse and cast boosters — the complete initiation range for surface and underground blasting.',
    'images/hero/blast-mountain.jpg',
    'OUR PRODUCTS', 'initiating', TYPES_INIT, PRODUCTS_INIT,
    'Need help choosing an initiation system?',
    'Our technical team will help you select the right detonator, fuse or booster for your site.',
    'NEO E-DET, NEO DET COMBIDET/DTH/LP-SP/STLD, NEO CDD, NEO BOOST and NEO CORD — SBL Energy initiating systems: electronic and non-electric detonators, detonating fuse and cast boosters.')

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
    if p[0] in RICH:        # rich product pages are built separately below
        continue
    build_stub(*p)

for slug, d in RICH.items():
    build_rich(slug, d)

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

# Old externally-hosted brochure URL → self-hosted local copy.
OLD_BROCHURE = 'https://www.sblenergy.com/_files/ugd/06db74_7aba56dcc5c9456fbe8bcffc8c9c3cb6.pdf'
NEW_BROCHURE = 'assets/brochure/sbl-energy-brochure.pdf'

swapped = 0
for fn in glob.glob('*.html'):
    with open(fn) as f:
        txt = f.read()
    new = txt
    for old in (OLD_BLOCK, OLD_MEGA, OLD_MEGA2, OLD_MEGA3, OLD_MEGA4):
        if old in new:
            new = new.replace(old, MEGA)
    if OLD_BROCHURE in new:
        new = new.replace(OLD_BROCHURE, NEW_BROCHURE)
    if new != txt:
        with open(fn,'w') as f:
            f.write(new)
        swapped += 1
print('existing pages updated:', swapped)
