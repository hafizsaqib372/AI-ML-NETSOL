import pandas as pd
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV,
    StratifiedKFold,
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("students_week5.csv")
X = df.drop(columns=["student_id", "final_score", "result", "performance"])
y = df["result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


scores = cross_val_score(
    make_pipeline(StandardScaler(), SVC()), X_train, y_train, cv=cv
)
print("SVM 5 fold:", scores.round(3), "| mean", round(scores.mean(), 3))


settings = {"max_depth": [2, 3, 4, 5, 6, 8], "min_samples_leaf": [1, 5, 10, 20]}
grid = GridSearchCV(DecisionTreeClassifier(random_state=42), settings, cv=cv)
grid.fit(X_train, y_train)
print(
    "Best:",
    grid.best_params_,
    "| CV:",
    round(grid.best_score_, 3),
    "| final test:",
    round(grid.score(X_test, y_test), 3)
)

print(
    "Best:",
    grid.best_params_,
    "| CV:",
    round(grid.best_scores_, 3),
    "| final Test:",
    round(grid.score(X_test, y_test), 3)
)
