"""
bettervibe — OG Image + Favicon Generator
Requires: Pillow (pip install Pillow)
Output:   og-image.png, twitter-card.png, favicon.svg,
          favicon-32x32.png, favicon-16x16.png,
          apple-touch-icon.png, favicon.ico, site.webmanifest
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUT   = '.'  # change to your output directory if needed

# ── Colours ──────────────────────────────────────────────
BG        = (13, 15, 17)
AMBER     = (218, 119, 86)
AMBER_DIM = (196, 98, 62)
TEXT      = (232, 228, 223)
TEXT_SEC  = (155, 150, 144)
TEXT_MUT  = (107, 102, 96)
GREEN     = (126, 198, 153)

BOLD    = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
REGULAR = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'


def amber_glow(img, cx, cy, max_r, max_alpha=30, step=8):
    """Paint a radial amber glow onto img at (cx, cy)."""
    for r in range(max_r, 0, -step):
        alpha = int(max_alpha * (1 - r / max_r))
        glow = Image.new('RGBA', img.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*AMBER, alpha))
        base = Image.new('RGBA', img.size, (0, 0, 0, 0))
        merged = Image.alpha_composite(base, glow)
        img.paste(merged.convert('RGB'), mask=merged.split()[3])


def scanlines(d, w, h):
    for y in range(0, h, 4):
        d.line([(0, y), (w, y)], fill=(0, 0, 0, 18), width=1)


# ═══════════════════════════════════════════════════════════
# OG IMAGE  1200 × 630
# ═══════════════════════════════════════════════════════════
W, H = 1200, 630
og = Image.new('RGB', (W, H), BG)
amber_glow(og, W - 60, -40, 320, max_alpha=30)
d = ImageDraw.Draw(og)
scanlines(d, W, H)
d.rectangle([0, 0, W - 1, H - 1], outline=(255, 255, 255, 20), width=1)

f_sm  = ImageFont.truetype(REGULAR, 18)
f_xl  = ImageFont.truetype(BOLD, 96)
f_tag = ImageFont.truetype(REGULAR, 30)
f_desc = ImageFont.truetype(REGULAR, 20)
f_meta = ImageFont.truetype(BOLD, 18)
f_meta_val = ImageFont.truetype(REGULAR, 18)
f_url  = ImageFont.truetype(BOLD, 18)

# Terminal prompt
d.text((64, 64), '~/workshop', font=f_sm, fill=GREEN)
d.text((64 + d.textlength('~/workshop', font=f_sm), 64), ' $ cat event.md', font=f_sm, fill=TEXT_MUT)
d.line([(64, 100), (280, 100)], fill=AMBER_DIM, width=1)

# Wordmark
bv_w = d.textlength('bettervibe', font=f_xl)
d.text((64, 130), 'bettervibe', font=f_xl, fill=TEXT)
d.text((64 + bv_w, 130), '.', font=f_xl, fill=AMBER)

# Tagline + descriptor
d.text((64, 250), 'Avoiding the vibe coding hangover.', font=f_tag, fill=AMBER)
d.text((64, 310), 'Write production-ready code with AI.', font=f_desc, fill=TEXT_SEC)

# Divider
d.line([(64, 370), (W - 64, 370)], fill=(255, 255, 255, 20), width=1)

# Meta row
items = [('DATE', 'May 15, 2026'), ('TIME', '1:00 – 6:00 PM'), ('LOCATION', 'WERK1, Munich')]
x = 64
for label, val in items:
    d.text((x, 400), label, font=f_meta, fill=TEXT_MUT)
    d.text((x, 428), val,   font=f_meta_val, fill=AMBER)
    x += 300

# URL
url_w = d.textlength('bettervibe.org', font=f_url)
d.text((W - 64 - url_w, H - 56), 'bettervibe.org', font=f_url, fill=TEXT_MUT)

og.save(f'{OUT}/og-image.png', 'PNG', optimize=True)
print('og-image.png')

# ── Twitter/X card (crop to 600px tall) ──────────────────
og.crop((0, 0, W, 600)).save(f'{OUT}/twitter-card.png', 'PNG', optimize=True)
print('twitter-card.png')


# ═══════════════════════════════════════════════════════════
# FAVICON SVG
# ═══════════════════════════════════════════════════════════
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" fill="#0D0F11" rx="4"/>
  <text x="16" y="22" font-family="monospace" font-size="18" font-weight="bold"
        text-anchor="middle" fill="#E8E4DF">b<tspan fill="#DA7756">.</tspan></text>
</svg>'''
with open(f'{OUT}/favicon.svg', 'w') as fh:
    fh.write(favicon_svg)
print('favicon.svg')


# ═══════════════════════════════════════════════════════════
# FAVICON PNGs
# ═══════════════════════════════════════════════════════════
def make_favicon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(img)
    d2.rounded_rectangle([0, 0, size - 1, size - 1], radius=size // 8, fill=BG)
    if size >= 32:
        f_fav = ImageFont.truetype(BOLD, int(size * 0.55))
        b_w   = d2.textlength('b', font=f_fav)
        dot_w = d2.textlength('.', font=f_fav)
        x_s   = (size - b_w - dot_w) / 2
        y_s   = (size - int(size * 0.55)) / 2 - size * 0.04
        d2.text((x_s, y_s),       'b', font=f_fav, fill=TEXT)
        d2.text((x_s + b_w, y_s), '.', font=f_fav, fill=AMBER)
    else:
        f_fav = ImageFont.truetype(BOLD, 12)
        d2.text((4, 2), 'b.', font=f_fav, fill=AMBER)
    return img

make_favicon(32).save(f'{OUT}/favicon-32x32.png', 'PNG')
print('favicon-32x32.png')

make_favicon(16).save(f'{OUT}/favicon-16x16.png', 'PNG')
print('favicon-16x16.png')

make_favicon(180).save(f'{OUT}/apple-touch-icon.png', 'PNG')
print('apple-touch-icon.png')

make_favicon(32).save(f'{OUT}/favicon.ico', format='ICO', sizes=[(32, 32), (16, 16)])
print('favicon.ico')


# ═══════════════════════════════════════════════════════════
# WEBMANIFEST
# ═══════════════════════════════════════════════════════════
manifest = '''{
  "name": "bettervibe",
  "short_name": "bettervibe",
  "description": "Write production-ready code with AI. Avoiding the vibe coding hangover.",
  "icons": [
    { "src": "/favicon-32x32.png", "sizes": "32x32", "type": "image/png" },
    { "src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png" }
  ],
  "theme_color": "#0D0F11",
  "background_color": "#0D0F11",
  "display": "standalone"
}'''
with open(f'{OUT}/site.webmanifest', 'w') as fh:
    fh.write(manifest)
print('site.webmanifest')

print('\nAll OG + favicon assets generated.')
