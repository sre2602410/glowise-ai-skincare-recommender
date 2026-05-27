import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SkincareRecommender:
    def __init__(self, df):
        # Reset index to ensure alignment with TF-IDF matrix rows
        self.df = df.reset_index(drop=True)
        self.vectorizer = TfidfVectorizer(token_pattern=r'[^,]+')
        self.tfidf_matrix = None
        self._fit()

    def _fit(self):
        """
        Fits the TF-IDF vectorizer on a combination of ingredients, skin type, and concerns.
        """
        # Ensure all fields are strings and normalized
        self.df['features'] = (
            self.df['cleaned_ingredients'].fillna('') + ", " + 
            self.df['skin_type'].fillna('') + ", " + 
            self.df['concern'].fillna('') + ", " +
            self.df['category'].fillna('')
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['features'])

    def recommend(self, user_profile, top_n=5, category=None, usage=None):
        """
        Recommends products based on user profile.
        Optionally filter by category and usage (AM/PM).
        """
        temp_df = self.df.copy()
        
        # 1. Filter by category
        if category:
            temp_df = temp_df[temp_df['category'].str.lower() == category.lower()]
            
        # 2. Filter by usage
        if usage:
            # Usage in DB can be 'AM', 'PM', or 'Both'
            temp_df = temp_df[temp_df['usage'].str.lower().isin([usage.lower(), 'both'])]

        if temp_df.empty:
            return pd.DataFrame()

        # 3. Create a query
        concerns = user_profile['concern'].split(',')
        weighted_concern = ", ".join([c.strip() for c in concerns] * 2)
        query = f"{user_profile['skin_type']}, {weighted_concern}, {category if category else ''}"
        
        # 4. Calculate similarity
        query_vector = self.vectorizer.transform([query.lower()])
        filtered_indices = temp_df.index
        similarities = cosine_similarity(query_vector, self.tfidf_matrix[filtered_indices]).flatten()
        
        temp_df['similarity_score'] = similarities
        
        # 5. Calculate final score
        if 'rating' in temp_df.columns:
            temp_df['final_score'] = (0.7 * temp_df['similarity_score']) + (0.3 * (temp_df['rating'] / 5))
        else:
            temp_df['final_score'] = temp_df['similarity_score']
        
        # 6. Filter by similarity and sort
        recommendations = temp_df[temp_df['similarity_score'] > 0]
        
        if recommendations.empty:
            # Fallback to skin type matching if no concern matches
            recommendations = temp_df[temp_df['skin_type'].str.contains(user_profile['skin_type'], case=False)]
            if not recommendations.empty:
                recommendations['final_score'] = recommendations['rating'] / 5 if 'rating' in recommendations.columns else 0
        
        # If still empty, just return the highest rated products in that category/usage
        if recommendations.empty:
            recommendations = temp_df.copy()
            recommendations['final_score'] = recommendations['rating'] / 5 if 'rating' in recommendations.columns else 0
            
        recommendations = recommendations.sort_values(by='final_score', ascending=False).head(top_n)
        
        return recommendations

    def recommend_routine(self, user_profile):
        """
        Generates a complete AM and PM CTM routine.
        """
        categories = ['Cleanser', 'Toner', 'Serum', 'Moisturizer']
        routine = {
            "AM": {},
            "PM": {}
        }
        
        for time in ["AM", "PM"]:
            for cat in categories:
                rec = self.recommend(user_profile, top_n=1, category=cat, usage=time)
                if not rec.empty:
                    product = rec.iloc[0]
                    routine[time][cat] = product.to_dict()
                    
        return routine

if __name__ == "__main__":
    from src.preprocessing import load_data, preprocess_dataframe
    from src.safety_filter import filter_by_safety
    
    df = load_data("data/skincare_products.csv")
    if df is not None:
        df = preprocess_dataframe(df)
        recommender = SkincareRecommender(df)
        
        # Test with Acne
        print("Testing for Acne:")
        recs = recommender.recommend({"skin_type": "oily", "concern": "acne"}, top_n=2)
        print(recs[['product_name', 'similarity_score']])
        
        # Test with Hydration
        print("\nTesting for Hydration:")
        recs = recommender.recommend({"skin_type": "dry", "concern": "hydration"}, top_n=2)
        print(recs[['product_name', 'similarity_score']])
