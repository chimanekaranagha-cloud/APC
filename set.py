numbers = {10, 20, 30, 40, 50}
print("Set elements:", numbers)


numbers = [10, 20, 10, 30, 20, 40]
result = set(numbers)
print("Set:", result)


fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
fruits.add("Papaya")
fruits.add("Watermelon")
print("Updated set:", fruits)


numbers = {10, 20, 30, 40, 50}
num = 30
numbers.remove(num)
print("Updated set:", numbers)


students = {"Anagha", "Rahul", "Sneha", "Priya", "Amit"}
name = input("Enter student name: ")
if name in students:
    print("Student exists")
else:
    print("Student does not exist")



cities = {"Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur"}
print("Total cities:", len(cities))


languages = {"Python", "Java", "C++", "JavaScript", "C"}
for language in languages:
    print(language)


numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = set(numbers)
print("Without duplicates:", unique_numbers)  


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Only in first set:", set1 - set2)
print("Only in second set:", set2 - set1)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Symmetric difference:", set1.symmetric_difference(set2))


set1 = {1, 2}
set2 = {1, 2, 3, 4}
if set1.issubset(set2):
    print("First set is a subset of second set")
else:
    print("First set is not a subset of second set")



set1 = {1, 2, 3, 4}
set2 = {1, 2}
if set1.issuperset(set2):
    print("First set is a superset of second set")
else:
    print("First set is not a superset of second set")



set1 = {1, 2, 3}
set2 = {4, 5, 6}
if set1.isdisjoint(set2):
    print("Sets have no elements in common")
else:
    print("Sets have common elements")




set1 = {1, 2, 3}
set2 = {3, 2, 1}
if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")



student1 = {"Python", "Java", "Maths", "DS"}
student2 = {"Python", "C++", "Maths", "OS"}
print("Subjects studied by both:", student1.intersection(student2))



sentence = input("Enter a sentence: ")
words = set(sentence.split())
print("Unique words:", words)



morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Neha", "Kiran"}
print("Both sessions:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)



python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Neha", "Kiran"}
print("Python students:", python_students)
print("Java students:", java_students)



python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Neha", "Kiran"}
both = python_students & java_students
only_one = python_students ^ java_students
print("Students in both courses:", both)
print("Students in only one course:", only_one)



available_books = {"Python", "Java", "C++", "AI", "OS"}
requested_books = {"Python", "DS", "CN"}
print("Requested books available:", available_books & requested_books)



day1 = {11, 12, 13, 14}
day2 = {13, 14, 15, 16}
print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)



category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Mobile", "Mouse", "Monitor", "Tablet"}
print("Products in both categories:", category1 & category2)





user1 = {"Rahul", "Anu", "Sanu", "Priya"}
user2 = {"Sneha", "Priya", "Kiran", "Neha"}
print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1 | user2))

















