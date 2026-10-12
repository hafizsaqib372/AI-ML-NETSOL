import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix



# 1. Load Dataset

df = pd.read_csv("Titanic-Dataset.csv")

# 2. Feature Engineering

# Family size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Is the passenger alone?
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# Extract passenger title from Name
df["Title"] = df["Name"].str.extract(
    r",\s*([^.]*)\."
)

# Group uncommon titles
title_counts = df["Title"].value_counts()

df["Title"] = df["Title"].where(
    df["Title"].isin(title_counts[title_counts >= 10].index),
    "Rare"
)

# 3. Select Features

features = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked",
    "FamilySize",
    "IsAlone",
    "Title"
]

X = df[features]

y = df["Survived"]

# 4. Define Columns

numeric_features = [
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "FamilySize",
    "IsAlone"
]

categorical_features = [
    "Sex",
    "Embarked",
    "Title"
]

# 5. Numeric Preprocessing

numeric_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        )
    ]
)


# 6. Categorical Preprocessing

categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "onehot",
            OneHotEncoder(handle_unknown="ignore")
        )
    ]
)


# 7. Combine Preprocessing

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_transformer,
            numeric_features
        ),
        (
            "categorical",
            categorical_transformer,
            categorical_features
        )
    ]
)


# 8. Random Forest Pipeline

pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            RandomForestClassifier(
                random_state=42
            )
        )
    ]
)



# 9. Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# 10. Hyperparameter Tuning

param_grid = {

    "classifier__n_estimators": [
        100,
        200,
        300
    ],

    "classifier__max_depth": [
        None,
        5,
        10,
        15
    ],

    "classifier__min_samples_split": [
        2,
        5,
        10
    ],

    "classifier__min_samples_leaf": [
        1,
        2,
        4
    ],

    "classifier__max_features": [
        "sqrt",
        "log2"
    ]
}


grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)


# 11. Train

grid_search.fit(X_train, y_train)

# 12. Best Parameters

# print("\nBest Parameters:")
# print(grid_search.best_params__)


# 13. Best Cross Validation Accuracy

print("\nBest CV Accuracy:")
print(grid_search.best_score_)


# 14. Prediction

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)


# 15. Test Accuracy

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nTest Accuracy:")
print(accuracy)

print("\nTest Accuracy Percentage:")
print(f"{accuracy * 100:.2f}%")


# 16. Classification Report

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)


# 17. Confusion Matrix

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)