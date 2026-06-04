import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.train_model import load_trained_model, build_feature_text


class SkincareRecommender:
    def __init__(self, df, artifact=None):
        self.df = df.reset_index(drop=True)
        self.vectorizer = None
        self.tfidf_matrix = None

        if artifact is not None:
            self._load_from_artifact(artifact)
        else:
            persisted = load_trained_model()
            if persisted is not None and len(persisted.get("df", [])) >= len(self.df) * 0.9:
                self._load_from_artifact(persisted)
            else:
                self._fit()

    def _load_from_artifact(self, artifact):
        self.vectorizer = artifact["vectorizer"]
        self.tfidf_matrix = artifact["tfidf_matrix"]
        stored_df = artifact["df"].reset_index(drop=True)
        if len(stored_df) == len(self.df):
            self.df = stored_df
        else:
            self.df["feature_text"] = self.df.apply(build_feature_text, axis=1)
            self.tfidf_matrix = self.vectorizer.transform(self.df["feature_text"])

    def _fit(self):
        self.df["feature_text"] = self.df.apply(build_feature_text, axis=1)
        self.vectorizer = TfidfVectorizer(
            token_pattern=r"(?u)\b[a-z][a-z0-9+\-]*\b",
            ngram_range=(1, 2),
            max_features=15000,
            min_df=1,
            max_df=0.95,
            sublinear_tf=True,
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["feature_text"])

    def recommend(self, user_profile, top_n=5, category=None, usage=None):
        temp_df = self.df.copy()

        if category:
            temp_df = temp_df[temp_df['category'].str.lower() == category.lower()]

        if usage:
            temp_df = temp_df[temp_df['usage'].str.lower().isin([usage.lower(), 'both'])]

        if temp_df.empty:
            return pd.DataFrame()

        concerns = user_profile['concern'].split(',')
        weighted_concern = ", ".join([c.strip() for c in concerns] * 2)
        query = f"{user_profile['skin_type']}, {weighted_concern}, {category if category else ''}"
        query_vector = self.vectorizer.transform([query.lower()])

        filtered_indices = temp_df.index
        similarities = cosine_similarity(
            query_vector, self.tfidf_matrix[filtered_indices]
        ).flatten()

        temp_df = temp_df.copy()
        temp_df['similarity_score'] = similarities

        if 'rating' in temp_df.columns:
            temp_df['final_score'] = (0.7 * temp_df['similarity_score']) + (0.3 * (temp_df['rating'] / 5))
        else:
            temp_df['final_score'] = temp_df['similarity_score']

        recommendations = temp_df[temp_df['similarity_score'] > 0]

        if recommendations.empty:
            recommendations = temp_df[
                temp_df['skin_type'].str.contains(user_profile['skin_type'], case=False, na=False)
            ]
            if not recommendations.empty:
                recommendations = recommendations.copy()
                recommendations['final_score'] = (
                    recommendations['rating'] / 5 if 'rating' in recommendations.columns else 0
                )

        if recommendations.empty:
            recommendations = temp_df.copy()
            recommendations['final_score'] = (
                recommendations['rating'] / 5 if 'rating' in recommendations.columns else 0
            )

        return recommendations.sort_values(by='final_score', ascending=False).head(top_n)

    def recommend_routine(self, user_profile):
        am_categories = ['Cleanser', 'Treatment', 'Moisturizer', 'Sunscreen']
        pm_categories = ['Cleanser', 'Treatment', 'Eye cream', 'Moisturizer']

        routine = {"AM": {}, "PM": {}}

        for cat in am_categories:
            rec = self.recommend(user_profile, top_n=1, category=cat, usage='AM')
            if not rec.empty:
                routine["AM"][cat] = rec.iloc[0].to_dict()

        for cat in pm_categories:
            rec = self.recommend(user_profile, top_n=1, category=cat, usage='PM')
            if not rec.empty:
                routine["PM"][cat] = rec.iloc[0].to_dict()

        return routine
