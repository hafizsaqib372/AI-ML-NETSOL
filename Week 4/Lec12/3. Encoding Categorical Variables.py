import pandas as pd
from sklearn.preprocessing import LabelEncoder

sizes = ["Small", "Medium", "Large", "Medium"]
le = LabelEncoder()
print(le.fit_transform(sizes))
