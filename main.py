from src.preprocessing import load_data, preprocess_dataframe
from src.safety_filter import filter_by_safety, get_default_irritants
from src.recommender import SkincareRecommender
from src.explainability import explain_recommendation

def run_glowise(user_profile, avoided_ingredients=None):
    """
    Main execution flow for Glowise recommendation system.
    """
    # 1. Load and Preprocess Data
    df = load_data("data/skincare_products.csv")
    if df is None:
        return "Error: Could not load data."
    
    df = preprocess_dataframe(df)
    
    # 2. Apply Safety Filter
    is_sensitive = user_profile.get("is_sensitive", False)
    safe_df = filter_by_safety(df, user_allergies=avoided_ingredients, is_sensitive=is_sensitive)
    
    if safe_df.empty:
        return "No products found matching your safety requirements."
    
    # 3. Generate Recommendations
    recommender = SkincareRecommender(safe_df)
    recommendations = recommender.recommend(user_profile, top_n=3)
    
    # 4. Generate Explanations
    irritants = get_default_irritants()
    results = []
    for _, product in recommendations.iterrows():
        explanation = explain_recommendation(product, user_profile, irritants)
        results.append({
            "product": product['product_name'],
            "brand": product['brand'],
            "explanation": explanation,
            "ingredients": product['ingredients']
        })
        
    return results

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
    print("\nProcessing...\n")
    
    recommendations = run_glowise(user_input, avoided_ingredients=avoid)
    
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        for i, rec in enumerate(recommendations, 1):
            print(f"Recommendation #{i}: {rec['product']} by {rec['brand']}")
            print(f"Why: {rec['explanation']}")
            print("-" * 30)
