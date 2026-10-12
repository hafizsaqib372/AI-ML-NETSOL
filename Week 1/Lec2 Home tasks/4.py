# 1. Ask the user for two numbers, convert them to float, and print their sum, product, and average.

a = input("Enter first number: ")
b = input("Enter 2nd number: ")

a = float(a)
b = float(b)

print(a + b)
print(a * b)
print((a + b) / 2)

"""
2. Ask the user for their name, birth year, and marks in three subjects. Convert the birth year to int and the marks to float or int. Then print:

- Their name and calculated age
- Total marks
- Average marks
- Whether they passed, where the average must be at least 50

Use an f-string for the final output.
"""

name = input("Enter your name: ")
birthYear = int(input("Enter birth year: "))
marksInMaths = int(input("Enter your marks in maths: "))
marksInPhysics = int(input("Enter your marks in physics: "))
marksInComputer = int(input("Enter your marks in computer: "))

age = 2026 - birthYear
totalMarks = marksInMaths + marksInPhysics + marksInComputer
avg = totalMarks / 3
isPass = avg >= 50

print(f"{name} with {age} age got {totalMarks} total marks with {avg} average and his pass status is {isPass}")