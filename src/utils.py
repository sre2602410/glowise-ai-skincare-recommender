def format_ingredients(ingredients_str):
    """
    Formats the ingredients string for display.
    """
    return ingredients_str.replace(", ", "\n- ").capitalize()

def get_skin_types():
    return ["Oily", "Dry", "Combination", "Sensitive", "Normal", "All"]

def get_concerns():
    return ["Acne", "Hydration", "Aging", "Brightening", "Sensitivity", "Pores", "Texture"]
