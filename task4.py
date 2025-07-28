import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# -------------------------------
# 1. Sample User-Item Ratings Data
# -------------------------------
data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item3', 'Item2', 'Item3', 'Item1'],
    'Rating': [5, 3, 4, 4, 5, 2, 4, 5]
}

df = pd.DataFrame(data)

# -------------------------------
# 2. Create User-Item Matrix
# -------------------------------
ratings_matrix = df.pivot_table(index='User', columns='Item', values='Rating').fillna(0)

# -------------------------------
# 3. Compute Cosine Similarity Between Users
# -------------------------------
similarity = cosine_similarity(ratings_matrix)
similarity_df = pd.DataFrame(similarity, index=ratings_matrix.index, columns=ratings_matrix.index)

print("User Similarity Matrix:")
print(similarity_df)

# -------------------------------
# 4. Recommend Items to a User
# -------------------------------
def recommend_items(user_id, top_n=2):
    # Get similarity scores for the target user
    sim_scores = similarity_df[user_id].drop(user_id)
    
    # Weighted sum of ratings from similar users
    similar_users = sim_scores.sort_values(ascending=False)
    weighted_ratings = pd.Series(dtype=float)
    
    for sim_user, score in similar_users.items():
        user_ratings = ratings_matrix.loc[sim_user]
        weighted_ratings = weighted_ratings.add(user_ratings * score, fill_value=0)
    
    # Remove already rated items
    already_rated = ratings_matrix.loc[user_id][ratings_matrix.loc[user_id] > 0].index
    weighted_ratings = weighted_ratings.drop(already_rated, errors='ignore')
    
    # Recommend top N items
    recommendations = weighted_ratings.sort_values(ascending=False).head(top_n)
    return recommendations

# Example: Recommend for user 'C'
print("\nRecommended Items for User C:")
print(recommend_items('C'))
