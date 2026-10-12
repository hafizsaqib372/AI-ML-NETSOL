import pandas as pd

df = pd.DataFrame({"height_cm": [170, 180, 160], "weight_kg": [65, 80, 55]})

df["bmi"] = df["weight_kg"] / (df["height_cm"] / 100) ** 2
print(df)

print("------------")

df = pd.DataFrame({"price": [100, 200, 150], "quantity": [10, 2, 5]})

df["total_cost"] = df["price"] * df["quantity"]
print(df)

print("------------")

df = pd.DataFrame(
    {"total_income": [100000, 500000, 20000], "total_expenses": [120000, 550000, 18000]}
)

savings = df["total_income"] - df["total_expenses"]
df["savings_rate"] = savings / df["total_income"]
print(df)
