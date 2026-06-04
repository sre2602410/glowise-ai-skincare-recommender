import streamlit as st
import sys
import os
import time

_APP_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.abspath(os.path.join(_APP_DIR, ".."))
for _path in (_ROOT_DIR, _APP_DIR):
    if _path not in sys.path:
        sys.path.insert(0, _path)

from main import get_routine, get_product_catalog
from src.utils import get_skin_types, get_concerns
from src.image_processor import analyze_skin_image
from themes import get_theme_css
from ui_visuals import render_hero_visual, render_banner_visual

st.set_page_config(
    page_title="Glowise — AI Skincare",
    page_icon="✨",
    layout="wide",
)

if "theme" not in st.session_state:
    st.session_state.theme = "light"

st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

_is_dark = st.session_state.theme == "dark"
_toggle_dark = st.toggle(
    "Dark mode",
    value=_is_dark,
    key="glowise_theme_toggle",
    label_visibility="collapsed",
)
if _toggle_dark != _is_dark:
    st.session_state.theme = "dark" if _toggle_dark else "light"
    st.rerun()


@st.cache_data
def _catalog_size():
    df = get_product_catalog()
    return len(df) if df is not None else 0


PRODUCT_COUNT = _catalog_size()


def draw_logo(size="large"):
    if size == "large":
        st.markdown('<p class="logo-text">glowise</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="logo-sub">clinical-grade skincare · powered by AI</p>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<p class="logo-text" style="font-size:2rem;">glowise</p>',
            unsafe_allow_html=True,
        )


def draw_hero():
    st.markdown(
        """
        <span class="hero-eyebrow">✦ skin intelligence 2.0</span>
        <p class="hero-headline">your routine, but actually personalized.</p>
        <p class="hero-body">
            We scan your profile, filter for safety, and match you with
            <strong>1,500+ real formulations</strong> — no generic 10-step nonsense.
            just what your skin actually needs.
        </p>
        """,
        unsafe_allow_html=True,
    )


