from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips", data_home=Path(__file__).parent)

sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total bill and tip")
plt.xlabel("Total bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.show()
