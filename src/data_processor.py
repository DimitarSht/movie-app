from typing import List, Dict

def format_data(results: List[Dict]) -> List[Dict]:
    formatted = []
    for item in results:
        title = item.get("title") or item.get("name")
        rating = item.get("vote_average")
        if title and rating is not None:
            formatted.append({"title": title, "rating": rating})
    return sorted(formatted, key=lambda x: x["rating"], reverse=True)