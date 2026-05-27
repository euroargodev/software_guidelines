import requests
import json
import os
from argparse import ArgumentParser
from pathlib import Path

# =====================
# CONFIGURATION
# =====================
TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

QUERY = """
query($projectId: ID!) {
  node(id: $projectId) {
    ... on ProjectV2 {
      items(last: 70) {
        nodes {
          id
          content {
            ... on Issue {
              title
              url
              body
              state              
              assignees(first: 10) {
                nodes {
                  login
                }
              }
            }
          }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                field {
                  ... on ProjectV2SingleSelectField {
                    name
                  }
                }
                name
                id
              }
              ... on ProjectV2ItemFieldLabelValue {
                labels(first: 20) {
                  nodes {
                    id
                    name
                  }
                }
              }
              ... on ProjectV2ItemFieldTextValue {
                text
                id
                updatedAt
                creator {
                  url
                }
              }
              ... on ProjectV2ItemFieldMilestoneValue {
                milestone {
                  id
                }
              }
              ... on ProjectV2ItemFieldRepositoryValue {
                repository {
                  id
                  url
                }
              }
            }
          }
        }
      }
    }
  }
}
"""

def run_query(query, variables):
    url = "https://api.github.com/graphql"
    response = requests.post(url, headers=HEADERS, json={"query": query, "variables": variables})
    response.raise_for_status()
    responsj = response.json()

    # Filter out issues with state == "CLOSED"
    keep = []
    items = responsj["data"]["node"]["items"]["nodes"]
    for item in items:
        content = item.get("content")
        if content and content.get("state") != "CLOSED":
            keep.append(item)

    return keep

if __name__ == "__main__":
    default_output = Path(str(Path(__file__).parent).replace('src', 'docs')).joinpath('sil_last.json')

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="OUTPUT_FILE", default=default_output,
                        help="write guidelines to FILE", metavar="FILE")
    args = parser.parse_args()

    variables = {"projectId": "PVT_kwDOA3TSm84BYfNs",
                 "itemsCursor": None}

    result = run_query(QUERY, variables)
    with open(args.OUTPUT_FILE, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"Data saved in: {args.OUTPUT_FILE}")