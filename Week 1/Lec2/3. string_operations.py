course = "Machine Learning"
print(course.upper())  # MACHINE LEARNING
print(len(course))  # 16
print(course[0:9])  # Machine L
print("Learn" in course)  # True

student, score = "Ashar", 95
print(f"{student} scored {score}")  # Ashar scored 95

print(student + " scored " + str(score) + " marks")  # Ashar scored 95 marks

print("\n------------------------------------\n")

course = "Deep Learning"
print(course.lower())  # deep learning
print(len(course))  # 13
print("Deep" in course)  # True
print(f"The topic is {course}")  # The topic is Deep Learning