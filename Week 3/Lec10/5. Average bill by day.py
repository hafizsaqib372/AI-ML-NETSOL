from pathlib import Path
import seaborn as sns

df = sns.load_dataset("tips", data_home=Path(__file__).parent)

avg_bill = df.groupby("day", observed=True)["total_bill"].mean()

print(avg_bill)
print("------------------")
print("Day with highest average bill:", avg_bill.idxmax())
print("Highest average bill:", round(avg_bill.max(), 2))
