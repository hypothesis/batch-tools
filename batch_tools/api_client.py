import requests


class HypothesisClient:
    """
    Hypothesis API client.
    """

    def __init__(self, endpoint: str, access_token: str):
        """
        :param endpoint: Hypothesis API endpoint
        :param api_key: Hypothesis API token
        """
        self.endpoint = endpoint
        self.access_token = access_token

    def search(self, **query):
        """Search for annotations."""

        anns = []
        search_after = ""
        page_size = 200
        total = None

        while True:
            rsp = requests.get(
                f"{self.endpoint}/search",
                headers={"Authorization": f"Bearer {self.access_token}"},
                params={
                    # General search args
                    "search_after": search_after,
                    "sort": "id",
                    "order": "asc",
                    "limit": page_size,
                    # Annotation filter
                    **query,
                },
            )
            rsp.raise_for_status()
            body = rsp.json()
            if total is None:
                total = body["total"]

            if body["rows"]:
                page_start = len(anns) + 1
                page_end = len(anns) + len(body["rows"])
                print(f"Fetched annotations {page_start}..{page_end} out of {total}")

            page_anns = body["rows"]
            if not page_anns:
                break
            for ann in page_anns:
                anns.append(ann)
            search_after = anns[-1]["id"]

        return anns

    def delete(self, ids):
        """Delete annotations."""

        for idx, id_ in enumerate(ids):
            print(f"Deleting annotation {id_} ({idx+1} of {len(ids)})")
            delete_rsp = requests.delete(
                f"{self.endpoint}/annotations/{id_}",
                headers={"Authorization": f"Bearer {self.access_token}"},
            )
            delete_rsp.raise_for_status()
