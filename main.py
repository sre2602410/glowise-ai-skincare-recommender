from src.preprocessing import load_data, preprocess_dataframe
from src.safety_filter import filter_by_safety, get_default_irritants
from src.recommender import SkincareRecommender
from src.explainability import explain_recommendation
import os

def get_routine(user_profile, avoided_ingredients=None):
    """
    Builds a complete AM/PM routine.
    """
    # Use real dataset if it exists, fallback to small one
    if os.path.exists("data/sephora_products.csv"):
        df = load_data("data/sephora_products.csv")
    elif os.path.exists("data/cosmetics.csv"):
        df = load_data("data/cosmetics.csv")
    else:
        df = load_data("data/skincare_products.csv")
        
    if df is None: return "Error: Could not load data."
    
    df = preprocess_dataframe(df)
    is_sensitive = user_profile.get("is_sensitive", False)
    safe_df = filter_by_safety(df, user_allergies=avoided_ingredients, is_sensitive=is_sensitive)
    
    if safe_df.empty:
        return "No products found matching your safety requirements."
    
    recommender = SkincareRecommender(safe_df)
    routine = recommender.recommend_routine(user_profile)
    
    irritants = get_default_irritants()
    
    # Process the routine to add explanations
    for time in ["AM", "PM"]:
        for cat, product in routine[time].items():
            explanation = explain_recommendation(product, user_profile, irritants)
            product['explanation'] = explanation
            
    return routine

if __name__ == "__main__":
    # Example CLI Usage
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
