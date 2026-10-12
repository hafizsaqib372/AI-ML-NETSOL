import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

forest = RandomForestClassifier(n_estimators=200, random_state=42)
forest.fit(X_train, y_train)
print('Random Forest test accuracy:', round(forest.score(X_test, y_test), 3))

importance = pd.Series(forest.feature_importance_, index=X.columns)
print(importance.sort_values(ascending=False).round(3))

