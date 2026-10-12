class Student:
    def __init__(this, name, age):
        this.n = name
        this.a = age

    def greet(self):
        print(f"Hi, I am {self.n}")


s1 = Student("Ashar", 21)
s1.greet()

class Car:
    def __init__(this, brand, year):
        this.brand = brand
        this.year = year

    def description(this):
        print(f"The car is {this.brand} {this.year} model.")

c1 = Car("BMW", 1998)
c2 = Car("Supra", 2024)
c1.description()
c2.description()