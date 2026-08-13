t = (10, 20, 30, 40, 50)
print(t)


cities = ("Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])


students = ("Anagha", "Riya", "Sneha", "Pooja", "Neha")
print("Total students:", len(students))


colors = ("Red", "Blue", "Green", "Yellow", "Black")
color = input("Enter color: ")
if color in colors:
    print("Color exists")
else:
    print("Color does not exist")


fruits=("apple","grapes","watermelon","mango")
for fruit in fruits:
        print(fruit)


numbers = (10, 20, 10, 30, 10, 40, 20)
n = int(input("Enter number: "))
print("Count:", numbers.count(n))


ids = (101, 102, 103, 104, 105)
id = int(input("Enter employee ID: "))
if id in ids:
    print("Index:", ids.index(id))
else:
    print("ID not found")


t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)


t = (1, 2, 3)
print(t * 4)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five:", numbers[:5])
print("Last five:", numbers[5:])
print("Middle four:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])



t = (10, 20, 30)
lst = list(t)
lst.append(40)
print(lst)


numbers = []
for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)
t = tuple(numbers)
print("Tuple:", t)


t = (10, 20, 30)
lst = list(t)
lst[1] = 50
t = tuple(lst)
print(t)


t=(10,20,30)
del t
print("tuple deleted")



students = (
    (1, "Anagha", 85),
    (2, "Riya", 90),
    (3, "Sneha", 88)
)
for student in students:
    print(student)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
total = 0
for n in numbers:
    total += n
print("Sum:", total)



numbers = (25, 10, 45, 5, 30)
largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest)
print("Smallest:", smallest)



numbers = (10, 20, 30, 40, 50)
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print("Average:", average)



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)



numbers = (10, 20, 30, 40, 50)
n = int(input("Enter number: "))
if n in numbers:
    print("Number exists")
else:
    print("Number does not exist")




student = (101, "Anagha", "Computer Engineering", 85)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])



employees = (
    (101, "Rahul", 30000),
    (102, "Sneha", 35000),
    (103, "Pooja", 40000)
)
for emp in employees:
    print("ID:", emp[0], "Name:", emp[1], "Salary:", emp[2])




prices = (100, 250, 150, 300, 200)
total = sum(prices)
average = total / len(prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest price:", max(prices))
print("Lowest price:", min(prices))




temperatures = (30, 32, 29, 31, 33, 28, 30)
total = sum(temperatures)
average = total / len(temperatures)
print("Maximum:", max(temperatures))
print("Minimum:", min(temperatures))
print("Average:", average)


runs = (45, 60, 32, 75, 80, 55, 40, 90, 65, 50)
total = sum(runs)
average = total / len(runs)
print("Total runs:", total)
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", average)



t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
common = tuple(set(t1) & set(t2))
print("Common elements:", common)



t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
merged = tuple(set(t1 + t2))
print("Merged tuple:", merged)



numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
for n in set(numbers):
    print(n, ":", numbers.count(n))




numbers = (40, 10, 30, 20, 50)
ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending) 




patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Pooja", 22, "O+"),
    (104, "Amit", 28, "A+")
)


print("All Patient Records:")
for patient in patients:
    print(patient)
pid = int(input("\nEnter Patient ID: "))
found = False
for patient in patients:
    if patient[0] == pid:
        print("Patient Found:", patient)
        found = True
if not found:
    print("Patient not found")
print("Total patients:", len(patients))
blood = input("Enter blood group: ")
print("Patients with blood group", blood, ":")
for patient in patients:
    if patient[3] == blood:
        print(patient)
