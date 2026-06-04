"""
Train and persist the TF-IDF recommendation model on the merged product catalog.
Run: python -m src.train_model
"""
import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.data_loader import load_all_datasets

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "recommender_model.joblib")
COMBINED_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "combined_products.csv")


def build_feature_text(row):
    parts = [
        str(row.get("product_name", "")),
        str(row.get("brand", "")),
        str(row.get("cleaned_ingredients", "")),
        str(row.get("skin_type", "")),
        str(row.get("concern", "")),
        str(row.get("category", "")),
    ]
    return " ".join(p for p in parts if p and p != "nan").lower()


def train_recommender(df=None, save=True):
    """
    Fits an enhanced TF-IDF model on the merged dataset and optionally persists it.
    """
    if df is None:
        df = load_all_datasets()

    if df is None or df.empty:
        raise ValueError("No training data available. Add CSV files under data/.")

    df = df.reset_index(drop=True)
    df["feature_text"] = df.apply(build_feature_text, axis=1)

    vectorizer = TfidfVectorizer(
        token_pattern=r"(?u)\b[a-z][a-z0-9+\-]*\b",
        ngram_range=(1, 2),
        max_features=15000,
        min_df=1,
        max_df=0.95,
        sublinear_tf=True,
    )
    tfidf_matrix = vectorizer.fit_transform(df["feature_text"])

    artifact = {
        "vectorizer": vectorizer,
        "tfidf_matrix": tfidf_matrix,
        "df": df,
        "product_count": len(df),
        "vocab_size": len(vectorizer.vocabulary_),
    }

    if save:
        os.makedirs(MODEL_DIR, exist_ok=True)
        joblib.dump(artifact, MODEL_PATH)
        export_cols = [
            c
            for c in [
                "product_name",
                "brand",
                "category",
                "usage",
                "skin_type",
                "concern",
                "rating",
                "ingredients",
                "cleaned_ingredients",
                "sensitive_skin_safe",
                "source_dataset",
            ]
            if c in df.columns
        ]
        df[export_cols].to_csv(COMBINED_DATA_PATH, index=False)

    return artifact


def load_trained_model():
    """Loads a persisted model if available."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


if __name__ == "__main__":
    print("Loading merged datasets...")
    artifact = train_recommender(save=True)
    print(f"Model trained on {artifact['product_count']} products.")
    print(f"Vocabulary size: {artifact['vocab_size']}")
    print(f"Saved to {MODEL_PATH}")
