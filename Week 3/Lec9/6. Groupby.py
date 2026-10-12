import pandas as pd

# sales = pd.DataFrame({"dept": ["IT", "IT", "HR", "HR"], "sales": [100, 150, 80, 90]})

# print(sales.groupby("dept")["sales"].sum())

products = pd.DataFrame(
    {"category": ["Mobile", "Laptop", "Mobile", "Laptop"], "price": [100, 50, 200, 150]}
)
print(products.groupby("category")["price"].mean())
print("------------------")
print(products.groupby("category").count())
