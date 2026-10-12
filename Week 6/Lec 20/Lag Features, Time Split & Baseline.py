import pandas as pd
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("shop_sales_daily.csv", parse_dates=["date"])


df["lag_1"] = df["sales"].shift(1)
df["lag_7"] = df["sales"].shift(7)
df["roll_7"] = df["sales"].shift(1).rolling(7).mean()
df["dayofweek"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
df = df.dropna()


train = df[df["date"] < "2025-10-01"]
test = df[df["date"] >= "2025-10-01"]
print("Train days:", len(train), "| Test days:", len(test))

for name, col in [
    ("Naive (yesterday)", "lag_1"),
    ("7-day average", "roll_7"),
    ("Seasonal naive (lag 7)", "lag_7"),
]:
    print(f"{name:24s} MAE: {mean_absolute_error(test['sales'], test[col]):.1f}")
