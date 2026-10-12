import pandas as pd

df = pd.DataFrame({"name": ["Ali", "Sara", "Ali"], "marks": [85, 92, 85]})

print(df.duplicated())
print(df.drop_duplicates())

df = pd.DataFrame({"name": ["Ashar", "Sara", "Ashar"], "marks": [100, 92, 100]})

print(df.duplicated())
print(df.drop_duplicates())

s = pd.Series([10, 12, 11, 9, 14, 8, 13, 250])
