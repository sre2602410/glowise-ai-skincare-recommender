import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SkincareRecommender:
    def __init__(self, df):
        self.df = df
        self.vectorizer = TfidfVectorizer(token_pattern=r'[^,]+') # Treat ingredients as tokens
        self.tfidf_matrix = None
        self._fit()

    def _fit(self):
        """
        Fits the TF-IDF vectorizer on the cleaned ingredients.
        """
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['cleaned_ingredients'])

    def recommend(self, user_profile, top_n=5):
        """
        Recommends products based on user profile (skin type and concerns).
        """
        # Create a query string from user profile
        query = f"{user_profile['skin_type']}, {user_profile['concern']}"
        
        # Transform the query into a TF-IDF vector
        query_vector = self.vectorizer.transform([query.lower()])
        
        # Calculate cosine similarity between query and all products
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        
        # Add similarity scores to the dataframe
        temp_df = self.df.copy()
        temp_df['similarity_score'] = similarities
        
        # Prioritize skin type matching in the query (simple rule-based boost)
        # We can also filter the dataframe first by skin type if we want strict matching
        # But content-based filtering usually handles this via ingredients
        
        # Sort by similarity score
        recommendations = temp_df.sort_values(by='similarity_score', ascending=False).head(top_n)
        
        return recommendations

if __name__ == "__main__":
    from preprocessing import load_data, preprocess_dataframe
    from safety_filter import filter_by_safety
    
    # Load and preprocess
    df = load_data("data/skincare_products.csv")
    if df is not None:
        df = preprocess_dataframe(df)
        
        # Apply safety filter first
        user_allergies = ["salicylic acid"]
        is_sensitive = True
        safe_df = filter_by_safety(df, user_allergies=user_allergies, is_sensitive=is_sensitive)
        
        if not safe_df.empty:
            # Initialize recommender with safe products
            recommender = SkincareRecommender(safe_df)
            
            # User profile
            user_profile = {
                "skin_type": "dry",
                "concern": "hydration"
            }
            
            # Get recommendations
            recs = recommender.recommend(user_profile, top_n=3)
            print("\nTop Recommendations:")
            print(recs[['product_name', 'brand', 'similarity_score']])
        else:
            print("No safe products found for the given filters.")
