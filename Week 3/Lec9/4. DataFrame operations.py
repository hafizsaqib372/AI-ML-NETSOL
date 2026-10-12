import pandas as pd

data = {"name": ["Ali", "Sara", "Zain"], "marks": [85, 92, 78]}
df = pd.DataFrame(data)

df["grade"] = df["marks"].apply(lambda x: "Pass" if x >= 90 else "Fail")
print(df.sort_values("marks", ascending=False))

data = {"name": ["Ali", "Sara", "Zain"], "temparature": [65, 92, 92]}
df = pd.DataFrame(data)

df["status"] = df["temparature"].apply(lambda x: "high" if x >= 70 else "low")
print(df.sort_values("temparature", ascending=False))

print(df.value_counts("temparature"))