import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
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


features = ["lag_1", "lag_7", "roll_7", "dayofweek", "month"]
X_train, y_train = train[features], train["sales"]
X_test, y_test = test[features], test["sales"]

for name, model in [
    ("Linear Regression", LinearRegression()),
    ("Random Forest", RandomForestRegressor(300, random_state=42)),
]:

    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f"{name:18s} MAE: {mean_absolute_error(y_test, pred):.1f}")


rf = RandomForestRegressor(300, random_state=42).fit(X_train, y_train)
print(pd.Series(rf.feature_importances_, index=features).round(2))
