student = {
    "roll_no": 101,
    "name": "Anu",
    "department": "CSE",
    "marks": 85
}
for key, value in student.items():
    print(key, ":", value)



employee = {
    "name": "Rahul",
    "id": 101,
    "department": "IT",
    "salary": 45000
}
key = input("Enter key: ")
print("Value:", employee.get(key, "Key not found"))  




products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Bottle": 100
}
products["Notebook"] = 80
print(products)




marks = {
    "Anu": 80,
    "Riya": 75,
    "Neha": 90
}
name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))
marks[name] = new_marks
print(marks)




cities = {
    "Pune": 7000000,
    "Mumbai": 20000000,
    "Delhi": 30000000
}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
print(cities)




employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha"
}
id = int(input("Enter employee ID: "))
if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")




students = {
    "Anu": 80,
    "Riya": 75,
    "Neha": 90,
    "Amit": 85
}
print("Total pairs:", len(students))    





data = {
    "name": "Anu",
    "age": 20,
    "city": "Pune"
}
print("Keys:", data.keys())
print("Values:", data.values())
print("Pairs:", data.items())




languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "Java": "James Gosling"
}
for language, creator in languages.items():
    print(language, ":", creator)






students = {}
for i in range(5):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print(students)    





students = {
    "Anu": 85,
    "Riya": 92,
    "Neha": 78
}
name = max(students, key=students.get)
print("Highest:", name)
print("Marks:", students[name])



students = {
    "Anu": 85,
    "Riya": 92,
    "Neha": 78
}
name = min(students, key=students.get)
print("Lowest:", name)
print("Marks:", students[name])





students = {
    "Anu": 80,
    "Riya": 90,
    "Neha": 70
}
total = sum(students.values())
average = total / len(students)
print("Average marks:", average)




text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)





sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)





d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}
d1.update(d2)
print(d1)






d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 40, "c": 50, "d": 60}
common = d1.keys() & d2.keys()
print("Common keys:", common)




d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"x": 20, "y": 40, "z": 30}
common = set(d1.values()) & set(d2.values())
print("Common values:", common)




data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)




data = {
    3: "C",
    1: "A",
    2: "B",
    5: "E",
    4: "D"
}
for key in sorted(data):
    print(key, ":", data[key])




squares = {}
for i in range(1, 11):
    squares[i] = i * i
print(squares) 




squares = {}
for i in range(2, 21, 2):
    squares[i] = i * i
print(squares)




numbers = [1, 2, 2, 3, 3, 3, 4, 4]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)



cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)






students = {
    "Anu": 80,
    "Riya": 90
}
students["Neha"] = 85         
students["Anu"] = 88         
del students["Riya"]           
name = input("Search student: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")
print("All students:", students)
print("Highest marks:", max(students.values()))
print("Average:", sum(students.values()) / len(students))







employees = {
    "Rahul": 45000,
    "Amit": 60000,
    "Sneha": 75000,
    "Neha": 40000
}
print("Highest salary:", max(employees.values()))
print("Lowest salary:", min(employees.values()))
average = sum(employees.values()) / len(employees)
print("Average salary:", average)
print("Salary above 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)




products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}
products["Pencil"] = 8       # Add
products["Pen"] = 25         # Update
del products["Bag"]          # Delete
name = input("Search product: ")
if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")
print("Products below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)







contacts = {
    "Anu": "9876543210",
    "Riya": "9123456780"
}
contacts["Neha"] = "9988776655"    
contacts["Anu"] = "9000000000"      
name = input("Search contact: ")
if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")
del contacts["Riya"]                
print("All contacts:")
for name, phone in contacts.items():
    print(name, phone)






books = {
    101: "Python",
    102: "Java",
    103: "C++"
}
books[104] = "HTML"       
id = int(input("Enter book ID: "))
if id in books:
    print("Book:", books[id])
else:
    print("Book not found")
del books[103]              
print("All books:", books)
print("Total books:", len(books))   





students = {
    "Anu": "CSE",
    "Riya": "IT",
    "Amit": "CSE",
    "Neha": "ENTC"
}
groups = {}
for name, dept in students.items():
    if dept not in groups:
        groups[dept] = []
    groups[dept].append(name)
print(groups)





words = ["cat", "dog", "apple", "ball", "sun"]
result = {}
for word in words:
    length = len(word)
    if length not in result:
        result[length] = []
    result[length].append(word)
print(result)



numbers = [2, 7, 11, 15]
target = 9
seen = {}
for num in numbers:
    need = target - num
    if need in seen:
        print("Numbers:", need, num)
        break
    seen[num] = True





text = input("Enter a string: ")
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
for ch in text:
    if count[ch] == 1:
        print("First unique character:", ch)
        break






text = input("Enter a string: ")
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
for ch in text:
    if count[ch] > 1:
        print("First repeated character:", ch)
        break    




paragraph = input("Enter a paragraph: ")
words = paragraph.split()
result = {}
for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1
print(result)

