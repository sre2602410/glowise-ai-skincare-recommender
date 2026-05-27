import streamlit as st
import sys
import os

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import get_routine
from src.utils import get_skin_types, get_concerns

# Page Config
st.set_page_config(
    page_title="Glowise - AI Skincare Expert",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for a more "Skincare/Wellness" feel with dark mode support
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;600&display=swap');

    /* Global styles using theme variables */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: transparent;
    }

    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 700;
    }

    /* Logo Styling */
    .logo-text {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 3.5rem;
        background: linear-gradient(135deg, #d63384 0%, #ff8fa3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        letter-spacing: -1px;
    }

    .logo-sub {
        font-size: 1.1rem;
        color: #888;
        margin-top: -10px;
        margin-bottom: 2rem;
        font-weight: 400;
        font-style: italic;
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #d63384 0%, #ff8fa3 100%);
        color: white !important;
        border-radius: 50px;
        border: none;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(214, 51, 132, 0.3);
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 25px rgba(214, 51, 132, 0.4);
        color: white !important;
    }

    /* Card Design - Glassmorphism style for Dark/Light mode */
    .recommendation-card {
        padding: 2.5rem;
        border-radius: 30px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2.5rem;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    /* Light mode specific override if needed, but the above is better for both */
    [data-theme="light"] .recommendation-card {
        background: #ffffff;
        border: 1px solid #f0f0f0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }

    .recommendation-card:hover {
        transform: translateY(-8px);
        border-color: #d63384;
    }

    .product-title {
        font-size: 1.8rem;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
        margin-bottom: 0.3rem;
    }

    .brand-title {
        color: #d63384;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .ingredient-tag {
        display: inline-block;
        background: rgba(214, 51, 132, 0.1);
        color: #d63384;
        padding: 0.4rem 1rem;
        border-radius: 12px;
        font-size: 0.85rem;
        margin-right: 0.6rem;
        margin-bottom: 0.6rem;
        border: 1px solid rgba(214, 51, 132, 0.2);
        font-weight: 500;
    }

    .explanation-box {
        background: rgba(214, 51, 132, 0.03);
        padding: 1.5rem;
        border-radius: 20px;
        border-left: 6px solid #d63384;
        margin-top: 1.8rem;
    }

    .explanation-text {
        line-height: 1.8;
        font-size: 1.05rem;
    }

    .rating-badge {
        display: inline-flex;
        align-items: center;
        background: #f1c40f;
        color: #000;
        padding: 0.2rem 0.6rem;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-left: 10px;
    }

    /* Sidebar focus */
    .stSelectbox:focus-within, .stMultiSelect:focus-within, .stTextInput:focus-within {
        border-color: #d63384 !important;
    }

    /* Step indicator */
    .step-box {
        padding: 1rem;
        border-radius: 15px;
        background: rgba(214, 51, 132, 0.05);
        margin-bottom: 1rem;
        border-left: 4px solid #d63384;
    }
    </style>
""", unsafe_allow_html=True)

# Helper for Logo
def draw_logo(size="large"):
    if size == "large":
        st.markdown('<p class="logo-text">Glowise</p>', unsafe_allow_html=True)
        st.markdown('<p class="logo-sub">AI-Powered Skincare Intelligence</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="logo-text" style="font-size: 2.2rem;">Glowise</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    draw_logo(size="small")
    st.write("---")
    st.subheader("👤 Your Profile")
    skin_type = st.selectbox("What is your skin type?", get_skin_types(), help="Essential for matching base formulas")
    concern = st.multiselect("Main concerns", get_concerns(), help="We prioritize these in our AI matching")
    is_sensitive = st.checkbox("Sensitive Skin ✨")
    
    st.write("")
    st.subheader("🚫 Safety Controls")
    avoided = st.text_input("Ingredients to avoid", placeholder="e.g. alcohol, fragrance")
    
    st.write("")
    predict_btn = st.button("✨ Generate My Routine", use_container_width=True)
    
    st.write("---")
    st.info("💡 Tip: Selecting multiple concerns helps the AI find multi-tasking products.")

# Main Content
col_header1, col_header2 = st.columns([2.5, 1])
with col_header1:
    draw_logo(size="large")
    st.markdown("### Discover skincare that *actually* works for you.")
    st.write("Our hybrid AI system analyzes your unique skin profile against thousands of ingredient combinations to curate a routine that is safe, effective, and scientifically backed.")
with col_header2:
    st.image("https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&w=400&q=80", width=250)

if predict_btn:
    if not concern:
        st.error("Please select at least one skin concern to help our AI find the best match for you! 🌸")
    else:
        user_profile = {
            "skin_type": skin_type.lower(),
            "concern": ", ".join(concern).lower(),
            "is_sensitive": is_sensitive
        }
        
        avoid_list = [a.strip() for a in avoided.split(",") if a.strip()]
        
        with st.status("🔮 Glowise AI is analyzing...", expanded=True) as status:
            st.markdown('<div class="step-box">Step 1: Applying rule-based safety filters...</div>', unsafe_allow_html=True)
            import time
            time.sleep(0.6)
            
            st.markdown('<div class="step-box">Step 2: Building AM and PM routines...</div>', unsafe_allow_html=True)
            routine = get_routine(user_profile, avoided_ingredients=avoid_list)
            time.sleep(0.6)
            
            st.markdown('<div class="step-box">Step 3: Finalizing ingredient-based explanations...</div>', unsafe_allow_html=True)
            status.update(label="Routine Ready! ✨", state="complete", expanded=False)
        
        if isinstance(routine, str):
            st.warning(f"Note: {routine}")
        else:
            st.markdown(f"### ✨ Your Personalized Skincare Routine")
            st.write("Our AI has curated a balance of active ingredients for your day and night cycles:")
            
            tab_am, tab_pm = st.tabs(["☀️ Morning Routine (AM)", "🌙 Evening Routine (PM)"])
            
            with tab_am:
                if not routine["AM"]:
                    st.info("No specific AM products found for this profile.")
                for cat, rec in routine["AM"].items():
                    with st.container():
                        ing_list = rec['ingredients'].split(',')
                        ingredients_html = "".join([f'<span class="ingredient-tag">{i.strip()}</span>' for i in ing_list[:8]])
                        
                        st.markdown(f"""
                            <div class="recommendation-card">
                                <div class="brand-title">{rec['brand']} | {cat.upper()}</div>
                                <div style="display: flex; align-items: center;">
                                    <div class="product-title">{rec['product_name']}</div>
                                    <span class="rating-badge">★ {rec.get('rating', 4.5)}</span>
                                </div>
                                <div style="margin: 1.5rem 0;">
                                    {ingredients_html}
                                </div>
                                <div class="explanation-box">
                                    <div class="explanation-text">
                                        {rec['explanation']}
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            
            with tab_pm:
                if not routine["PM"]:
                    st.info("No specific PM products found for this profile.")
                for cat, rec in routine["PM"].items():
                    with st.container():
                        ing_list = rec['ingredients'].split(',')
                        ingredients_html = "".join([f'<span class="ingredient-tag">{i.strip()}</span>' for i in ing_list[:8]])
                        
                        st.markdown(f"""
                            <div class="recommendation-card">
                                <div class="brand-title">{rec['brand']} | {cat.upper()}</div>
                                <div style="display: flex; align-items: center;">
                                    <div class="product-title">{rec['product_name']}</div>
                                    <span class="rating-badge">★ {rec.get('rating', 4.5)}</span>
                                </div>
                                <div style="margin: 1.5rem 0;">
                                    {ingredients_html}
                                </div>
                                <div class="explanation-box">
                                    <div class="explanation-text">
                                        {rec['explanation']}
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

else:
    # Beautiful Landing Section
    st.write("---")
    st.markdown("### How Glowise Intelligence Works")
    L_col1, L_col2, L_col3 = st.columns(3)
    
    with L_col1:
        st.markdown("#### 🛡️ Safety Filtering")
        st.write("Our first layer is rule-based. It cross-references ingredients with your allergies and sensitivity profile to ensure absolute safety.")
        
    with L_col2:
        st.markdown("#### 🧠 TF-IDF Matching")
        st.write("Our AI vectorizes product formulas and your concerns, calculating a similarity score to find the most effective matches.")
        
    with L_col3:
        st.markdown("#### 🧪 XAI Explanations")
        st.write("We use Explainable AI to break down *why* a product works, focusing on active ingredients like Retinol, Vitamin C, or Ceramides.")

    st.image("https://images.unsplash.com/photo-1612817288484-6f916006741a?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #5d6d7e; font-size: 0.9rem;'>Glowise AI &copy; 2026 | Developed for Excellence in Skincare</p>", unsafe_allow_html=True)
