for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x", j, "=", i*j)

print("---------------------")

for i in range(1, 6):
    for j in range(1):
        print("*" * i)

print("---------------------")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("---------------------")

for i in range(2, 3):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)

print("---------------------")

for i in range(3, 4):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)