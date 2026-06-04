"""CSS theme definitions for Glowise Streamlit UI — pro + Gen Z aesthetic."""


def get_theme_css(theme: str) -> str:
    if theme == "dark":
        tokens = {
            "bg": "#06080f",
            "bg_soft": "#0c1019",
            "card": "rgba(17, 24, 39, 0.72)",
            "card_solid": "#111827",
            "text": "#F1F5F9",
            "text_muted": "#94A3B8",
            "heading": "#FFFFFF",
            "accent": "#6366F1",
            "accent_2": "#38BDF8",
            "accent_soft": "#818CF8",
            "accent_glow": "rgba(99, 102, 241, 0.45)",
            "gradient": "linear-gradient(135deg, #6366F1 0%, #38BDF8 50%, #22D3EE 100%)",
            "mesh_1": "rgba(99, 102, 241, 0.18)",
            "mesh_2": "rgba(56, 189, 248, 0.12)",
            "border": "rgba(148, 163, 184, 0.15)",
            "tag_bg": "rgba(99, 102, 241, 0.2)",
            "tag_text": "#C7D2FE",
            "btn_bg": "linear-gradient(135deg, #4F46E5 0%, #2563EB 100%)",
            "btn_text": "#FFFFFF",
            "shadow": "rgba(0, 0, 0, 0.35)",
            "sidebar": "rgba(8, 12, 22, 0.92)",
        }
    else:
        tokens = {
            "bg": "#FDF8FA",
            "bg_soft": "#FFF5F9",
            "card": "rgba(255, 255, 255, 0.78)",
            "card_solid": "#FFFFFF",
            "text": "#3F1D2E",
            "text_muted": "#9D6B8A",
            "heading": "#2D0A1E",
            "accent": "#E11D74",
            "accent_2": "#F472B6",
            "accent_soft": "#F9A8D4",
            "accent_glow": "rgba(225, 29, 116, 0.28)",
            "gradient": "linear-gradient(135deg, #E11D74 0%, #F472B6 45%, #FB7185 100%)",
            "mesh_1": "rgba(244, 114, 182, 0.22)",
            "mesh_2": "rgba(251, 113, 133, 0.14)",
            "border": "rgba(244, 114, 182, 0.28)",
            "tag_bg": "rgba(252, 231, 243, 0.9)",
            "tag_text": "#9D174D",
            "btn_bg": "linear-gradient(135deg, #DB2777 0%, #E11D74 100%)",
            "btn_text": "#FFFFFF",
            "shadow": "rgba(225, 29, 116, 0.12)",
            "sidebar": "rgba(255, 250, 252, 0.94)",
        }

    return f"""
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap" rel="stylesheet">
<style>
    :root {{
        --bg: {tokens['bg']};
        --bg-soft: {tokens['bg_soft']};
        --card: {tokens['card']};
        --card-solid: {tokens['card_solid']};
        --text: {tokens['text']};
        --text-muted: {tokens['text_muted']};
        --heading: {tokens['heading']};
        --accent: {tokens['accent']};
        --accent-2: {tokens['accent_2']};
        --accent-soft: {tokens['accent_soft']};
        --accent-glow: {tokens['accent_glow']};
        --gradient: {tokens['gradient']};
        --mesh-1: {tokens['mesh_1']};
        --mesh-2: {tokens['mesh_2']};
        --border: {tokens['border']};
        --tag-bg: {tokens['tag_bg']};
        --tag-text: {tokens['tag_text']};
        --btn-bg: {tokens['btn_bg']};
        --btn-text: {tokens['btn_text']};
        --shadow: {tokens['shadow']};
        --sidebar: {tokens['sidebar']};
        --radius: 20px;
        --radius-sm: 12px;
        --radius-pill: 999px;
    }}

    html, body, [class*="css"] {{
        font-family: 'DM Sans', system-ui, sans-serif;
        color: var(--text);
    }}

    .stApp {{
        background: var(--bg);
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background:
            radial-gradient(ellipse 55% 45% at 8% 12%, var(--mesh-1) 0%, transparent 55%),
            radial-gradient(ellipse 50% 40% at 92% 8%, var(--mesh-2) 0%, transparent 50%),
            radial-gradient(ellipse 40% 35% at 70% 88%, var(--mesh-1) 0%, transparent 45%),
            linear-gradient(180deg, var(--bg) 0%, var(--bg-soft) 100%);
        pointer-events: none;
        z-index: 0;
    }}

    [data-testid="stAppViewContainer"] {{
        position: relative;
        z-index: 1;
    }}

    h1, h2, h3, h4,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.03em;
        color: var(--heading) !important;
    }}

    /* ── Brand ── */
    .logo-text {{
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        font-size: clamp(2.8rem, 6vw, 4.2rem);
        background: var(--gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        letter-spacing: -0.04em;
        line-height: 1.05;
    }}

    .logo-sub {{
        font-size: 0.8rem;
        color: var(--text-muted);
        margin: 0.35rem 0 0 0;
        font-weight: 500;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }}

    .hero-eyebrow {{
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.35rem 0.85rem;
        border-radius: var(--radius-pill);
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        background: var(--tag-bg);
        color: var(--accent);
        border: 1px solid var(--border);
        margin-bottom: 1rem;
    }}

    .hero-headline {{
        font-family: 'Outfit', sans-serif;
        font-size: clamp(1.5rem, 3vw, 2rem);
        font-weight: 700;
        color: var(--heading);
        line-height: 1.2;
        margin: 0 0 0.75rem 0;
        letter-spacing: -0.03em;
    }}

    .hero-body {{
        font-size: 1.02rem;
        line-height: 1.65;
        color: var(--text-muted);
        margin: 0;
        max-width: 36rem;
    }}

    .hero-body strong {{
        color: var(--heading);
        font-weight: 600;
    }}

    .stat-pill {{
        display: inline-flex;
        flex-direction: column;
        padding: 0.85rem 1.1rem;
        border-radius: var(--radius-sm);
        background: var(--card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        min-width: 7rem;
    }}

    .stat-pill .stat-value {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.35rem;
        font-weight: 800;
        background: var(--gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}

    .stat-pill .stat-label {{
        font-size: 0.68rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--text-muted);
        margin-top: 0.15rem;
    }}

    .section-label {{
        font-family: 'Outfit', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: 0.35rem;
    }}

    .sidebar-panel {{
        padding: 1rem;
        border-radius: var(--radius-sm);
        background: var(--card);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border);
        margin-bottom: 0.85rem;
    }}

    /* ── Cards ── */
    .recommendation-card {{
        padding: 1.75rem 2rem;
        border-radius: var(--radius);
        background: var(--card);
        backdrop-filter: blur(14px);
        border: 1px solid var(--border);
        margin-bottom: 1.25rem;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        box-shadow: 0 8px 32px var(--shadow);
    }}

    .recommendation-card:hover {{
        transform: translateY(-3px);
        border-color: var(--accent-soft);
        box-shadow: 0 20px 48px var(--shadow);
    }}

    .product-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: var(--heading);
        margin-bottom: 0.35rem;
        letter-spacing: -0.02em;
    }}

    .brand-title {{
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: 0.85rem;
    }}

    .ingredient-tag {{
        display: inline-block;
        background: var(--tag-bg);
        color: var(--tag-text);
        padding: 0.3rem 0.75rem;
        border-radius: var(--radius-pill);
        font-size: 0.68rem;
        font-weight: 600;
        margin: 0 0.35rem 0.35rem 0;
        border: 1px solid var(--border);
    }}

    .explanation-box {{
        background: var(--bg-soft);
        padding: 1.15rem 1.25rem;
        border-radius: var(--radius-sm);
        border-left: 3px solid var(--accent);
        margin-top: 1.25rem;
        color: var(--text-muted);
        line-height: 1.65;
        font-size: 0.92rem;
    }}

    .rating-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        padding: 0.25rem 0.65rem;
        border-radius: var(--radius-pill);
        background: var(--tag-bg);
        color: var(--accent);
        font-weight: 700;
        font-size: 0.75rem;
        margin-left: 10px;
        border: 1px solid var(--border);
    }}

    .step-box {{
        padding: 0.9rem 1.15rem;
        background: var(--card);
        backdrop-filter: blur(8px);
        border: 1px solid var(--border);
        border-radius: var(--radius-sm);
        margin-bottom: 0.6rem;
        color: var(--text);
        font-size: 0.8rem;
        font-weight: 500;
        letter-spacing: 0.02em;
    }}

    .step-box span {{
        font-weight: 700;
        color: var(--accent);
        margin-right: 0.35rem;
    }}

    .hero-card {{
        padding: 1.35rem 1.5rem;
        border-radius: var(--radius);
        background: var(--card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        box-shadow: 0 8px 28px var(--shadow);
        height: 100%;
        transition: transform 0.2s ease;
    }}

    .hero-card:hover {{
        transform: translateY(-2px);
    }}

    .hero-card .card-icon {{
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }}

    .hero-card h4 {{
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        color: var(--heading) !important;
        margin: 0 0 0.4rem 0 !important;
    }}

    .hero-card p {{
        color: var(--text-muted) !important;
        font-size: 0.88rem !important;
        line-height: 1.55 !important;
        margin: 0 !important;
    }}

    .footer-text {{
        text-align: center;
        color: var(--text-muted);
        font-size: 0.82rem;
        letter-spacing: 0.02em;
    }}

    .footer-text a {{
        color: var(--accent);
        text-decoration: none;
    }}

    /* ── Streamlit widgets ── */
    .stButton>button {{
        background: var(--btn-bg) !important;
        color: var(--btn-text) !important;
        border: none !important;
        border-radius: var(--radius-pill) !important;
        padding: 0.8rem 1.75rem !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.03em !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        box-shadow: 0 8px 28px var(--shadow) !important;
    }}

    .stButton>button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 14px 36px var(--accent-glow) !important;
    }}

    [data-testid="stSidebar"] {{
        background: var(--sidebar) !important;
        backdrop-filter: blur(16px);
        border-right: 1px solid var(--border);
    }}

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }}

    [data-testid="stMetricValue"] {{
        font-family: 'Outfit', sans-serif !important;
        font-weight: 800 !important;
        background: var(--gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    [data-testid="stMetricLabel"] {{
        color: var(--text-muted) !important;
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }}

    .stTabs [data-baseweb="tab"] {{
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        color: var(--text-muted);
        border-radius: var(--radius-pill);
    }}

    .stTabs [aria-selected="true"] {{
        color: var(--accent) !important;
        border-color: var(--accent) !important;
        background: var(--tag-bg) !important;
    }}

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {{
        border-color: var(--border) !important;
        background-color: var(--card-solid) !important;
        border-radius: var(--radius-sm) !important;
    }}

    /* ── Floating theme toggle ── */
    .st-key-glowise_theme_toggle {{
        position: fixed !important;
        top: 0.85rem !important;
        right: 1rem !important;
        z-index: 999999 !important;
        padding: 0.35rem 0.55rem 0.35rem 0.45rem !important;
        background: var(--card) !important;
        backdrop-filter: blur(14px) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-pill) !important;
        box-shadow: 0 8px 28px var(--shadow) !important;
    }}

    .st-key-glowise_theme_toggle label,
    .st-key-glowise_theme_toggle [data-testid="stWidgetLabel"] {{
        display: none !important;
    }}

    .st-key-glowise_theme_toggle [role="switch"] {{
        width: 2.75rem !important;
        height: 1.5rem !important;
        min-width: 2.75rem !important;
        border-radius: var(--radius-pill) !important;
        background: var(--border) !important;
        border: none !important;
    }}

    .st-key-glowise_theme_toggle [role="switch"][aria-checked="true"] {{
        background: var(--accent) !important;
    }}

    .st-key-glowise_theme_toggle::before {{
        content: "☀️";
        font-size: 0.85rem;
        margin-right: 0.3rem;
    }}

    .st-key-glowise_theme_toggle:has([role="switch"][aria-checked="true"])::before {{
        content: "🌙";
    }}

    .st-key-glowise_theme_toggle::after {{
        content: "lite";
        font-family: 'Outfit', sans-serif;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: lowercase;
        color: var(--text-muted);
        margin-left: 0.35rem;
    }}

    .st-key-glowise_theme_toggle:has([role="switch"][aria-checked="true"])::after {{
        content: "dark";
        color: var(--accent-soft);
    }}

    .st-key-glowise_theme_toggle > div {{
        display: flex !important;
        align-items: center !important;
    }}

    /* ── Text visibility ── */
    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] li,
    [data-testid="stAppViewContainer"] .stMarkdown,
    [data-testid="stAppViewContainer"] .stMarkdown p {{
        color: var(--text) !important;
    }}

    [data-testid="stAppViewContainer"] .stMarkdown strong,
    [data-testid="stAppViewContainer"] strong {{
        color: var(--heading) !important;
    }}

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stMarkdown p {{
        color: var(--text) !important;
    }}

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: var(--heading) !important;
    }}

    [data-testid="stCaptionContainer"], .stCaption {{
        color: var(--text-muted) !important;
    }}

    [data-testid="stWidgetLabel"] p, label[data-testid="stWidgetLabel"] {{
        color: var(--text) !important;
        font-weight: 500 !important;
    }}

    [data-testid="stCheckbox"] label span,
    [data-testid="stCheckbox"] label p {{
        color: var(--text) !important;
    }}

    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary span,
    [data-testid="stExpander"] p {{
        color: var(--text) !important;
    }}

    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] span {{
        color: var(--text) !important;
    }}

    [data-testid="stStatusWidget"] p,
    [data-testid="stStatusWidget"] label,
    [data-testid="stStatusWidget"] span {{
        color: var(--text) !important;
    }}

    div[data-baseweb="select"] span,
    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea {{
        color: var(--text) !important;
        -webkit-text-fill-color: var(--text) !important;
    }}

    [data-testid="stInfo"] p,
    [data-testid="stWarning"] p,
    [data-testid="stSuccess"] p,
    [data-testid="stError"] p {{
        color: var(--text) !important;
    }}

    [data-baseweb="tag"] {{
        background-color: var(--tag-bg) !important;
        color: var(--tag-text) !important;
        border-radius: var(--radius-pill) !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    section[data-testid="stMain"] > div {{
        padding-top: 3rem;
    }}

    hr {{
        border-color: var(--border) !important;
        opacity: 0.6;
    }}

    /* ── Styled visuals (mockup-style frames) ── */
    .visual-frame {{
        position: relative;
        border-radius: var(--radius);
        overflow: hidden;
        border: 1px solid var(--border);
        background: var(--card);
        box-shadow: 0 20px 50px var(--shadow);
    }}

    .visual-frame .visual-glow {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            145deg,
            var(--accent-glow) 0%,
            transparent 45%,
            transparent 70%,
            var(--mesh-2) 100%
        );
        pointer-events: none;
        z-index: 2;
    }}

    .visual-frame img {{
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    .hero-visual {{
        min-height: 320px;
        aspect-ratio: 3 / 4;
    }}

    .hero-visual img {{
        min-height: 320px;
    }}

    .visual-chip {{
        position: absolute;
        left: 1rem;
        bottom: 1rem;
        z-index: 3;
        padding: 0.4rem 0.85rem;
        border-radius: var(--radius-pill);
        font-family: 'Outfit', sans-serif;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: lowercase;
        color: var(--heading);
        background: var(--card);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        box-shadow: 0 6px 20px var(--shadow);
    }}

    .visual-tag {{
        position: absolute;
        top: 1rem;
        right: 1rem;
        z-index: 3;
        padding: 0.3rem 0.7rem;
        border-radius: var(--radius-pill);
        font-family: 'Outfit', sans-serif;
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--btn-text);
        background: var(--gradient);
    }}

    .banner-visual {{
        margin-top: 1.25rem;
        min-height: 220px;
        aspect-ratio: 16 / 7;
    }}

    .banner-visual img {{
        min-height: 220px;
        filter: saturate(1.05);
    }}

    .banner-overlay {{
        position: absolute;
        inset: auto 0 0 0;
        z-index: 3;
        padding: 1.25rem 1.5rem;
        background: linear-gradient(0deg, rgba(0,0,0,0.55) 0%, transparent 100%);
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }}

    .banner-label {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #fff;
        letter-spacing: -0.02em;
    }}

    .banner-sub {{
        font-size: 0.78rem;
        color: rgba(255,255,255,0.85);
        font-weight: 500;
    }}

    .hero-visual-wrap {{
        margin-top: 0.25rem;
    }}
</style>
"""
