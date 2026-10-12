# Step 1: Extract

import requests
import pandas as pd

url = "https://api.github.com/search/repositories"

params = {
    "q": "language:python created:>2025-05-26",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

response = requests.get(url, params=params)
data = response.json()

print(response.status_code)
print(data.keys())

print("Total matches on GitHub:", data['total_count'])
print("Repos returned:", len(data['items']))

first_repo = data['items'][0]
print("\nFirst repo name:", first_repo['name'])
print("Stars:", first_repo['stargazers_count'])
print("Language:", first_repo['language'])
print("URL:", first_repo['html_url'])

# Step 2: Transform

repos = []

for repo in data['items']:
    repos.append({
        "name": repo['name'],
        "owner": repo['owner']['login'],
        "stars": repo['stargazers_count'],
        "forks": repo['forks_count'],
        "language": repo['language'],
        "description": repo['description'],
        "url": repo['html_url'],
        "created_at": repo['created_at']
    })

df = pd.DataFrame(repos)
print(df.head())

# Drop rows where description is missing
df_clean = df.dropna(subset=['description'])

# Add a viral flag for repos with over 50k stars
df_clean = df_clean.copy()
df_clean['viral'] = df_clean['stars'].apply(lambda x: 'Yes' if x > 50000 else 'No')

# Sort by stars descending
df_clean = df_clean.sort_values('stars', ascending=False).reset_index(drop=True)

print("Before cleaning:", len(df))
print("After cleaning:", len(df_clean))

# Step 3: Load

df_clean.to_csv('github_trending_repos.csv', index=False)

print("Pipeline complete. File saved.")
print(f"{len(df_clean)} repos loaded into github_trending_repos.csv")
