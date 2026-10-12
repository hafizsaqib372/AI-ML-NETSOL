marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")


age = int(input("Enter your age: "))
has_ticket = input("Do you have ticket? ")

if age >= 18:
    if has_ticket == "Yes" or has_ticket == "yes":
        print("Allowed")
    else:
        print("Not Allowed")
else:
    print("Age must be greater or equal to 18.")