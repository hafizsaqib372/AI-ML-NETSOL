import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from pathlib import Path
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


file_path = Path(__file__).parent / 'students_week5.csv'
df = pd.read_csv(file_path)
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {'Logistic Regression': LogisticRegression(max_iter=1000),
          'SVM (RBF)': SVC(), 'KNN(K=5)': KNeighborsClassifier(5),
          'Naive Bayes': GaussianNB()}

for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(X_train, y_train)
    print(f'{name:20s} accuracy = {pipe.score(X_test, y_test):.3f}')
