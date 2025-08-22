# Movie Ratings Analysis and Visualization
# Tools: Pandas, NumPy, Matplotlib, Seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
# Replace 'movies.csv' with your dataset filename
df = pd.read_csv("movies.csv")

# Show first few rows
print("\n--- First 5 Rows of Dataset ---")
print(df.head())

# -------------------------------
# 2. Data Cleaning
# -------------------------------
print("\n--- Cleaning Data ---")
df.dropna(inplace=True)           # Remove missing values
df.drop_duplicates(inplace=True)  # Remove duplicate rows
print("Remaining rows:", len(df))

# -------------------------------
# 3. Summary Statistics
# -------------------------------
print("\n--- Summary Statistics ---")
print("Mean rating:", df['rating'].mean())
print("Median rating:", df['rating'].median())
print("Mode rating:", df['rating'].mode()[0])

# -------------------------------
# 4. Visualizations
# -------------------------------

# Histogram of ratings
plt.figure(figsize=(6,4))
sns.histplot(df['rating'], bins=10, kde=True, color="skyblue")
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Boxplot of ratings
plt.figure(figsize=(6,4))
sns.boxplot(x=df['rating'], color="lightgreen")
plt.title("Boxplot of Movie Ratings")
plt.xlabel("Rating")
plt.show()

# Average rating by genre
plt.figure(figsize=(8,5))
genre_ratings = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
sns.barplot(x=genre_ratings.index, y=genre_ratings.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.show()

# -------------------------------
# 5. Top Rated Movies
# -------------------------------
print("\n--- Top 10 Movies by Rating ---")
top_movies = df.sort_values(by='rating', ascending=False).head(10)
print(top_movies[['title', 'genre', 'rating']])

# -------------------------------
# 6. Mini Dashboard
# -------------------------------
plt.figure(figsize=(12,6))

# Subplot 1 - Histogram
plt.subplot(1,2,1)
sns.histplot(df['rating'], bins=10, kde=True, color="coral")
plt.title("Rating Distribution")

# Subplot 2 - Avg rating by genre
plt.subplot(1,2,2)
sns.barplot(x=genre_ratings.index, y=genre_ratings.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Avg Rating by Genre")

plt.tight_layout()
plt.show()
