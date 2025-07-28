# RECOMMENDATION-SYSTEM

COMPANY: CODTECH IT SOLUTIONS

NAME: SAKSHAM SHRIVASTAVA

INTERN ID: CT04DZ534

DOMAIN: MACHINE LEARNING

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH

Task 4 – Recommendation System using Machine Learning
In this task, we have built a basic Recommendation System using the Collaborative Filtering technique with Python’s pandas and scikit-learn libraries. The goal is to recommend relevant items to a user based on the preferences and ratings given by other similar users. This system is particularly useful in real-world applications such as movie recommendations (Netflix), product suggestions (Amazon), or music preferences (Spotify).

The core idea behind collaborative filtering is that users with similar tastes in the past will likely agree again in the future. There are two primary types of collaborative filtering: user-based and item-based. In this project, we implemented user-based collaborative filtering using cosine similarity to measure how similar one user is to others.

We began by creating a sample dataset consisting of users, items, and the ratings they gave to those items. This dataset was converted into a user-item matrix, where rows represent users, columns represent items, and values are the corresponding ratings. Missing values (i.e., items not yet rated by a user) were filled with zeros to prepare the matrix for similarity calculation.

To determine which users are similar, we used the cosine similarity metric. Cosine similarity is a mathematical measure that calculates the cosine of the angle between two vectors — in this case, the vectors represent the ratings each user has given across various items. A similarity score close to 1 means the users are highly similar, whereas a score closer to 0 indicates low similarity.

Once we had the similarity matrix, we could generate recommendations. For a selected user (say, User C), we identified other users with high similarity scores. We then aggregated the ratings of those similar users to generate a weighted score for the items that User C hasn't rated yet. These scores act as predicted ratings, and the top-rated items among them are recommended.

For example, if User C has not rated Item1, but other users similar to C (like User A and User B) have rated it highly, then Item1 will likely be recommended to User C.

The system is implemented without using any external recommendation libraries like scikit-surprise, making it lightweight and highly customizable. This approach is ideal for learning purposes and can be extended to larger datasets by incorporating additional optimizations such as normalization, thresholding, and performance tuning.

Finally, the results are displayed clearly: we print a User Similarity Matrix and show the top-N recommended items for a selected user. This provides a transparent view of how recommendations are made and how user similarities influence them.

In conclusion, this project demonstrates a simple yet powerful recommendation engine using Python’s core libraries. It introduces the concept of collaborative filtering, vector similarity, and rating prediction without complex dependencies, making it a strong foundational step for more advanced recommendation systems in real-world applications.

OUTPUT 

<img width="1693" height="322" alt="image" src="https://github.com/user-attachments/assets/1686f068-5bfe-483e-a205-306ef7f75f24" />
