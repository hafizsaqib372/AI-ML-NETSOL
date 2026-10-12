import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score' 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

for depth in [3, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    print(f'max_depth={depth}: train = {tree.score(X_train, y_train):.3f}'
          f' | test = {tree.score(X_test, y_test):.3f}')


small = DecisionTreeClassifier(max_depth=2, random_state=42,).fit(X_train, y_train)
print(export_text(small, feature_names=list(X.columns)))

