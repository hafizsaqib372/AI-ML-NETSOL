import pandas as pd

df = pd.DataFrame(
    {
        "study_hours": [1, 2, 3, 4, 5],
        "sleep_hrs": [8, 7, 6, 8, 7],
        "marks": [50, 55, 65, 70, 85],
    }
)

print(df.corr()["marks"])

print("----------------")

ages = pd.Series([5, 17, 25, 45, 68, 80])
print(
    pd.cut(
        ages, bins=[0, 12, 19, 59, 100], labels=["Child", "Teen", "Adult", "Seniors"]
    )
)

df = pd.DataFrame(
    {
        "study_hours": [1, 2, 3, 4, 5],
        "sleep_hrs": [8, 7, 6, 8, 7],
        "marks": [50, 55, 65, 70, 85],
    }
)
print(df[["marks", "sleep_hrs"]].corr())

print("----------------")

scores = pd.Series([96, 59, 72, 83, 6])

print(
    pd.cut(
        scores, bins=[0, 30, 50, 70, 100], labels=["Fail", "Pass", "Merit", "Distinct"]
    )
)
