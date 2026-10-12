student = {"name": "Ali", "age": 20}
print(student["name"])
student["age"] = 21
student["city"] = "Lahore"

for key, value in student.items():
    print(key, " : ", value)


book = {
    "title": "A litle life",
    "author": "Newton",
    "year": 2021
}

for key, value in book.items():
    print(key)

for key, value in book.items():
    print(value)

book["year"] = 2026
