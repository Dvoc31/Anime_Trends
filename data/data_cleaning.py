import pandas as pd

# Load raw data
df = pd.read_csv(r"D:\practice\raw_anime_data.csv")

# Remove duplicates + rows without important info
df.drop_duplicates(subset="mal_id", inplace=True)
df = df.dropna(subset=["title", "score", "episodes"])

# Extract year
df["year"] = pd.to_datetime(df["aired.from"], errors="coerce").dt.year

# Fill episodes (missing → 0)
df["episodes"] = df["episodes"].fillna(0).astype(int)

# Keep only simple useful columns
df_clean = df[["mal_id", "title", "score", "episodes", "year", "season", "type", "rating","source"]]

# Save cleaned data
df_clean.to_csv(r"D:\practice\cleaned_anime_data.csv", index=False)

