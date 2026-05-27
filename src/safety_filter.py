def get_default_irritants():
    """
    Returns a list of common irritants in skincare.
    """
    return [
        "alcohol denat", "fragrance", "parfum", "menthol", "peppermint", 
        "lemon juice", "essential oils", "sls", "sodium lauryl sulfate"
    ]

def filter_by_safety(df, user_allergies=None, is_sensitive=False):
    """
    Filters out products based on user allergies and skin sensitivity.
    """
    if user_allergies is None:
        user_allergies = []
    
    # Normalize user allergies
    user_allergies = [a.lower().strip() for a in user_allergies if a]
    
    # 1. Filter by specific user allergies/avoided ingredients
    def contains_allergy(ingredients_str):
        ingredients_list = [i.strip() for i in ingredients_str.lower().split(',')]
        for allergy in user_allergies:
            if any(allergy in ingredient for ingredient in ingredients_list):
                return True
        return False

    df = df[~df['cleaned_ingredients'].apply(contains_allergy)]
    
    # 2. If sensitive skin, filter out products not marked as sensitive safe
    # and products containing common irritants
    if is_sensitive:
        # Keep only sensitive safe products
        df = df[df['sensitive_skin_safe'] == True]
        
        # Further filter out common irritants just in case
        irritants = get_default_irritants()
        
        def contains_irritant(ingredients_str):
            ingredients_list = [i.strip() for i in ingredients_str.lower().split(',')]
            for irritant in irritants:
                if any(irritant in ingredient for ingredient in ingredients_list):
                    return True
            return False
            
        df = df[~df['cleaned_ingredients'].apply(contains_irritant)]
        
    return df

if __name__ == "__main__":
    import pandas as pd
    from preprocessing import load_data, preprocess_dataframe
    
    df = load_data("data/skincare_products.csv")
    if df is not None:
        df = preprocess_dataframe(df)
        
        # Test allergy filtering
        print(f"Total products: {len(df)}")
        safe_df = filter_by_safety(df, user_allergies=["salicylic acid"], is_sensitive=True)
        print(f"Products after filtering for 'salicylic acid' and sensitivity: {len(safe_df)}")
        print(safe_df[['product_name', 'sensitive_skin_safe']])
