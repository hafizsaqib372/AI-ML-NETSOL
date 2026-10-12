import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from pathlib import Path

file_path = Path(__file__).parent / 'students_week5.csv'
df = pd.read_csv(file_path)
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# without scaling first -- then with scaling
raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
print("KNN without scaling:", accuracy_score(y_test, raw.predict(X_test)))
scaler = StandardScaler()
X_train_s, X_test_s = scaler.fit_transform(X_train), scaler.transform(X_test)

for k in [1, 3, 5, 7, 9, 15, 25]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test_s))
    print(f'k={k:>2}: accuracy = {acc:.3f}')


file_path = Path(__file__).parent / 'students_week5.csv'
df = pd.read_csv(file_path)
X = df.drop(columns=['student_id'])