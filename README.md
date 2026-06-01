# Glowise – AI-Powered Bespoke Skincare Ritual ✨

Glowise is a sophisticated, clinical-grade skincare recommendation system that combines computer vision, rule-based safety filtering, and natural language processing to curate the perfect routine for your unique skin profile.

## 🚀 Key Features

- **AI Skin Scanner (CNN)**: Utilizes Convolutional Neural Networks and OpenCV to analyze your skin from a photo, detecting concerns like redness, dark spots, and texture issues.
- **Sephora Intelligence**: Powered by a real-world dataset of over 1,400+ premium products from brands like *Tatcha*, *Drunk Elephant*, and *The Ordinary*.
- **AM/PM Bespoke Rituals**: Automatically synchronizes your day and night cycles with specialized categories like *Treatments*, *Eye Creams*, and *Sunscreen*.
- **Safety & Biocompatibility**: A rigorous rule-based engine that cross-references product formulations against your allergies and sensitivity profile.
- **Minimalist Luxury UI**: A refined, high-end interface featuring a cream and charcoal palette, elegant serif typography, and full Dark Mode support.
- **Explainable AI (XAI)**: Transparent, ingredient-focused insights that explain the scientific reasoning behind every selection.

## 🏗️ Architecture

```text
glowise/
│
├── data/
│   ├── sephora_products.csv       # 1,400+ real-world products
│   └── skincare_products.csv      # Initial seed dataset
│
├── src/
│   ├── image_processor.py         # CNN & OpenCV Skin Analysis
│   ├── recommender.py             # ML Engine (TF-IDF + Cosine Similarity)
│   ├── safety_filter.py           # Biocompatibility Logic
│   ├── preprocessing.py           # Data Pipeline & Normalization
│   ├── explainability.py          # Clinical Insight Generator
│   └── utils.py                   # System Utilities
│
├── app/
│   └── app.py                     # Streamlit Luxury Interface
│
├── requirements.txt               # System Dependencies
├── main.py                        # CLI Verification Engine
└── README.md                      # Project Documentation
```

## 🛠️ Tech Stack

- **Computer Vision**: TensorFlow (CNN), OpenCV
- **Data Science**: Pandas, NumPy, Scikit-learn
- **Frontend**: Streamlit (Bespoke CSS)
- **ML Logic**: TF-IDF Vectorization, Content-Based Filtering

## ⚙️ Setup & Execution

### 1. Environment Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Ritual
```bash
streamlit run app/app.py
```

## 🧪 Clinical Verification (CLI)
Verify the recommendation logic directly in your terminal:
```bash
python main.py
```

---
*Glowise: Elevating Skincare through Artificial Intelligence and Scientific Precision.*
