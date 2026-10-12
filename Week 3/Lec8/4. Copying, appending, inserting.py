import numpy as np

c = np.array([1, 2, 3])
c_copy = c.copy()
c_copy[0] = 99
print(c, c_copy)

d = np.array([1, 2, 3])
print(np.append(d, [4, 5]))
print(np.insert(d, 1, 100))

arr = np.array([4, 5, 6])
copy_arr = arr.copy()
copy_arr[2] = 7
print(arr)
print(copy_arr)

print(np.append(arr, [7, 8, 9]))
print(np.insert(arr, 2, 3))
