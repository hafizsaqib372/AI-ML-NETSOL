# 1. Store a sentence in a variable. Print it in uppercase and lowercase, display its length, print a slice of it, and check whether it contains a specific word.

sentence = "I love coding in python."

print(sentence.upper())
print(sentence.lower())
print(sentence[0:])
print(sentence[:-1])
print(sentence[9:-1])
print(sentence[7:-5])
print(sentence[0:9:2])
print(sentence[::-1])
print(sentence[9:0:-1])
print(sentence[9:0:-2])
print(sentence[::])
print("hello" in sentence)

# 2. Store a student’s name, subject, and marks in variables. Print a formatted sentence showing the student’s result.

name = "Ashar"
subject = "Maths"
marks = 100

print(f"{name} got {marks} marks in {subject}.")