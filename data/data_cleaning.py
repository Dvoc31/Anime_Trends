import pandas as pd
import ast
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Load raw data
df = pd.read_csv("data/raw_anime_data.csv")

# Remove duplicates + rows without critical info
df.drop_duplicates(subset="mal_id", inplace=True)
df = df.dropna(subset=["title", "score", "genres", "studios"])

# Extract year and season
df["year"] = pd.to_datetime(df["aired.from"], errors="coerce").dt.year
df["season"] = df["season"].str.title()

# Clean genre_list properly
def clean_genres(x):
    try:
        lst = ast.literal_eval(x)  # string to list of dicts
        return [g['name'] for g in lst]  # extract only names
    except:
        return []

df["genre_list"] = df["genres"].apply(clean_genres)

# Optional: Clean studios similarly
def clean_studios(x):
    try:
        lst = ast.literal_eval(x)
        return [s['name'] for s in lst]
    except:
        return []

df["studios"] = df["studios"].apply(clean_studios)

# Episodes: fill NaN with 0 and convert to int
df["episodes"] = df["episodes"].fillna(0).astype(int)

# Keep only useful columns
df_clean = df[["mal_id", "title", "score", "genre_list", "studios",
               "episodes", "source", "season", "year", "type", "rating"]]

# Save cleaned data as JSON + CSV
df_clean.to_csv("data/cleaned_anime_data.csv", index=False)
df_clean.to_json("data/cleaned_anime_data.json", orient="records", force_ascii=False)

print("✅ Data cleaned and saved as cleaned_anime_data.csv & .json")
