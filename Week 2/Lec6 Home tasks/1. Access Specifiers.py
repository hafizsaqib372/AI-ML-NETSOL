class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self._roll_no = roll_no
        self.__marks = marks

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self._roll_no)
        print("Marks:", self.__marks)

    def get_marks(self):
        return self.__marks


s = Student("Ali", 101, 85)
print(s.name)
print(s._roll_no)
print(s.get_marks())
s.show()
