from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips", data_home=Path(__file__).parent)

nums = df[["total_bill", "tip", "size"]]
corr = nums.corr()

print(corr)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation of bill, tip and party size")
plt.tight_layout()
plt.show()
