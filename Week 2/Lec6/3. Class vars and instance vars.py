class Student:
    school = "NAVTACC"

    def __init__(self, name):
        self.name = name


s1 = Student("Ali")
s2 = Student("Sara")
print(s1.school, s2.school, s1.name, s2.name)


class Employee:
    company = "Netsol"

    def __init__(this, name):
        this.name = name


e1 = Employee("Ali")
e2 = Employee("Ahmad")
e3 = Employee("Bilal")

print(e1.company, e2.company, e3.company)
