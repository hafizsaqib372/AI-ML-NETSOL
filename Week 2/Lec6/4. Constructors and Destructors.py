class Student:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")


s1 = Student("Ali")
del s1


class Book:
    def __init__(self, title):
        self.title = title
        print("Book added")

    def __del__(self):
        print("Book removed")


b1 = Book("A little life")
del b1
