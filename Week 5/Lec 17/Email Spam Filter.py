
# EMAIL SPAM DETECTION
# Naive Bayes + Other Supervised ML Models

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
 

# 1. LOAD DATASET

df = pd.read_csv("spam email.csv")

print("Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)



# 2. CLEAN DATA

# Remove missing values
df = df.dropna(subset=["Category", "Message"])

# Convert text to string
df["Message"] = df["Message"].astype(str)

# Convert labels to lowercase
df["Category"] = df["Category"].str.lower().str.strip()

print("\nClass Distribution:")
print(df["Category"].value_counts())


# 3. CONVERT LABEL

# ham = 0
# spam = 1

df["Category"] = df["Category"].map({
    "ham": 0,
    "spam": 1
})

# Remove rows where label conversion failed
df = df.dropna(subset=["Category"])

df["Category"] = df["Category"].astype(int)


# 4. INPUT AND OUTPUT

X = df["Message"]
y = df["Category"]


# 5. TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# 6. TF-IDF

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=10000,
    sublinear_tf=True
)

X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)


print("\nTF-IDF Training Shape:")
print(X_train_tfidf.shape)


# 7. CREATE MODELS

models = {

    "Naive Bayes": MultinomialNB(),

    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "SVM": LinearSVC(),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    )
}



# 8. TRAIN AND EVALUATE


results = []

for name, model in models.items():

    print("\n================================")
    print(name)
    print("================================")

    # Train
    model.fit(X_train_tfidf, y_train)

    # Prediction
    y_pred = model.predict(X_test_tfidf)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["Ham", "Spam"],
            zero_division=0
        )
    )

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })



# 9. MODEL COMPARISON

results_df = pd.DataFrame(results)

print("\n================================")
print("MODEL COMPARISON")
print("================================")

print(results_df)


# 10. CONFUSION MATRIX - NAIVE BAYES

nb_model = models["Naive Bayes"]

nb_prediction = nb_model.predict(X_test_tfidf)

cm = confusion_matrix(
    y_test,
    nb_prediction
)

print("\nNaive Bayes Confusion Matrix:")
print(cm)

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Ham", "Spam"]
).plot()

plt.title("Naive Bayes - Spam Detection")
plt.show()



# 11. COMPARE MODEL ACCURACY

plt.figure(figsize=(10, 6))

plt.bar(
    results_df["Model"],
    results_df["Accuracy"]
)

plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.title("Spam Detection Model Comparison")

plt.xticks(rotation=30)
plt.ylim(0, 1)

plt.tight_layout()
plt.show()



# 12. TEST NEW EMAIL

new_email = [
    "Congratulations! You have won a free cash prize. Click here now!"
]

new_email_tfidf = vectorizer.transform(new_email)


prediction = nb_model.predict(new_email_tfidf)


if prediction[0] == 1:
    print("\nResult: SPAM EMAIL 🚨")
else:
    print("\nResult: HAM / NOT SPAM ✅")