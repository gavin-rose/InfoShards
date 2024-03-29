"""Firebase Functions for InfoShards"""

import json  # type: ignore[import-untyped]
import requests  # type: ignore[import-untyped]
from firebase_functions import https_fn  # type: ignore[import-untyped]
from firebase_admin import initialize_app  # type: ignore[import-untyped]

initialize_app()


@https_fn.on_call()
def get_data(req: https_fn.CallableRequest):
    """Get JSON data from URL."""
    link = req.data["link"]
    url = f"https://storage.googleapis.com/infoshards.appspot.com/public{link}.json"
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        return response.text
    return {"error": "something went wrong", "response": response}


@https_fn.on_call()
def search_shards(req: https_fn.CallableRequest):
    """Search for files based on query."""
    query = req.data["query"]
    url = "https://storage.googleapis.com/infoshards.appspot.com/queryable.json"
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        matches = []
        data = json.loads(response.text)
        for item in data.items():
            if query.lower() in item[1]["queryable"].lower():
                matches.append(
                    {"title": item[1]["title"], "filepath": item[1]["filepath"]}
                )
        return {"results": matches}
    return {"error": "something went wrong", "response": response}
