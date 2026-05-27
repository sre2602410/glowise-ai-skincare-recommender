# Glowise – AI-Based Skincare Recommendation System ✨

Glowise is a production-style hybrid recommendation system designed to provide personalized skincare advice. It combines rule-based safety filtering with machine learning to ensure recommendations are both effective and safe for users.

## 🚀 Features

- **Personalized Recommendations**: Uses TF-IDF and Cosine Similarity to match products with user skin types and concerns.
- **Safety Filtering**: Automatically excludes products containing ingredients the user is allergic to or common irritants for sensitive skin.
- **Explainable AI (XAI)**: Provides clear, natural language explanations for every recommendation, highlighting key beneficial ingredients and safety aspects.
- **Modern UI**: Built with Streamlit for a clean, interactive user experience.

## 🏗️ Architecture

```text
glowise-ai-skincare-recommender/
│
├── data/
│   └── skincare_products.csv      # Sample dataset of products
│
├── notebooks/
│   └── experimentation.ipynb      # Exploration and ML prototyping
│
├── src/
│   ├── preprocessing.py           # Data cleaning and normalization
│   ├── recommender.py             # ML engine (TF-IDF + Cosine Similarity)
│   ├── safety_filter.py           # Rule-based safety logic
│   ├── explainability.py          # Natural language explanation generator
│   └── utils.py                   # Helper functions
│
├── app/
│   └── app.py                     # Streamlit web application
│
├── requirements.txt               # Project dependencies
├── .gitignore                     # Git exclusion rules
├── main.py                        # CLI entry point for testing
└── README.md                      # Project documentation
```

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend / ML**: [Python](https://www.python.org/), [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Scikit-learn](https://scikit-learn.org/)
- **ML Concepts**: TF-IDF Vectorization, Cosine Similarity, Content-Based Filtering.

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/glowise-ai-skincare-recommender.git
cd glowise-ai-skincare-recommender
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run app/app.py
```

## 🧪 Testing the CLI
You can also run the system via command line to see the logic in action:
```bash
python main.py
```

## 🔮 Future Improvements

- **Ingredient Database Expansion**: Integrate a larger, real-world skincare dataset (e.g., from Kaggle or scraping).
- **Deep Learning**: Explore neural collaborative filtering for more complex user-product interactions.
- **User Reviews**: Incorporate sentiment analysis of user reviews into the recommendation score.
- **Dermatologist Validation**: Add a verification layer for ingredient benefit mappings.

---
*Created as a demonstration of production-level AI/ML project structuring.*
