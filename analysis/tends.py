# Step 3: Anime Data Analysis & Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast



df = pd.read_csv("data/cleaned_anime_data.csv")

plt.style.use("seaborn-v0_8")
sns.set_palette("viridis")


# popular anime by genre
df['genre_list'] = df['genre_list'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])


df_exploded = df.explode('genre_list')


genre_counts = df_exploded['genre_list'].value_counts().head(15)

plt.figure(figsize=(12,6))
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title("Top 15 Most Popular Anime Genres")
plt.xlabel("Number of Anime")
plt.ylabel("Genre")
plt.show()

# -------------------------------------------------------------------------------------------------------------
# Studio-wise rating distribution
df['studios'] = df['studios'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

df_exploded = df.explode('studios')

studio_ratings = df_exploded.groupby("studios")["score"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=studio_ratings.values, y=studio_ratings.index)
plt.title("Top 10 Studios by Average Rating")
plt.xlabel("Average Score")
plt.ylabel("Studio")
plt.show()

# -------------------------------------------------------------------------------------------------------------
# Anime releases per season
plt.figure(figsize=(10,6))
sns.countplot(x="season", data=df, order=df["season"].value_counts().index)
plt.title("Number of Anime Released per Season")
plt.xlabel("Season")
plt.ylabel("Count")
plt.show()

# Avg rating per season
season_ratings = df.groupby("season")["score"].mean().sort_values()

plt.figure(figsize=(8,6))
sns.barplot(x=season_ratings.index, y=season_ratings.values)
plt.title("Average Ratings by Season")
plt.xlabel("Season")
plt.ylabel("Average Score")
plt.show()
# -------------------------------------------------------------------------------------------------------------

studio_counts = df.explode("studios")["studios"].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=studio_counts.values, y=studio_counts.index)
plt.title("Top 10 Studios by Number of Anime Produced")
plt.xlabel("Number of Anime")
plt.ylabel("Studio")
plt.show()


# -------------------------------------------------------------------------------------------------------------

# Short vs Long series
df["series_type"] = df["episodes"].apply(lambda x: "Short (<=24)" if x<=24 else "Long (>24)")
series_ratings = df.groupby("series_type")["score"].mean()

plt.figure(figsize=(8,6))
sns.barplot(x=series_ratings.index, y=series_ratings.values)
plt.title("Average Ratings: Short vs Long Series")
plt.xlabel("Series Type")
plt.ylabel("Average Score")
plt.show()

# --------------------------------------------------------------------------------------------------------------
# Ratings by source type
source_counts = df["source"].value_counts().head(6)

plt.figure(figsize=(8,6))
sns.barplot(x=source_counts.values, y=source_counts.index)
plt.title("Most Common Anime Source Types")
plt.xlabel("Number of Anime")
plt.ylabel("Source")
plt.show()

# Ratings by source
source_ratings = df.groupby("source")["score"].mean().sort_values(ascending=False).head(6)

plt.figure(figsize=(8,6))
sns.barplot(x=source_ratings.values, y=source_ratings.index)
plt.title("Average Ratings by Source Type")
plt.xlabel("Average Score")
plt.ylabel("Source")
plt.show()

# --------------------------------------------------------------------------------------------------------------
# tv and movies ratings

type_ratings = df.groupby("type")["score"].mean().sort_values(ascending=False).head(6)

plt.figure(figsize=(8,6))
sns.barplot(x=type_ratings.values, y=type_ratings.index)
plt.title("Average Ratings: TV vs Movies")
plt.xlabel("Average Score")
plt.ylabel("Type")
plt.show()

# --------------------------------------------------------------------------------------------------------------



