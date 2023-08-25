from argparse import ArgumentParser
import os
import sys

from .api_client import HypothesisClient

parser = ArgumentParser(description="Bulk annotation deletion script. Use with care!")
parser.add_argument("url", help="Document URL")
parser.add_argument("group", help="Group ID")
parser.add_argument(
    "--endpoint", help="Hypothesis API endpoint", default="https://hypothes.is/api"
)
args = parser.parse_args()

access_token = os.getenv("HYPOTHESIS_ACCESS_TOKEN")
if access_token is None:
    print("HYPOTHESIS_ACCESS_TOKEN env var not set", file=sys.stderr)
    sys.exit(1)

client = HypothesisClient(args.endpoint, access_token)

anns = client.search(url=args.url, group=args.group)
ids = [ann["id"] for ann in anns]
if not ids:
    print("No matching annotations found.")
    sys.exit(0)

print(f"Found {len(ids)} matching annotations. Delete these?")
ok = input()

if ok.lower() not in ["y", "yes", "1"]:
    print("Deletion skipped")
    sys.exit(0)

client.delete(ids)
