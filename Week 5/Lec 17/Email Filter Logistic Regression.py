from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

file_path = Path(__file__).parent / "emails.csv"
df = pd.read_csv(file_path)

X = df.drop(columns=["spam"])
y = df["spam"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("=== Testing Different k Values for KNN ===")
best_k = 1
best_acc = 0

for k in [1, 3, 5, 7, 9, 11, 15, 21, 25]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test_scaled))
    if acc > best_acc:
        best_acc = acc
        best_k = k
    print(f"k = {k:>2}, Accuracy = {acc:.4f} ({acc * 100:.2f}%)")

print("---------------------------------------------------------")
print(f"Optimal k = {best_k} with Highest Accuracy: {best_acc:.4f} ({best_acc * 100:.2f}%)")
print("---------------------------------------------------------")

best_model = KNeighborsClassifier(n_neighbors=best_k)
best_model.fit(X_train_scaled, y_train)
pred = best_model.predict(X_test_scaled)

print("\nConfusion Matrix (Optimal k):")
print(confusion_matrix(y_test, pred))

print("\nClassification Report (Optimal k):")
print(classification_report(y_test, pred, target_names=["Not Spam (Ham)", "Spam"]))

sample_email = X_test_scaled[[0]]
actual_label = "Spam" if y_test.iloc[0] == 1 else "Not Spam (Ham)"
pred_label = "Spam" if pred[0] == 1 else "Not Spam (Ham)"
prob = best_model.predict_proba(sample_email)[0][1]

print(f"Sample Email - Actual: {actual_label} | Predicted: {pred_label}")
print(f"Spam Probability: {prob:.2%}")