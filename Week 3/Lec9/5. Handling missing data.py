import pandas as pd

# df = pd.DataFrame({"a": [1, 2, None], "b": [4, None, 6]})

# print(df.isnull())
# print(df.fillna(0))

df = pd.DataFrame({"a": [1, 2, None], "b": [4, None, 6]})
print(df.isnull())

print(df.dropna())
print(df.fillna(5))
