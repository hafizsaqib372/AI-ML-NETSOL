import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from pathlib import Path


file_path = Path(__file__).parent / 'students_week5.csv'
df = pd.read_csv(file_path)
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

for kernal in ['linear', 'rbf']:
    model = SVC(kernel=kernal, C= 1.0)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f'SVM {kernal} accuracy: {acc:.3f}')

#ANOTHER CODE WITH FIND PERFORMANCE

file_path = Path(__file__).parent / 'students_week5.csv'
df = pd.read_csv(file_path)
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['performance']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

for kernal in ['linear', 'rbf']:
    model = SVC(kernel=kernal, C=1.0)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f'SVM {kernal} accuracy: {acc:.3f}')
