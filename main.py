import sys
import requests
from output_writer import *
from data_processor import *
from typing import List, Dict
from api_client import *

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <tv|movies|all> <day|week> <csv|json>", file=sys.stderr)
        sys.exit(1)

    media_type, time_window, output_format = sys.argv[1:]
    if media_type not in {"tv", "movies", "all"} or time_window not in {"day", "week"} or output_format not in {"csv", "json"}:
        print("Invalid arguments", file=sys.stderr)
        sys.exit(1)

    with requests.get(f"{BASE_URL}/{media_type}/{time_window}", headers=HEADERS) as session:
        results = []

        if media_type == "all":
            tv_data = fetch_trending("tv", time_window)
            movie_data = fetch_trending("movie", time_window)
            results = tv_data + movie_data
        else:
            media_type_api = "tv" if media_type == "tv" else "movie"
            results = fetch_trending(media_type_api, time_window)

        formatted_results = format_data(results)

        if output_format == "csv":
            output_csv(formatted_results)
        else:
            output_json(formatted_results)

if __name__ == "__main__":
    main()
