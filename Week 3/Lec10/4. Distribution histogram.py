from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips", data_home=Path(__file__).parent)

sns.histplot(df["total_bill"])
plt.title("Distribution of total bills")
plt.xlabel("Total bill ($)")
plt.ylabel("Number of records")
plt.tight_layout()
plt.show()
