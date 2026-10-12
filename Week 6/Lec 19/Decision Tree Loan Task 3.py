from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df = pd.read_csv('loan_data_set.csv')
df.columns = df.columns.str.strip()

df = df.drop(columns=["loan_id"])

y = (df["loan_status"].str.strip() == "Approved").astype(int)
X_raw = df.drop(columns=["loan_status"])

X = pd.get_dummies(X_raw, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\n=== Evaluating Decision Tree at Different Depths ===")
for depth in [3, 5, 7, 10, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    train_acc = tree.score(X_train, y_train)
    test_acc = tree.score(X_test, y_test)
    depth_name = f"max_depth={depth}" if depth is not None else "max_depth=None (Full)"
    print(
        f"{depth_name:<22}: Train = {train_acc * 100:.2f}% | Test = {test_acc * 100:.2f}%"
    )

model = DecisionTreeClassifier(max_depth=None, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print("\n" + "-" * 55)
print(f"      DECISION TREE FINAL ACCURACY: {accuracy * 100:.2f}%")
print("-" * 55)

print(confusion_matrix(y_test, pred))

print("\nClassification Report:")
print(
    classification_report(y_test, pred, target_names=["Rejected (0)", "Approved (1)"])
)

importance = pd.Series(model.feature_importances_, index=X.columns)
top_features = importance[importance > 0].sort_values(ascending=False)
print("Top Decision Features (Importance > 0):")
print(top_features.round(4))

print("\n=== Decision Tree Logic (Top Rules) ===")
small_tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print(export_text(small_tree, feature_names=list(X.columns)))

print("\n" + "-" * 55)
print("ENTER LOAN DETAILS FOR PREDICTION")
print("-" * 55)

dependents = int(input("Number of dependents: "))
education = input("Education (Graduate / Not Graduate): ").strip().lower()
self_employed = input("Self employed (Yes / No): ").strip().lower()
income = float(input("Annual income: "))
loan_amt = float(input("Loan amount: "))
term = int(input("Loan term (years): "))
cibil = int(input("CIBIL score (300-900): "))
res_assets = float(input("Residential assets value: "))
comm_assets = float(input("Commercial assets value: "))
lux_assets = float(input("Luxury assets value: "))
bank_assets = float(input("Bank asset value: "))

user_df = pd.DataFrame([{
    "no_of_dependents": dependents,
    "income_annum": income,
    "loan_amount": loan_amt,
    "loan_term": term,
    "cibil_score": cibil,
    "residential_assets_value": res_assets,
    "commercial_assets_value": comm_assets,
    "luxury_assets_value": lux_assets,
    "bank_asset_value": bank_assets,
    "education_ Not Graduate": 1 if "not" in education else 0,
    "self_employed_ Yes": 1 if "yes" in self_employed else 0,
}])

user_pred = model.predict(user_df)[0]
user_prob = model.predict_proba(user_df)[0]

print("-" * 55)
if user_pred == 1:
    print(f"Loan Status: APPROVED (Confidence: {user_prob[1] * 100:.2f}%)")
else:
    print(f"Loan Status: REJECTED (Confidence: {user_prob[0] * 100:.2f}%)")
print("-" * 55)

