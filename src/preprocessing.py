import pandas as pd
import re

def load_data(file_path):
    """
    Loads the skincare products dataset.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def clean_ingredients(ingredients_str):
    """
    Cleans and normalizes the ingredients string.
    - Lowercase conversion
    - Removing extra spaces
    - Splitting by comma
    - Stripping whitespace
    """
    if not isinstance(ingredients_str, str):
        return ""
    
    # Lowercase
    ingredients_str = ingredients_str.lower()
    
    # Remove special characters except commas
    ingredients_str = re.sub(r'[^a-z0-9, ]', '', ingredients_str)
    
    # Split, strip, and rejoin to normalize spaces
    ingredients_list = [i.strip() for i in ingredients_str.split(',')]
    ingredients_list = [i for i in ingredients_list if i] # Remove empty strings
    
    return ", ".join(ingredients_list)

def preprocess_dataframe(df):
    """
    Applies preprocessing to the entire dataframe, supporting both the
    original generated dataset and the new Sephora dataset.
    """
    # 1. Map columns if they exist (Sephora Dataset mapping)
    column_mapping = {
        'Label': 'category',
        'Brand': 'brand',
        'Name': 'product_name',
        'Rank': 'rating'
    }
    for old_col, new_col in column_mapping.items():
        if old_col in df.columns and new_col not in df.columns:
            df[new_col] = df[old_col]

    # 2. Handle missing values
    df = df.fillna({
        'product_name': 'Unknown Product',
        'brand': 'Unknown Brand',
        'ingredients': '',
        'Ingredients': '',
        'skin_type': 'all',
        'concern': 'general',
        'sensitive_skin_safe': False,
        'rating': 4.0
    })
    
    # Use 'Ingredients' if 'ingredients' is missing
    if 'Ingredients' in df.columns and ('ingredients' not in df.columns or df['ingredients'].str.len().mean() < 5):
        df['ingredients'] = df['Ingredients']

    # 3. Handle binary skin type columns (Sephora format)
    if 'Combination' in df.columns:
        def get_skin_type_string(row):
            types = []
            if row.get('Combination') == 1: types.append('combination')
            if row.get('Dry') == 1: types.append('dry')
            if row.get('Normal') == 1: types.append('normal')
            if row.get('Oily') == 1: types.append('oily')
            return ", ".join(types) if types else 'all'
        df['skin_type'] = df.apply(get_skin_type_string, axis=1)

    if 'Sensitive' in df.columns:
        df['sensitive_skin_safe'] = df['Sensitive'].apply(lambda x: True if x == 1 else False)

    # 4. Infer usage (AM/PM/Both)
    def infer_usage(row):
        cat = str(row.get('category', '')).lower()
        name = str(row.get('product_name', '')).lower()
        if 'sun' in cat or 'sun' in name or 'spf' in name:
            return 'AM'
        if 'night' in cat or 'night' in name or 'sleeping' in name:
            return 'PM'
        if 'cleanser' in cat:
            return 'Both'
        if 'moisturizer' in cat:
            return 'Both'
        return 'Both'
    
    if 'usage' not in df.columns:
        df['usage'] = df.apply(infer_usage, axis=1)

    # 5. Infer concern
    def infer_concern(row):
        ingredients = str(row.get('ingredients', '')).lower()
        name = str(row.get('product_name', '')).lower()
        concerns = []
        if any(x in ingredients or x in name for x in ['acne', 'salicylic', 'blemish']): concerns.append('acne')
        if any(x in ingredients or x in name for x in ['hydrate', 'hyaluronic', 'dry']): concerns.append('hydration')
        if any(x in ingredients or x in name for x in ['aging', 'wrinkle', 'retinol', 'fine line']): concerns.append('aging')
        if any(x in ingredients or x in name for x in ['bright', 'vitamin c', 'niacinamide', 'dark spot']): concerns.append('brightening')
        if any(x in ingredients or x in name for x in ['sensitive', 'redness', 'soothe', 'calm']): concerns.append('sensitivity')
        if any(x in ingredients or x in name for x in ['pore', 'texture', 'exfoliate', 'bha', 'aha']): concerns.append('pores')
        return ", ".join(concerns) if concerns else 'general'

    if 'concern' not in df.columns or df['concern'].str.contains('general').all():
        df['concern'] = df.apply(infer_concern, axis=1)

    # 6. Lowercase and clean ingredients
    df['cleaned_ingredients'] = df['ingredients'].apply(clean_ingredients)
    
    # 7. Normalize skin_type and concern
    df['skin_type'] = df['skin_type'].str.lower()
    df['concern'] = df['concern'].str.lower()
    
    # 8. Remove duplicates
    df = df.drop_duplicates(subset=['product_name', 'brand'])
    
    return df

if __name__ == "__main__":
    # Test the preprocessing
    df = load_data("data/skincare_products.csv")
    if df is not None:
        processed_df = preprocess_dataframe(df)
        print("Preprocessing complete. Sample data:")
        print(processed_df[['product_name', 'cleaned_ingredients']].head())
