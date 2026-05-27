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
    Applies preprocessing to the entire dataframe.
    """
    # 1. Handle missing values
    df = df.fillna({
        'product_name': 'Unknown Product',
        'brand': 'Unknown Brand',
        'ingredients': '',
        'skin_type': 'All',
        'concern': 'General',
        'sensitive_skin_safe': False
    })
    
    # 2. Lowercase and clean ingredients
    df['cleaned_ingredients'] = df['ingredients'].apply(clean_ingredients)
    
    # 3. Normalize skin_type and concern (lowercase and list format)
    df['skin_type'] = df['skin_type'].str.lower()
    df['concern'] = df['concern'].str.lower()
    
    # 4. Remove duplicates
    df = df.drop_duplicates(subset=['product_name', 'brand'])
    
    return df

if __name__ == "__main__":
    # Test the preprocessing
    df = load_data("data/skincare_products.csv")
    if df is not None:
        processed_df = preprocess_dataframe(df)
        print("Preprocessing complete. Sample data:")
        print(processed_df[['product_name', 'cleaned_ingredients']].head())
