# try:
#     num = int(input("Enter a number: "))
#     print(10/num)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("That is not a valid number!")
# finally:
#     print("Done trying.")

try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("That is not a valid number!")
finally:
    print("Done trying.")
