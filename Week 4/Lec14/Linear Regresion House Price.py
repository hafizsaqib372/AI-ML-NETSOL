from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data_path = Path(__file__).parent / "House Price Prediction Dataset.csv"
df = pd.read_csv(data_path)

print("Dataset Shape:", df.shape)
print("------------------")
print(df.head())
print("------------------")

print("Missing values in columns:")
print(df.isnull().sum())
print("------------------")

SQFT_PER_MARLA = 225

df["Area_Marla"] = df["Area"] / SQFT_PER_MARLA

print("First 5 rows after adding 'Area_Marla':")
print(df[["Area", "Area_Marla", "Price"]].head())
print("------------------")

corr = df[["Area_Marla", "Price"]].corr()
print("Correlation between Area_Marla and Price:")
print(corr)
print("------------------")

X = df[["Area_Marla"]]
y = df["Price"]

# 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Linear Regression Results (Single Feature: Area_Marla):")
print(f"Slope (Coefficient): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Mean Absolute Error (MAE): {mae:,.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:,.2f}")
print(f"R² Score: {r2:.4f}")
print("------------------")

# PREDICTIONS ON NEW DATA
new_houses = pd.DataFrame({"Area_Marla": [3, 5, 10, 20]})
new_predictions = model.predict(new_houses)

print("Predicted Prices for Sample House Sizes (in Marla):")
for marla, price in zip(new_houses["Area_Marla"], new_predictions):
    print(f"  {marla} Marla House -> Predicted Price: PKR {price:,.2f}")