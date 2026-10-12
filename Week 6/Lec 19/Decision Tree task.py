import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)



# 1. LOAD DATASET


df = pd.read_csv("student-mat.csv", sep=";")

print("Dataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())


# 2. CREATE TARGET: PASS / FAIL

# G3 = final grade
# G3 >= 10  --> Pass
# G3 < 10   --> Fail

df["result"] = (df["G3"] >= 10).astype(int)

print("\nResult Distribution:")
print(df["result"].value_counts())

# 0 = Fail
# 1 = Pass


# 3. SELECT FEATURES

# Remove G3 because result is directly created from G3.
# Also remove G1 and G2 to make the prediction more realistic
# if you want to predict final performance before final grade.

X = df.drop(
    columns=["G3", "G2", "result"]
)
y = df["result"]


# 4. FIND NUMERICAL AND CATEGORICAL COLUMNS

categorical_columns = X.select_dtypes(
    include=["object"]
).columns

numerical_columns = X.select_dtypes(
    exclude=["object"]
).columns

print("\nCategorical Columns:")
print(list(categorical_columns))

print("\nNumerical Columns:")
print(list(numerical_columns))


# 5. ENCODE CATEGORICAL DATA

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)


# 6. PREPROCESS DATA

X_processed = preprocessor.fit_transform(X)


# 7. TRAIN / TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X_processed,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# 8. TEST DIFFERENT TREE DEPTHS

print("\n===================================")
print("DECISION TREE RESULTS")
print("===================================")

for depth in [2, 3, 4, 5, None]:

    tree = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    tree.fit(X_train, y_train)

    train_accuracy = tree.score(X_train, y_train)
    test_accuracy = tree.score(X_test, y_test)

    print(
        f"max_depth = {depth}: "
        f"Train = {train_accuracy:.3f} | "
        f"Test = {test_accuracy:.3f}"
    )



# 9. CREATE FINAL DECISION TREE

tree = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

tree.fit(X_train, y_train)


# 10. MAKE PREDICTIONS

y_pred = tree.predict(X_test)

# 11. ACCURACY

accuracy = accuracy_score(y_test, y_pred)

print("\n===================================")
print("MODEL ACCURACY")
print("===================================")

print(f"Accuracy: {accuracy:.3f}")
print(f"Accuracy: {accuracy * 100:.2f}%")

# 12. CONFUSION MATRIX

print("\n===================================")
print("CONFUSION MATRIX")
print("===================================")

print(confusion_matrix(y_test, y_pred))

# 13. CLASSIFICATION REPORT

print("\n===================================")
print("CLASSIFICATION REPORT")
print("===================================")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Fail", "Pass"]
    )
)

# 14. DISPLAY DECISION TREE RULES

print("\n===================================")
print("DECISION TREE RULES")
print("===================================")

feature_names = preprocessor.get_feature_names_out()

rules = export_text(
    tree,
    feature_names=list(feature_names)
)

print(rules)