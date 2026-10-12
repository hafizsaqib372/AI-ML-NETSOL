# import seaborn as sns
import pandas as pd

# import matplotlib.pyplot as plt

df = pd.DataFrame({"dept": ["IT", "HR", "Sales"], "revenue": [250, 170, 130]})

df.plot(x="dept", y="revenue", kind="bar")
# plt.show()
