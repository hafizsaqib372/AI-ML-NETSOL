import pandas as pd

data = {"name": ["Ali", "Sara", "Zain"], "marks": [85, 92, 78]}
df = pd.DataFrame(data)
print(df)

students_data = {
    "name": ["Ashar", "Ahmad", "Ali", "Noman"],
    "city": ["Lahore", "Islamabad", "Nawabshah", "Lahore"],
    "score": [100, 90, 85, 94],
}

s_df = pd.DataFrame(students_data)
print(s_df)
