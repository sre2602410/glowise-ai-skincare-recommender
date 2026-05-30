import streamlit as st
import sys
import os
import time

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import get_routine
from src.utils import get_skin_types, get_concerns
from src.image_processor import analyze_skin_image

# Page Config
st.set_page_config(
    page_title="Glowise - AI Skincare Expert",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for Luxury Aesthetic - defined as a string first
LUXURY_STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
    /* Support for both Light and Dark modes */
    :root {
        --luxury-gold: #C5A059;
        --luxury-cream: #FAF9F6;
        --luxury-charcoal: #1A1A1A;
        --luxury-border: #E5E5E5;
        --text-color: #2C2C2C;
        --card-bg: #FFFFFF;
        --tag-bg: #F9F9F9;
        --tag-text: #666666;
        --explanation-bg: #FDFDFD;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --luxury-cream: #121212;
            --luxury-charcoal: #FAF9F6;
            --luxury-border: #333333;
            --text-color: #E0E0E0;
            --card-bg: #1E1E1E;
            --tag-bg: #2A2A2A;
            --tag-text: #AAAAAA;
            --explanation-bg: #1A1A1A;
        }
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text-color);
    }

    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400;
        letter-spacing: -0.5px;
        color: var(--luxury-charcoal);
    }

    .stApp {
        background-color: var(--luxury-cream);
    }

    .logo-text {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 4rem;
        color: var(--luxury-charcoal);
        margin-bottom: 0;
        letter-spacing: -2px;
        text-transform: lowercase;
    }

    .logo-sub {
        font-size: 0.9rem;
        color: var(--luxury-gold);
        margin-top: -10px;
        margin-bottom: 2.5rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 6px;
    }

    .stButton>button {
        background: var(--luxury-charcoal) !important;
        color: var(--luxury-cream) !important;
        border: 1px solid var(--luxury-gold) !important;
        border-radius: 0px;
        padding: 1rem 2.5rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.4s ease;
        width: 100%;
    }

    .stButton>button:hover {
        background: var(--luxury-gold) !important;
        color: #FFFFFF !important;
        letter-spacing: 3px;
    }

    .recommendation-card {
        padding: 3rem;
        border-radius: 0px;
        background: var(--card-bg);
        border: 1px solid var(--luxury-border);
        margin-bottom: 3rem;
        transition: all 0.5s ease;
    }

    .recommendation-card:hover {
        border-color: var(--luxury-gold);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }

    .product-title {
        font-size: 2rem;
        font-weight: 400;
        font-family: 'Playfair Display', serif;
        margin-bottom: 0.5rem;
        color: var(--luxury-charcoal);
    }

    .brand-title {
        color: var(--luxury-gold);
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    .ingredient-tag {
        display: inline-block;
        background: var(--tag-bg);
        color: var(--tag-text);
        padding: 0.4rem 1rem;
        border-radius: 0px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid var(--luxury-border);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .explanation-box {
        background: var(--explanation-bg);
        padding: 2rem;
        border: 1px solid var(--luxury-border);
        margin-top: 2rem;
        font-style: italic;
        color: var(--tag-text);
    }

    .rating-badge {
        display: inline-flex;
        align-items: center;
        border-bottom: 1px solid var(--luxury-gold);
        color: var(--luxury-gold);
        padding: 0.2rem 0;
        font-weight: 600;
        font-size: 0.9rem;
        margin-left: 15px;
    }

    .stSelectbox:focus-within, .stMultiSelect:focus-within, .stTextInput:focus-within {
        border-color: var(--luxury-gold) !important;
    }

    .step-box {
        padding: 1.5rem;
        background: var(--card-bg);
        border: 1px solid var(--luxury-border);
        margin-bottom: 1rem;
        color: var(--luxury-charcoal);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }

    [data-testid="stMetricValue"] {
        font-family: 'Playfair Display', serif;
        color: var(--luxury-gold) !important;
    }

    /* Streamlit sidebar and other elements fix for dark mode */
    [data-testid="stSidebar"] {
        background-color: var(--luxury-cream);
        border-right: 1px solid var(--luxury-border);
    }
</style>
"""

# Inject CSS
st.markdown(LUXURY_STYLE, unsafe_allow_html=True)

# Helper for Logo
def draw_logo(size="large"):
    if size == "large":
        st.markdown('<p class="logo-text">glowise</p>', unsafe_allow_html=True)
        st.markdown('<p class="logo-sub">The Science of Bespoke Skincare</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="logo-text" style="font-size: 2.2rem;">glowise</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    draw_logo(size="small")
    st.write("---")
    
    st.subheader("📸 AI Skin Scanner")
    uploaded_file = st.file_uploader("Upload a photo of your skin", type=["jpg", "jpeg", "png"])
    
    scan_results = None
    if uploaded_file is not None:
        with st.spinner("Analyzing skin..."):
            image_bytes = uploaded_file.read()
            scan_results = analyze_skin_image(image_bytes)
            if scan_results:
                st.success("Analysis complete.")
                
                cols = st.columns(3)
                with cols[0]:
                    st.metric("Redness", f"{int(scan_results['scores']['redness']*100)}%")
                with cols[1]:
                    st.metric("Spots", f"{int(scan_results['scores']['dark_spots']*100)}%")
                with cols[2]:
                    st.metric("Texture", f"{int(scan_results['scores']['texture']*100)}%")
    
    st.write("---")
    st.subheader("👤 Your Profile")
    skin_type = st.selectbox("Skin type", get_skin_types())
    
    default_concerns = []
    if scan_results:
        default_concerns = [c.capitalize() for c in scan_results["detected_concerns"] if c.capitalize() in get_concerns()]
        
    concern = st.multiselect("Concerns", get_concerns(), default=default_concerns)
    is_sensitive = st.checkbox("Sensitive Skin", value=("sensitivity" in scan_results["detected_concerns"] if scan_results else False))
    
    st.write("")
    st.subheader("🚫 Safety")
    avoided = st.text_input("Ingredients to avoid", placeholder="e.g. alcohol")
    
    st.write("")
    predict_btn = st.button("Curate My Routine", use_container_width=True)

# Main Content
col_header1, col_header2 = st.columns([2.5, 1])
with col_header1:
    draw_logo(size="large")
    st.markdown("### Elevate your skincare to a bespoke ritual. ✨")
    st.write("Our AI-driven analysis curates a sophisticated routine from a selection of over 1,400 clinical formulations.")
with col_header2:
    st.image("https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&w=400&q=80", width=250)

if predict_btn:
    if not concern:
        st.error("Please select at least one concern.")
    else:
        user_profile = {
            "skin_type": skin_type.lower(),
            "concern": ", ".join(concern).lower(),
            "is_sensitive": is_sensitive
        }
        
        avoid_list = [a.strip() for a in avoided.split(",") if a.strip()]
        
        with st.status("💎 Glowise AI is curating...", expanded=True) as status:
            st.markdown('<div class="step-box">1. verifying safety & biocompatibility...</div>', unsafe_allow_html=True)
            time.sleep(0.6)
            
            st.markdown('<div class="step-box">2. synchronizing AM/PM ritual...</div>', unsafe_allow_html=True)
            routine = get_routine(user_profile, avoided_ingredients=avoid_list)
            time.sleep(0.6)
            
            st.markdown('<div class="step-box">3. finalising your bespoke routine...</div>', unsafe_allow_html=True)
            status.update(label="Collection Complete ✨", state="complete", expanded=False)
        
        if isinstance(routine, str):
            st.warning(f"Note: {routine}")
        else:
            st.markdown(f"### 🖋️ Your Bespoke Skincare Routine")
            
            all_products = list(routine["AM"].values()) + list(routine["PM"].values())
            top_concerns = set()
            for p in all_products:
                if 'concern' in p:
                    top_concerns.update([c.strip().capitalize() for c in p['concern'].split(',')])
            
            st.info(f"✨ Ritual Focus: {', '.join(list(top_concerns)[:3])}. Optimized for {skin_type} skin.")

            tab_am, tab_pm = st.tabs(["☀️ The Day Ritual", "🌙 The Night Ritual"])
            
            with tab_am:
                for cat, rec in routine["AM"].items():
                    with st.container():
                        ing_list = rec['ingredients'].split(',')
                        ingredients_html = "".join([f'<span class="ingredient-tag">{i.strip()}</span>' for i in ing_list[:8]])
                        
                        st.markdown(f"""
                            <div class="recommendation-card">
                                <div class="brand-title">{rec['brand']} | {cat.upper()}</div>
                                <div style="display: flex; align-items: center;">
                                    <div class="product-title">{rec['product_name']}</div>
                                    <span class="rating-badge">Rating {rec.get('rating', 4.5)}</span>
                                </div>
                                <div style="margin: 1.5rem 0;">
                                    {ingredients_html}
                                </div>
                                <div class="explanation-box">
                                    {rec['explanation']}
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            
            with tab_pm:
                for cat, rec in routine["PM"].items():
                    with st.container():
                        ing_list = rec['ingredients'].split(',')
                        ingredients_html = "".join([f'<span class="ingredient-tag">{i.strip()}</span>' for i in ing_list[:8]])
                        
                        st.markdown(f"""
                            <div class="recommendation-card">
                                <div class="brand-title">{rec['brand']} | {cat.upper()}</div>
                                <div style="display: flex; align-items: center;">
                                    <div class="product-title">{rec['product_name']}</div>
                                    <span class="rating-badge">Rating {rec.get('rating', 4.5)}</span>
                                </div>
                                <div style="margin: 1.5rem 0;">
                                  {ingredients_html}
                                </div>
                                <div class="explanation-box">
                                    {rec['explanation']}
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

else:
    # Beautiful Landing Section
    st.write("---")
    st.markdown("### The Glowise Methodology")
    L_col1, L_col2, L_col3 = st.columns(3)
    
    with L_col1:
        st.markdown("#### 🛡️ Biocompatibility")
        st.write("Our system cross-references formulations with your sensitivity profile.")
        
    with L_col2:
        st.markdown("#### 🧠 AI Synthesis")
        st.write("Using TF-IDF vectorization, we identify the precise active ingredients required.")
        
    with L_col3:
        st.markdown("#### 🧪 Clinical Insights")
        st.write("We provide transparent, ingredient-focused explanations.")

    st.image("https://images.unsplash.com/photo-1612817288484-6f916006741a?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #5d6d7e; font-size: 0.9rem;'>Glowise AI &copy; 2026 | The Science of Bespoke Skincare</p>", unsafe_allow_html=True)
