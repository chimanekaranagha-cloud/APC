calculator.py
def add (a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul (a,b):
    return (a*b)
def div(a,b):
    return(a/b)

main.py
import calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", calculator.add(a, b))
print("Subtraction =", calculator.sub(a, b))
print("Multiplication =", calculator.mul(a, b))
print("Division =", calculator.div(a, b))

file.py
f = open("demo.txt", "r")
vowels = 0
consonants = 0
digits = 0
special = 0
text = f.read()
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1
f.close()
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Special Characters =", special)

student.py
import numpy as np
marks = np.array([
    [[80, 75, 90], [70, 85, 88]],
    [[65, 78, 82], [90, 92, 85]]
])
print("3D Array:")
print(marks)
print("Student 1 marks:")
print(marks[0])
print("Student 2 marks:")
print(marks[1])
print("Student 1, Subject 2 marks:")
print(marks[0][1][0])






