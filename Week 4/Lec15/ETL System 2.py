import requests
import pandas as pd
from google.cloud import bigquery


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

response.raise_for_status()

data = response.json()

print("Data Extracted Successfully!")

# 2. TRANSFORM

df = pd.DataFrame(data)

# Extract city from nested address
df["city"] = df["address"].apply(lambda x: x["city"])

# Extract company name
df["company_name"] = df["company"].apply(lambda x: x["name"])

# Remove unnecessary nested columns
df = df.drop(columns=["address", "company"])

print("Data Transformed Successfully!")

print(df)


# 3. LOAD → BIGQUERY

# Google Cloud Project ID
PROJECT_ID = "buoyant-striker-510111-i2"

# BigQuery dataset name
DATASET_ID = "etl_dataset"

# BigQuery table name
TABLE_ID = "users"

# Full BigQuery table ID
table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"


# Create BigQuery client
client = bigquery.Client(project=PROJECT_ID)


# Create dataset if it doesn't exist
dataset_id = f"{PROJECT_ID}.{DATASET_ID}"

dataset = bigquery.Dataset(dataset_id)

dataset.location = "US"

try:
    client.get_dataset(dataset_id)
    print("Dataset already exists.")

except Exception:
    client.create_dataset(dataset)
    print("Dataset created successfully!")


# Upload DataFrame to BigQuery
job = client.load_table_from_dataframe(
    df,
    table_id
)

# Wait for upload to finish
job.result()

print("Data Loaded Successfully into BigQuery!")

print(f"BigQuery Table: {table_id}")