import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# 1. LOAD DATASET


df = pd.read_csv("Titanic-Dataset.csv")


# 2. FEATURE ENGINEERING


# Family size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


# Is passenger alone?
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)


# Extract passenger title
df["Title"] = df["Name"].str.extract(
    r",\s*([^.]*)\."
)[0].str.strip()


# Keep common titles
common_titles = [
    "Mr",
    "Miss",
    "Mrs",
    "Master"
]

df["Title"] = df["Title"].where(
    df["Title"].isin(common_titles),
    "Rare"
)


# Fare per person
df["FarePerPerson"] = (
    df["Fare"] / df["FamilySize"]
)



# 3. SELECT FEATURES

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
    "Title",
    "FarePerPerson"
]

X = df[features]

y = df["Survived"]


# 4. NUMERICAL FEATURES


numeric_features = [
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "FamilySize",
    "IsAlone",
    "FarePerPerson"
]


# 5. CATEGORICAL FEATURES


categorical_features = [
    "Sex",
    "Embarked",
    "Title"
]


# 6. NUMERICAL PREPROCESSING

numeric_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),

        (
            "scaler",
            StandardScaler()
        )
    ]
)


# 7. CATEGORICAL PREPROCESSING

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



# 8. COMBINE PREPROCESSING

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


# 9. KNN PIPELINE

pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",
            KNeighborsClassifier()
        )
    ]
)



# 10. TRAIN / TEST SPLIT


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# 11. KNN PARAMETERS

param_grid = {

    "classifier__n_neighbors": [
        3, 5, 7, 9, 11, 13, 15, 17, 19, 21
    ],

    "classifier__weights": [
        "uniform",
        "distance"
    ],

    "classifier__metric": [
        "euclidean",
        "manhattan",
        "minkowski"
    ],

    "classifier__p": [
        1,
        2
    ]
}


# 12. CROSS VALIDATION


cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# 13. GRID SEARCH

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1
)


# 14. TRAIN

grid_search.fit(
    X_train,
    y_train
)



# 15. BEST PARAMETERS

print("\n==============================")
print("BEST PARAMETERS")
print("==============================")

print(
    grid_search.best_params_
)



# 16. BEST CV ACCURACY


print("\n==============================")
print("BEST CV ACCURACY")
print("==============================")

print(
    f"{grid_search.best_score_ * 100:.2f}%"
)



# 17. BEST MODEL

best_model = grid_search.best_estimator_


# 18. PREDICTION

y_pred = best_model.predict(
    X_test
)



# 19. TEST ACCURACY

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n==============================")
print("TEST ACCURACY")
print("==============================")

print(
    f"{accuracy * 100:.2f}%"
)



# 20. CLASSIFICATION REPORT

print("\n==============================")
print("CLASSIFICATION REPORT")
print("==============================")

print(
    classification_report(
        y_test,
        y_pred
    )
)



# 21. CONFUSION MATRIX


print("\n==============================")
print("CONFUSION MATRIX")
print("==============================")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)