import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score

df = pd.read_csv("students_week5.csv")
X = df.drop(columns=["student_id", "final_score", "result", "performance"])
y = (df["performance"] == 2).astype(int)
print("Share of High performers:", round(y.mean(), 2))
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    "Dummy (always 0)": DummyClassifier(strategy="most_frequent"),
    "Logistic": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "logistic balanced": make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=1000, class_weight="balanced")
    ),
}

for name, m in models.items():
    pred = m.fit(X_train, y_train).predict(X_test)
    print(
        f"{name:18s} acc={accuracy_score(y_test, pred):.2f}"
        f" recall={recall_score(y_test, pred):.2f} f1={f1_score(y_test, pred):.2f}"
    )
