from src.data_loader import load_all_datasets
from src.safety_filter import filter_by_safety, get_default_irritants
from src.recommender import SkincareRecommender
from src.explainability import explain_recommendation
from src.train_model import load_trained_model, train_recommender
import os


def get_product_catalog():
    """Returns the merged, preprocessed product catalog."""
    combined_path = os.path.join("data", "combined_products.csv")
    if os.path.exists(combined_path):
        from src.preprocessing import load_data, preprocess_dataframe
        df = load_data(combined_path)
        if df is not None:
            return preprocess_dataframe(df)
    return load_all_datasets()


def get_routine(user_profile, avoided_ingredients=None):
    """
    Builds a complete AM/PM routine using the merged trained catalog.
    """
    df = get_product_catalog()
    if df is None:
        return "Error: Could not load data."

    is_sensitive = user_profile.get("is_sensitive", False)
    safe_df = filter_by_safety(
        df, user_allergies=avoided_ingredients, is_sensitive=is_sensitive
    )

    if safe_df.empty:
        return "No products found matching your safety requirements."

    artifact = load_trained_model()
    recommender = SkincareRecommender(safe_df, artifact=artifact)
    routine = recommender.recommend_routine(user_profile)

    irritants = get_default_irritants()
    for time in ["AM", "PM"]:
        for cat, product in routine[time].items():
            product['explanation'] = explain_recommendation(
                product, user_profile, irritants
            )

    return routine


if __name__ == "__main__":
    if not os.path.exists("models/recommender_model.joblib"):
        print("Training model on merged datasets...")
        train_recommender(save=True)

    user_input = {
        "skin_type": "dry",
        "concern": "hydration",
        "is_sensitive": True
    }
    avoid = ["alcohol"]

    print("--- Glowise AI Skincare Recommender ---")
    print(f"User Profile: {user_input}")
    print(f"Avoid: {avoid}")
    print("\nProcessing Routine...\n")

    routine = get_routine(user_input, avoided_ingredients=avoid)

    if isinstance(routine, str):
        print(routine)
    else:
        for time in ["AM", "PM"]:
            print(f"=== {time} ROUTINE ===")
            for cat, rec in routine[time].items():
                print(f"[{cat}] {rec['product_name']} by {rec['brand']}")
                print(f"Why: {rec['explanation']}")
            print("-" * 30)
