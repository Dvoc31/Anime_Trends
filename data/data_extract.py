# scripts/extract_data.py
import requests
import pandas as pd

def fetch_anime_data(pages=5):
    base_url = "https://api.jikan.moe/v4/anime"
    anime_list = []

    for page in range(1, pages+1):
        response = requests.get(base_url, params={"page": page})
        if response.status_code == 200:
            data = response.json()
            anime_list.extend(data['data'])
        else:
            print(f"Failed to fetch page {page}")
    return anime_list

if __name__ == "__main__":
    anime_data = fetch_anime_data(10)  # fetch 10 pages
    df = pd.json_normalize(anime_data)
    df.to_csv("data/raw_anime_data.csv", index=False)
