import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
# 1. LOAD DATA

df = pd.read_csv("loan_approval_dataset.csv")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()
print(df.columns.tolist())

print(df.head())
print(df.info())

# 2. CHECK MISSING VALUES

print("\nMissing values:")
print(df.isnull().sum())

# 3. CLEAN STRING VALUES

df["education"] = df["education"].str.strip()
df["self_employed"] = df["self_employed"].str.strip()
df["loan_status"] = df["loan_status"].str.strip()

# Check actual target values
print("\nLoan status values:")
print(df["loan_status"].unique())


# 5. ENCODE CATEGORICAL FEATURES

df = pd.get_dummies(
    df,
    columns=["education", "self_employed"],
    drop_first=True
)

# 6. ENCODE TARGET

df["loan_status"] = df["loan_status"].map({
    "Approved": 1,
    "Rejected": 0
})

print("\nMissing values in loan_status:")
print(df["loan_status"].isnull().sum())

df.to_csv("loan_approval_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")


# 7. SEPARATE FEATURES AND TARGET

X = df.drop(columns=["loan_id","loan_status"])

y = df["loan_status"]


# 8. TRAIN-TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 9. CREATE DECISION TREE

model = DecisionTreeClassifier(
    random_state=42
)

# 10. TRAIN MODEL

model.fit(X_train, y_train)

# 11. MAKE PREDICTIONS

y_pred = model.predict(X_test)

# 12. EVALUATE MODEL

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))