def draw_stats():
    st.markdown(
        f"""
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap; margin:1.25rem 0 0.5rem 0;">
            <div class="stat-pill">
                <span class="stat-value">{PRODUCT_COUNT:,}</span>
                <span class="stat-label">products indexed</span>
            </div>
            <div class="stat-pill">
                <span class="stat-value">AM·PM</span>
                <span class="stat-label">ritual sync</span>
            </div>
            <div class="stat-pill">
                <span class="stat-value">AI</span>
                <span class="stat-label">skin scan</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Sidebar ──
with st.sidebar:
    draw_logo(size="small")
    st.caption("drop a selfie · pick your vibe · get your stack")
    st.markdown("---")

    st.markdown('<p class="section-label">scan</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload skin photo",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
        help="JPG or PNG · good lighting works best",
    )

    scan_results = None
    if uploaded_file is not None:
        with st.spinner("running skin analysis…"):
            image_bytes = uploaded_file.read()
            scan_results = analyze_skin_image(image_bytes)
            if scan_results:
                st.success(f"done · {scan_results['engine']}")
                cols = st.columns(3)
                with cols[0]:
                    st.metric(
                        "redness",
                        f"{int(max(scan_results['scores']['acne'], scan_results['scores']['sensitivity']) * 100)}%",
                    )
                with cols[1]:
                    st.metric(
                        "pigment",
                        f"{int(scan_results['scores']['brightening'] * 100)}%",
                    )
                with cols[2]:
                    st.metric(
                        "texture",
                        f"{int(scan_results['scores']['texture'] * 100)}%",
                    )
                if scan_results["detected_concerns"]:
                    with st.expander("what we detected"):
                        for c in scan_results["detected_concerns"]:
                            st.markdown(f"**{c.capitalize()}** — high confidence")
                        st.caption("CNN feature activations · not medical advice")

    st.markdown("---")
    st.markdown('<p class="section-label">profile</p>', unsafe_allow_html=True)
    skin_type = st.selectbox("skin type", get_skin_types())

    default_concerns = []
    if scan_results:
        default_concerns = [
            c.capitalize()
            for c in scan_results["detected_concerns"]
            if c.capitalize() in get_concerns()
        ]

    concern = st.multiselect("main concerns", get_concerns(), default=default_concerns)
    is_sensitive = st.checkbox(
        "sensitive skin",
        value=(
            "sensitivity" in scan_results["detected_concerns"]
            if scan_results
            else False
        ),
    )

    st.markdown('<p class="section-label">safety</p>', unsafe_allow_html=True)
    avoided = st.text_input(
        "ingredients to avoid",
        placeholder="alcohol, fragrance, …",
        label_visibility="collapsed",
    )

    predict_btn = st.button("build my routine →", use_container_width=True)

# ── Main ──
col_header1, col_header2 = st.columns([2.2, 1])
with col_header1:
    draw_logo(size="large")
    draw_hero()
    draw_stats()
with col_header2:
    st.markdown(
        f'<div class="hero-visual-wrap">{render_hero_visual(st.session_state.theme)}</div>',
        unsafe_allow_html=True,
    )

if predict_btn:
    if not concern:
        st.error("pick at least one concern — we need something to work with.")
    else:
        user_profile = {
            "skin_type": skin_type.lower(),
            "concern": ", ".join(concern).lower(),
            "is_sensitive": is_sensitive,
        }
        avoid_list = [a.strip() for a in avoided.split(",") if a.strip()]

        with st.status("curating your stack…", expanded=True) as status:
            st.markdown(
                '<div class="step-box"><span>01</span> safety & biocompatibility check</div>',
                unsafe_allow_html=True,
            )
            time.sleep(0.5)
            st.markdown(
                '<div class="step-box"><span>02</span> syncing AM / PM ritual</div>',
                unsafe_allow_html=True,
            )
            routine = get_routine(user_profile, avoided_ingredients=avoid_list)
            time.sleep(0.5)
            st.markdown(
                '<div class="step-box"><span>03</span> locking in your picks</div>',
                unsafe_allow_html=True,
            )
            status.update(label="you're all set ✦", state="complete", expanded=False)

        if isinstance(routine, str):
            st.warning(routine)
        else:
            st.markdown("### your routine")
            all_products = list(routine["AM"].values()) + list(routine["PM"].values())
            top_concerns = set()
            for p in all_products:
                if "concern" in p:
                    top_concerns.update(
                        [c.strip().capitalize() for c in p["concern"].split(",")]
                    )
            st.info(
                f"**focus:** {', '.join(list(top_concerns)[:3])} · "
                f"optimized for **{skin_type.lower()}** skin"
            )

            tab_am, tab_pm = st.tabs(["☀️ AM stack", "🌙 PM stack"])

            for tab, period in [(tab_am, "AM"), (tab_pm, "PM")]:
                with tab:
                    for cat, rec in routine[period].items():
                        ing_list = rec["ingredients"].split(",")
                        ingredients_html = "".join(
                            f'<span class="ingredient-tag">{i.strip()}</span>'
                            for i in ing_list[:8]
                        )
                        st.markdown(
                            f"""
                            <div class="recommendation-card">
                                <div class="brand-title">{rec['brand']} · {cat}</div>
                                <div style="display:flex; align-items:center; flex-wrap:wrap;">
                                    <div class="product-title">{rec['product_name']}</div>
                                    <span class="rating-badge">★ {rec.get('rating', 4.5)}</span>
                                </div>
                                <div style="margin:1.1rem 0;">{ingredients_html}</div>
                                <div class="explanation-box">{rec['explanation']}</div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

else:
    st.markdown("---")
    st.markdown('<p class="section-label">how it works</p>', unsafe_allow_html=True)
    st.markdown("### the glowise method")
    L_col1, L_col2, L_col3 = st.columns(3)

    cards = [
        ("🛡️", "biocompatibility", "cross-checks every formula against your sensitivity + avoid list."),
        ("🧠", "smart matching", "TF-IDF + cosine similarity on 1.5k+ real product profiles."),
        ("💬", "transparent picks", "every recommendation comes with a clear why — no black box."),
    ]
    for col, (icon, title, desc) in zip([L_col1, L_col2, L_col3], cards):
        with col:
            st.markdown(
                f'<div class="hero-card"><div class="card-icon">{icon}</div>'
                f"<h4>{title}</h4><p>{desc}</p></div>",
                unsafe_allow_html=True,
            )

    st.markdown(render_banner_visual(st.session_state.theme), unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p class='footer-text'>glowise · 2026 · not medical advice · just really good recommendations</p>",
    unsafe_allow_html=True,
)
