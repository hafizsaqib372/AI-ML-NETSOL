import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

df = pd.DataFrame({"name": ["Ali", "Sara"], "marks": [85, 92]})
print(df["marks"])

cities = ["Lahore", "Multan", "Karachi", "Islamabad", "Peshawar"]
s = pd.Series(cities, index=["c1", "c2", "c3", "c4", "c5"])
print(s)

students_data = {
    "name": ["Ashar", "Ahmad", "Ali", "Noman"],
    "city": ["Lahore", "Islamabad", "Nawabshah", "Lahore"],
    "score": [100, 90, 85, 94],
}
df = pd.DataFrame(students_data)
print(type(df["city"]))
