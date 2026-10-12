import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

df = pd.read_csv("students_week5.csv")
X = df.drop(columns=["student_id", "final_score", "result", "performance"])
y = df["result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

prob = model.predict_proba(X_test)[:, 1]
for threshold in [0.5, 0.3, 0.7]:
    pred = (prob >= threshold).astype(int)
    print(
        f"threshold={threshold}: precision={precision_score(y_test, pred):.2f}"
        f" recall={recall_score(y_test, pred):.2f} f1={f1_score(y_test, pred):.2f}"
    )

print(confusion_matrix(y_test, (prob >= 0.5).astype(int)))
print("ROC-AUC:", round(roc_auc_score(y_test, prob), 3))
