from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

file_path = Path(__file__).parent / "emails.csv"
df = pd.read_csv(file_path)

X = df.drop(columns=["spam"])
y = df["spam"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = GaussianNB()
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print("=== Gaussian Naive Bayes Results ===")
print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))
print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=["Not Spam (Ham)", "Spam"]))

sample_email = X_test.iloc[[0]]
actual_label = "Spam" if y_test.iloc[0] == 1 else "Not Spam (Ham)"
pred_label = "Spam" if pred[0] == 1 else "Not Spam (Ham)"
spam_prob = model.predict_proba(sample_email)[0][1]

print(f"Sample Email - Actual: {actual_label} | Predicted: {pred_label}")
print(f"Spam Probability: {spam_prob:.2%}")