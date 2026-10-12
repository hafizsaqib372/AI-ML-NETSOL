import numpy as np

arr = np.array([1, 2, 3, 4])
np.save("my_array.npy", arr)

loaded = np.load("my_array.npy")
print(loaded)
