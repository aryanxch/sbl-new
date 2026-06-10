# SBL Energy Website — Project Context

## Project Location
`/Users/aryan/Desktop/Claude/sbl-energy-website`

## What This Project Is
A static website for **SBL Energy Limited** — a manufacturer & supplier of Industrial & Mining Explosives based in Nagpur, Maharashtra, India (incorporated 2002).

## Tech Stack
- **Pure static HTML/CSS/JS** — no React, no Vue, no Node, no framework
- **CSS:** Vanilla custom CSS (`css/styles.css`)
- **JS:** Vanilla JavaScript (`js/main.js`)
- **Fonts:** Google Fonts — `Inter` + `Space Grotesk`
- **Build tool:** Python script (`build/generate.py`) — generates all `.html` pages from a shared template. Run locally, not on the server.

## File Structure
```
sbl-energy-website/
├── index.html                  # Homepage
├── about.html
├── contact.html
├── career.html
├── services.html
├── people-clients.html
├── bulk-explosives.html
├── cast-booster.html
├── copper-delay-detonator.html
├── detonating-fuse.html
├── electric-detonator.html
├── electronic-detonator.html
├── emulsion-explosives.html
├── low-column-charge.html
├── non-electric-detonator.html
├── ordinary-detonator.html
├── seismic-explosives.html
├── slurry-explosives.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── images/                     # All site images
├── assets/
├── build/
│   ├── generate.py             # Python build script (generates HTML from template)
│   ├── generate_pages.py
│   └── specs.py
├── scraped-html/               # Original scraped HTML references
└── .claude/
    └── launch.json             # Dev server config (python3 -m http.server, port 8000)
```

## How to Run Locally
Open Terminal and run:
```bash
cd /Users/aryan/Desktop/Claude/sbl-energy-website
python3 -m http.server 8000
```
Then open **http://localhost:8000** in your browser.
Press `Ctrl + C` to stop the server.

## How to Regenerate HTML Pages
If you edit the Python build template and want to regenerate all HTML:
```bash
cd /Users/aryan/Desktop/Claude/sbl-energy-website/build
python3 generate.py
```

## Hosting — GitHub Pages
This site is **fully compatible with GitHub Pages** (free static hosting).
- Steps: Push repo to GitHub → Settings → Pages → Source: `main` branch, `/ (root)` → Save
- Result: hosted at `https://<username>.github.io/sbl-energy-website`
- The `.py` files do NOT cause issues — GitHub Pages ignores them (can't execute Python)

## Current Status (as of June 8, 2026)
- All HTML pages generated and present
- Site runs correctly on localhost
- Not yet deployed to GitHub Pages
- No `package.json` / Node dependencies — pure static site
