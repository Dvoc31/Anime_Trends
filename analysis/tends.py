
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_anime_data.csv")

plt.style.use("seaborn-v0_8")
sns.set_palette("viridis")

# -----------------------------
# 1. Anime Released per Season
season_counts = df["season"].value_counts()
plt.figure(figsize=(10,6))
sns.countplot(x="season", data=df, order=season_counts.index)
plt.title("Number of Anime Released per Season")
plt.xlabel("Season")
plt.ylabel("Count")
plt.show()

print("Insight: Seasons with highest releases:", season_counts.idxmax())

# -----------------------------
# 2. Average Ratings by Season
season_ratings = df.groupby("season")["score"].mean()
plt.figure(figsize=(8,6))
sns.barplot(x=season_ratings.index, y=season_ratings.values)
plt.title("Average Ratings by Season")
plt.xlabel("Season")
plt.ylabel("Average Score")
plt.show()

print("Insight: Season with highest average rating:", season_ratings.idxmax())

# -----------------------------
# 3. Short vs Long Series
df["series_type"] = df["episodes"].apply(lambda x: "Short (<=24)" if x<=24 else "Long (>24)")
series_ratings = df.groupby("series_type")["score"].mean()
plt.figure(figsize=(8,6))
sns.barplot(x=series_ratings.index, y=series_ratings.values)
plt.title("Average Ratings: Short vs Long Series")
plt.xlabel("Series Type")
plt.ylabel("Average Score")
plt.show()

best_series_type = series_ratings.idxmax()
print(f"Insight: {best_series_type} series have higher average ratings.")

# -----------------------------
# 4. Most Common Anime Source Types
source_counts = df["source"].value_counts().head(6)
plt.figure(figsize=(8,6))
sns.barplot(x=source_counts.values, y=source_counts.index)
plt.title("Most Common Anime Source Types")
plt.xlabel("Number of Anime")
plt.ylabel("Source")
plt.show()

print("Insight: Most common source type is:", source_counts.idxmax())

# -----------------------------
# 5. Average Ratings by Source Type
source_ratings = df.groupby("source")["score"].mean().sort_values(ascending=False).head(6)
plt.figure(figsize=(8,6))
sns.barplot(x=source_ratings.values, y=source_ratings.index)
plt.title("Average Ratings by Source Type")
plt.xlabel("Average Score")
plt.ylabel("Source")
plt.show()

print("Insight: Source type with highest average rating:", source_ratings.idxmax())

# -----------------------------
# 6. Average Ratings: TV vs Movies
type_ratings = df.groupby("type")["score"].mean().sort_values(ascending=False)
plt.figure(figsize=(8,6))
sns.barplot(x=type_ratings.values, y=type_ratings.index)
plt.title("Average Ratings: TV vs Movies")
plt.xlabel("Average Score")
plt.ylabel("Type")
plt.show()

print("Insight: Highest rated type is:", type_ratings.idxmax())
