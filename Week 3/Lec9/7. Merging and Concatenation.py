import pandas as pd

a = pd.DataFrame({"id": [1, 2, 3], "name": ["Ali", "Sara", "Zain"]})
b = pd.DataFrame({"id": [1, 2, 4], "makrs": [85, 92, 70]})

print(pd.merge(a, b, on="id", how="inner"))
print(pd.merge(a, b, on="id", how="left"))

print(pd.concat((a, b)))
print(pd.concat((a, b), ignore_index=False))
