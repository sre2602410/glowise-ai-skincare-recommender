"""Styled image blocks matching the Glowise mockup aesthetic."""
import base64
import os

_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

HERO_IMAGE = os.path.join(_ASSETS_DIR, "hero-skincare.png")
BANNER_IMAGE = os.path.join(_ASSETS_DIR, "banner-skincare.png")

# Fallbacks if local assets are missing
HERO_FALLBACK = (
    "https://images.unsplash.com/photo-1617897903246-923366493997"
    "?auto=format&fit=crop&w=600&q=80"
)
BANNER_FALLBACK = (
    "https://images.unsplash.com/photo-1570172619644-dfd933f4571a"
    "?auto=format&fit=crop&w=1400&q=80"
)


def _image_to_data_uri(path: str):
    if not os.path.isfile(path):
        return None
    ext = os.path.splitext(path)[1].lower().lstrip(".")
    mime = "image/png" if ext == "png" else f"image/{ext or 'jpeg'}"
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def _img_src(local_path: str, fallback_url: str) -> str:
    data_uri = _image_to_data_uri(local_path)
    return data_uri if data_uri else fallback_url


def render_hero_visual(theme: str = "light") -> str:
    """HTML hero card — top-right product visual like the mockup."""
    src = _img_src(HERO_IMAGE, HERO_FALLBACK)
    chip = "your glow era" if theme == "light" else "night mode activated"
    return f"""
    <div class="visual-frame hero-visual">
        <div class="visual-glow"></div>
        <img src="{src}" alt="Glowise skincare essentials" loading="lazy" />
        <span class="visual-chip">✦ {chip}</span>
        <span class="visual-tag">AI-matched</span>
    </div>
    """


def render_banner_visual(theme: str = "light") -> str:
    """Wide banner for the methodology section."""
    src = _img_src(BANNER_IMAGE, BANNER_FALLBACK)
    label = "the routine, visualized" if theme == "light" else "skin stack · PM ready"
    return f"""
    <div class="visual-frame banner-visual">
        <div class="visual-glow"></div>
        <img src="{src}" alt="Skincare routine flat lay" loading="lazy" />
        <div class="banner-overlay">
            <span class="banner-label">✦ {label}</span>
            <span class="banner-sub">clean · clinical · actually personalized</span>
        </div>
    </div>
    """
