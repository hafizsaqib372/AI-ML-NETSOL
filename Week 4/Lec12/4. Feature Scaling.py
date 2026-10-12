import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

vals = np.array([[10], [20], [30], [40], [50]])
print(StandardScaler().fit_transform(vals).flatten())
print(MinMaxScaler().fit_transform(vals).flatten())

new_vals = np.array([[100], [200], [300], [400], [500]])
print(StandardScaler().fit_transform(vals).flatten())
print(MinMaxScaler().fit_transform(vals).flatten())
