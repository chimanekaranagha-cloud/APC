fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
print("Fruits:", fruits)


num = [10, 20, 30, 40, 50]

print("First:", num[0])
print("Last:", num[-1])
print("Third:", num[2])


colors = ["Red", "Blue", "Green", "Yellow"]
colors[2] = "Pink"

print(colors)


numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(0, 5)
numbers.insert(2, 15)

print(numbers)




students = ["Amit", "Riya", "Neha", "Karan", "Pooja"]

students.pop(0)
students.pop()
students.remove("Neha")

print(students)



num = [12, 45, 8, 67, 23]

largest = num[0]
smallest = num[0]

for i in num:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)




num = []

for i in range(10):
    n = int(input("Enter number: "))
    num.append(n)

s = sum(num)
avg = s / 10

print("Sum =", s)
print("Average =", avg)



num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even = 0
odd = 0

for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)



cities = ["Pune", "Mumbai", "Kolhapur", "Delhi"]

city = input("Enter city: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")



num = [10,20,30,40,50]

rev = num[::-1]

print(rev)



num = [1,2,3,4,5,6,7,8,9,10]

print("First 5:", num[:5])
print("Last 5:", num[5:])
print("Middle 4:", num[3:7])
print("Alternate:", num[::2])
print("Reverse:", num[::-1])


num = [10,20,30,40,50,60,70]

print("Elements at even index:")

for i in range(0, len(num), 2):
    print(num[i])





num = []

for i in range(10):
    n = int(input("Enter number: "))
    num.append(n)

num.sort()
print("Ascending:", num)

num.sort(reverse=True)
print("Descending:", num)




num = [1,2,2,3,4,4,5,6,6]

unique = []

for i in num:
    if i not in unique:
        unique.append(i)

print(unique)



num = [10,25,40,15,35]

num.sort()

print("Second Largest:", num[-2])



students = [
    ["Amit",101,85],
    ["Riya",102,90],
    ["Neha",103,88]
]

for s in students:
    print("Name:", s[0], "Roll:", s[1], "Marks:", s[2])



A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

C = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Result:")

for row in C:
    print(row)







cart = ["Milk","Bread","Rice"]

cart.append("Sugar")
cart.remove("Bread")

item = input("Search item: ")

if item in cart:
    print("Item Found")
else:
    print("Item Not Found")

print("Cart:", cart)
print("Total Items:", len(cart))







students = ["Amit","Riya","Neha"]

print("Total Students:", len(students))

name = input("Search student: ")

if name in students:
    print("Present")
else:
    print("Absent")

students.append("Karan")
students.remove("Neha")

print(students)








books = ["Python","Java","C++"]

books.append("HTML")

book = input("Search book: ")

if book in books:
    print("Book Found")
else:
    print("Book Not Found")

books.remove("Java")

print("Books:", books)
print("Total Books:", len(books))







list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print("Merged List:", list3)





list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements:", common)









num = [1, 2, 2, 3, 3, 3, 4]

for i in num:
    print(i, "=", num.count(i))







num = [1, 2, 3, 4, 5]

left = num[1:] + [num[0]]
right = [num[-1]] + num[:-1]

print("Left Rotation:", left)
print("Right Rotation:", right)






num = [1, 2, 2, 3, 4, 4, 5]

unique = []

for i in num:
    if i not in unique:
        unique.append(i)

print("Unique List:", unique)






marks = []

for i in range(20):
    m = int(input("Enter Marks: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / 20

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above Average:", above)
print("Below Average:", below)








salary = [25000, 60000, 45000, 70000, 28000]

print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", sum(salary) / len(salary))

above = 0
below = 0

for i in salary:
    if i > 50000:
        above += 1
    if i < 30000:
        below += 1

print("Above 50000:", above)
print("Below 30000:", below)









score = [45, 80, 120, 60, 20, 100, 55, 30, 140, 75]

print("Highest:", max(score))
print("Lowest:", min(score))
print("Total:", sum(score))
print("Average:", sum(score) / len(score))

century = 0
half = 0

for i in score:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1

print("Centuries:", century)
print("Half-centuries:", half)





temp = []

for i in range(30):
    t = int(input("Enter Temperature: "))
    temp.append(t)

highest = max(temp)
lowest = min(temp)
average = sum(temp) / 30

above = 0
below = 0

for i in temp:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Hottest Day:", highest)
print("Coldest Day:", lowest)
print("Average:", average)
print("Above Average:", above)
print("Below Average:", below)








names = ["Amit", "Riya", "Neha"]
ages = [25, 30, 22]

names.append("Karan")
ages.append(28)

search = input("Enter Patient Name: ")

if search in names:
    print("Patient Found")
else:
    print("Patient Not Found")

names.remove("Neha")
ages.pop(2)

print("Patients:")
for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total Patients:", len(names))







































