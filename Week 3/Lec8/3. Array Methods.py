import numpy as np

b = np.array([3, 7, 1, 9, 4])

print(b.reshape(5, 1))
print(b.max(), b.min())
print(b.argmax(), b.argmin())

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.reshape(2, 3))

arr = np.array([4, 2, 9, 2, 3, 38, 13, 0])
print(arr.max(), arr.min())
print(arr.argmax(), arr.argmin())
