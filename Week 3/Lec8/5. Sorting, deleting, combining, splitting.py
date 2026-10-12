import numpy as np

e = np.array([5, 2, 8, 1])
print(np.sort(e))
print(np.delete(e, 0))

f1, f2 = np.array([1, 2]), np.array([3, 4])
print(np.concatenate((f1, f2)))
print(np.array_split(np.arange(1, 7), 3))

arr = np.array([5, 9, 2, 7, 3, 1])
print(np.sort(arr))
print(np.delete(arr, 2))

arr1, arr2 = np.array([10, 11]), np.array([13, 14, 15])
arr3 = np.concatenate((arr1, arr2))
print(arr3)

arr4, arr5 = np.array_split(arr3, 2)
print(arr4)
print(arr5)
