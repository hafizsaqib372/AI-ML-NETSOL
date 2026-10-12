from pathlib import Path
import seaborn as sns

df = sns.load_dataset("tips", data_home=Path(__file__).parent)

print(df["day"].value_counts())
