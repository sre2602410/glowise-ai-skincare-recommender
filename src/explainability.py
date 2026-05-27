def explain_recommendation(product, user_profile, irritants_list):
    """
    Generates a natural language explanation for why a product was recommended.
    """
    product_name = product['product_name']
    ingredients = [i.strip() for i in product['cleaned_ingredients'].split(',')]
    concerns = user_profile['concern'].lower().split(',')
    
    # Identify key ingredients that match user concerns (simple heuristic)
    # In a real app, we might have a mapping of ingredient -> benefit
    benefit_map = {
        "hyaluronic acid": "hydration",
        "glycerin": "hydration",
        "salicylic acid": "acne",
        "niacinamide": "brightening and oil control",
        "retinol": "aging",
        "vitamin c": "brightening",
        "zinc oxide": "sun protection",
        "centella asiatica": "soothing",
        "ceramide": "barrier repair"
    }
    
    matching_benefits = []
    for ing in ingredients:
        for key, benefit in benefit_map.items():
            if key in ing:
                matching_benefits.append((ing, benefit))
    
    # Unique matches
    unique_benefits = list(set(matching_benefits))
    
    # Check for absence of irritants
    irritants_found = [i for i in irritants_list if any(i in ing for ing in ingredients)]
    
    explanation = f"**{product_name}** is recommended because it aligns with your skin type and concerns."
    
    if unique_benefits:
        benefit_str = ", ".join([f"{b[0]} (helps with {b[1]})" for b in unique_benefits[:3]])
        explanation += f" It contains key ingredients like {benefit_str}."
    
    if not irritants_found:
        explanation += " Importantly, it avoids common irritants like alcohol and fragrance, making it a safe choice for your profile."
    else:
        explanation += " Note: This product contains some ingredients you might want to watch out for if you have very high sensitivity."
        
    return explanation

if __name__ == "__main__":
    # Test
    sample_product = {
        "product_name": "Ultra Hydrating Gel",
        "cleaned_ingredients": "water, glycerin, hyaluronic acid, aloe vera, phenoxyethanol"
    }
    user_profile = {
        "skin_type": "dry",
        "concern": "hydration"
    }
    irritants = ["alcohol", "fragrance"]
    
    print(explain_recommendation(sample_product, user_profile, irritants))
