import streamlit as st
import sys
import os

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import run_glowise
from src.utils import get_skin_types, get_concerns

# Page Config
st.set_page_config(
    page_title="Glowise - AI Skincare Recommender",
    page_icon="✨",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .recommendation-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 5px solid #ff4b4b;
    }
    .product-title {
        color: #1f1f1f;
        font-size: 1.25rem;
        font-weight: bold;
    }
    .brand-title {
        color: #6c757d;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .explanation-text {
        font-style: italic;
        color: #495057;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("✨ Glowise")
st.sidebar.subheader("Your AI Skincare Expert")

skin_type = st.sidebar.selectbox("Select your skin type:", get_skin_types())
concern = st.sidebar.multiselect("What are your concerns?", get_concerns())
is_sensitive = st.sidebar.checkbox("Do you have sensitive skin?")
avoided = st.sidebar.text_input("Ingredients to avoid (comma separated):", placeholder="e.g. alcohol, fragrance")

# Main Content
st.title("Find Your Perfect Skincare Match")
st.write("Glowise uses AI and safety filters to recommend the best products for your unique skin profile.")

if st.sidebar.button("Get Recommendations"):
    if not concern:
        st.warning("Please select at least one concern.")
    else:
        user_profile = {
            "skin_type": skin_type.lower(),
            "concern": ", ".join(concern).lower(),
            "is_sensitive": is_sensitive
        }
        
        avoid_list = [a.strip() for a in avoided.split(",") if a.strip()]
        
        with st.spinner("Analyzing ingredients and matching products..."):
            recommendations = run_glowise(user_profile, avoided_ingredients=avoid_list)
        
        if isinstance(recommendations, str):
            st.error(recommendations)
        else:
            st.subheader(f"Top {len(recommendations)} Recommendations for You")
            
            for rec in recommendations:
                with st.container():
                    st.markdown(f"""
                        <div class="recommendation-card">
                            <div class="product-title">{rec['product']}</div>
                            <div class="brand-title">by {rec['brand']}</div>
                            <hr>
                            <p><strong>Ingredients:</strong> {rec['ingredients']}</p>
                            <div class="explanation-text">{rec['explanation']}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("") # Spacer

else:
    # Landing Page State
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1556228720-195a672e8a03?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="Healthy skin starts here")
    with col2:
        st.subheader("How Glowise Works")
        st.write("""
        - **Safety First**: We filter out products with ingredients you're allergic to.
        - **ML Powered**: Our TF-IDF + Cosine Similarity engine finds products that match your specific skin needs.
        - **Explainable AI**: We don't just recommend; we tell you *why* based on the ingredients.
        """)
        st.info("👈 Fill out your profile in the sidebar to get started!")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Glowise AI Team")
