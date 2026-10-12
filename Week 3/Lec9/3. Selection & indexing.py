import pandas as pd

data = {"name": ["Ali", "Sara", "Zain"], "marks": [85, 92, 78]}
df = pd.DataFrame(data)

print(df[df["marks"] > 80])

students_data = {
    "name": ["Ashar", "Ahmad", "Ali", "Noman", "Zain"],
    "city": ["Lahore", "Islamabad", "Nawabshah", "Lahore", "Okara"],
    "score": [100, 90, 85, 94, 70],
}
df = pd.DataFrame(students_data)
print(df[df["score"] > 75])

print(df[["name", "score"]])
