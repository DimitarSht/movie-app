import requests
import sys
from typing import List, Dict

BASE_URL = "https://api.themoviedb.org/3/trending"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZDVhNDU4YzljZmMxODdjZThlMDdhM2ZiYTU1MjE0YyIsInN1YiI6IjY1NzRkNzA2ZTkzZTk1MDExZDRlMmM2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MsO7CO9573rr8rTEczZJ4PW6dnVX9xuU2OUNOcaHEts"  # Replace with your actual token
}

def fetch_trending(media_type: str, time_window: str) -> List[Dict]:
    url = f"{BASE_URL}/{media_type}/{time_window}"
    with requests.get(url, headers=HEADERS) as response:
        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        else:
            print(f"Failed to fetch {media_type} data: {response.status}", file=sys.stderr)
            return []
