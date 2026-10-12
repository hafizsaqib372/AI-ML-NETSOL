import numpy as np
import pandas as pd

series = pd.Series([100, 500, 1000, 50000])
log_series = np.log(series)
print(log_series)