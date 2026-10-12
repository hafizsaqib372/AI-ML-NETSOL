from pathlib import Path
import seaborn as sns
from statistics import mode
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
import pandas as pd
import numpy as np

df = sns.load_dataset("Books_Data_Clean", data_home=Path(__file__).parent)

print(df.shape)

print("------------------")

# which cols have missing values and how many are missing in each
print(df.isnull().sum())

print("------------------")

print(df["Book_average_rating"].mean())

print("------------------")

print(df["gross sales"].sum())

print("------------------")

print(mode(df["genre"]))

print("------------------")

pubs = df.groupby("Publisher ")["units sold"].sum()
print(pubs.idxmax())

print("------------------")

corr = df[["gross sales", "publisher revenue"]].corr()
print(corr)

print("------------------")

print(df.sort_values("Publishing Year"))
# ==============================================================================
# ROUND 2 — PREPROCESSING CHALLENGE (25 min): Clean & Prepare the Data
# ==============================================================================

# ------------------------------------------------------------------------------
# Q1: Handle the missing values you found in Round 1 (Book Name, language_code, Publishing Year).
#     Decide a strategy for each column and justify it in a comment.
# ------------------------------------------------------------------------------

# 1. 'Book Name' (23 missing values):
# Strategy: Impute missing titles with 'Unknown'.
# Justification: 'Book Name' is an identifier / text attribute rather than a numeric metric.
# Filling missing titles with 'Unknown' preserves 23 valid rows of sales, ratings, and pricing
# data, preventing loss of valuable observation data during modeling and aggregate analysis.
df["Book Name"] = df["Book Name"].fillna("Unknown")

# 2. 'language_code' (53 missing values):
# Strategy: Impute missing language codes with the mode ('eng').
# Justification: 'language_code' is a categorical variable where English ('eng') is overwhelmingly
# the most frequent category (> 90% combined English). Mode imputation is the standard and most
# statistically sound strategy for categorical columns with a clear dominant class.
mode_language = df["language_code"].mode()[0]
df["language_code"] = df["language_code"].fillna(mode_language)

# 3. 'Publishing Year' (1 missing value):
# Strategy: Impute with the median publishing year (2003.0).
# Justification: 'Publishing Year' contains extreme negative outliers (e.g., historical classical works
# dating back to -560), which artificially skews the mean down to 1971.4. The median (2003.0) is
# robust against outliers and represents the typical modern publication year in this dataset.
median_year = df["Publishing Year"].median()
df["Publishing Year"] = df["Publishing Year"].fillna(median_year)

print("\n--- Q1: Missing Values After Cleaning ---")
print(df[["Book Name", "language_code", "Publishing Year"]].isnull().sum())
print("------------------")

# ------------------------------------------------------------------------------
# Q2: The 'genre' column has 4 categories. Apply One-Hot Encoding to it and print the result.
# ------------------------------------------------------------------------------
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
encoded_genre = encoder.fit_transform(df[["genre"]])

# Represent as a clean DataFrame with column names
encoded_genre_df = pd.DataFrame(
    encoded_genre, columns=encoder.get_feature_names_out(["genre"]), index=df.index
)

print("\n--- Q2: One-Hot Encoded Genre (First 5 Rows) ---")
print(encoded_genre_df.head())
print("Encoded Matrix Shape:", encoded_genre.shape)
print("------------------")

# ------------------------------------------------------------------------------
# Q3: The 'Author_Rating' column has a natural order: Novice < Intermediate < Excellent < Famous.
#     Apply Label Encoding so the numbers respect this order.
# ------------------------------------------------------------------------------
le = LabelEncoder()
df["Author_Rating"] = df["Author_Rating"].str.replace("*", "", regex=False).str.strip()
# Set classes_ in strict ascending order so: Novice=0, Intermediate=1, Excellent=2, Famous=3
le.classes_ = np.array(["Novice", "Intermediate", "Excellent", "Famous"])
df["Author_Rating"] = le.transform(df["Author_Rating"])

print("\n--- Q3: Ordered Label Encoded Author_Rating (First 10 Rows) ---")
print(df["Author_Rating"].head(10))
print("Class mapping: Novice: 0, Intermediate: 1, Excellent: 2, Famous: 3")
print("Value counts after encoding:\n", df["Author_Rating"].value_counts().sort_index())
print("------------------")

# ------------------------------------------------------------------------------
# Q4: Check the skewness of 'gross sales' using .skew().
#     Apply a log transform (np.log) and check the skewness again — did it improve?
# ------------------------------------------------------------------------------
skew_before = df["gross sales"].skew()
df["gross_sales_log"] = np.log(df["gross sales"])
skew_after = df["gross_sales_log"].skew()

print("\n--- Q4: Skewness of 'gross sales' ---")
print(f"Skewness before log transform : {skew_before:.4f}")
print(f"Skewness after log transform  : {skew_after:.4f}")
print(
    "Did it improve? Yes! The original distribution was heavily right-skewed (skew = 5.9325)."
)
print(
    "After log transformation, skewness dropped to 0.4818, which is within [-0.5, 0.5], indicating an approximately symmetric distribution."
)
print("------------------")

# ------------------------------------------------------------------------------
# Q5: Apply StandardScaler to the 'units sold' column.
#     Confirm the transformed mean is approximately 0.
# ------------------------------------------------------------------------------
scaler = StandardScaler()
df["units_sold_scaled"] = scaler.fit_transform(df[["units sold"]])

transformed_mean = df["units_sold_scaled"].mean()
transformed_std = df["units_sold_scaled"].std()

print("\n--- Q5: StandardScaler on 'units sold' ---")
print(f"Transformed Mean               : {transformed_mean:.10e}")
print(f"Is mean approximately 0?       : {np.isclose(transformed_mean, 0)}")
print(f"Transformed Standard Deviation : {transformed_std:.4f}")
print("------------------")
