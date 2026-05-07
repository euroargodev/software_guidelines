import requests
import json
import os

# =====================
# CONFIGURATION
# =====================
TOKEN = os.getenv("GITHUB_TOKEN")
OUTPUT_FILE = "guidelines_vtest.json"

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
    return responsj['data']['node']['items']['nodes']

variables = {"projectId": "PVT_kwDOA3TSm84A81yH", "itemsCursor": None}
result = run_query(QUERY, variables)
with open(OUTPUT_FILE, 'w') as f:
    json.dump(result, f)
print(f"Data saved to {OUTPUT_FILE}")