def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))


def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(7))


def greater(a, b):
    if a > b:
        return a
    else:
        return b
print(greater(10, 20))


def simple_interest(p, r, t):
    return (p * r * t) / 100
print(simple_interest(1000, 5, 2))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))



def circle_area(r):
    return 3.14 * r * r
print(circle_area(5))


def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
print(natural_sum(5))


def power(base, exponent):
    return base ** exponent
print(power(2, 3))



def largest(numbers):
    large = numbers[0]
    for n in numbers:
        if n > large:
            large = n
    return large
print(largest([10, 25, 7, 30, 15]))



def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count
print(count_vowels("umbreella"))



def reverse_string(text):
    return text[::-1]
print(reverse_string("college"))


def palindrome(value):
    value = str(value)
    if value == value[::-1]:
        return True
    else:
        return False
print(palindrome("madam"))


def average(numbers):
    return sum(numbers) / len(numbers)
print(average([10, 20, 30]))


def count_element(lst, element):
    count = 0
    for x in lst:
        if x == element:
            count += 1
    return count
print(count_element([1, 2, 2, 3, 2], 2))



def unique_elements(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result
print(unique_elements([1, 2, 2, 3, 3, 4]))



def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]
print(second_largest([10, 20, 60, 90]))


def fibonacci(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci(7))



def marks_result(a, b, c, d, e):
    total = a + b + c + d + e
    percentage = total / 5
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"
    return percentage, grade
print(marks_result(80, 75, 90, 85, 70))



def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill
print(electricity_bill(250))



def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da
print(gross_salary(20000))



def total_bill(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    discount = total * 0.10
    return total - discount
print(total_bill([100, 200], [2, 3]))



def list_details(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, average
print(list_details([40, 20, 40, 80]))



def total_marks(marks):
    return sum(marks)
def percentage(marks):
    return sum(marks) / 5
def grade(per):
    if per >= 75:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 50:
        return "C"
    else:
        return "D"
students = [
    {"name": "Amit", "roll": 1, "marks": [80, 75, 85, 90, 70]},
    {"name": "Riya", "roll": 2, "marks": [70, 65, 75, 80, 60]},
    {"name": "Raj", "roll": 3, "marks": [90, 85, 95, 88, 92]}
]
for s in students:
    per = percentage(s["marks"])
    print(s["name"], total_marks(s["marks"]), per, grade(per))







balance = 1000
history = []
def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited " + str(amount))
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")
def enquiry():
    print("Balance:", balance)
def transactions():
    print(history)
deposit(500)
withdraw(200)
enquiry()
transactions()  





books = {
    "Python": True,
    "Java": True,
    "C++": True
}
def add_book(name):
    books[name] = True
def issue_book(name):
    if name in books and books[name]:
        books[name] = False
        print("Book issued")
    else:
        print("Book not available")
def return_book(name):
    books[name] = True
def search_book(name):
    if name in books:
        print("Book found")
    else:
        print("Book not found")
def available_books():
    for name in books:
        if books[name]:
            print(name)
issue_book("Python")
available_books()




def slab_charge(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 500 + (units - 100) * 7
    else:
        return 1200 + (units - 200) * 10
def electricity_bill(units):
    fixed = 100
    charge = slab_charge(units)
    tax = charge * 0.05
    return charge + fixed + tax
print(electricity_bill(250))




def consultation(charge):
    return charge
def laboratory(charge):
    return charge
def medicine(charge):
    return charge
def room(charge):
    return charge
def final_bill(category, c, l, m, r):
    total = consultation(c) + laboratory(l) + medicine(m) + room(r)
    if category == "senior":
        total = total * 0.90
    return total
print(final_bill("senior", 500, 1000, 500, 2000))





products = []
def add_product(name, price, quantity):
    products.append((name, price, quantity))
def remove_product(name):
    for p in products:
        if p[0] == name:
            products.remove(p)
def subtotal():
    return sum(p[1] * p[2] for p in products)
def final_invoice():
    sub = subtotal()
    discount = sub * 0.10
    gst = (sub - discount) * 0.18
    total = sub - discount + gst
    print("Subtotal:", sub)
    print("Discount:", discount)
    print("GST:", gst)
    print("Final Bill:", total)
add_product("Pen", 20, 5)
add_product("Book", 100, 2)
final_invoice()




def binary_search(lst, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == key:
        return mid
    elif key < lst[mid]:
        return binary_search(lst, low, mid - 1, key)
    else:
        return binary_search(lst, mid + 1, high, key)
numbers = [10, 20, 30, 40, 50]
print(binary_search(numbers, 0, len(numbers)-1, 30))





def decimal_binary(n):
    if n == 0:
        return ""
    return decimal_binary(n // 2) + str(n % 2)
print(decimal_binary(10))







def palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palindrome(text[1:-1])
print(palindrome("mom"))



def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def calculate(function, a, b):
    return function(a, b)
print(calculate(add, 20, 4))
print(calculate(multiply, 20, 4))



square = lambda x: x * x
print(square(5))


cube = lambda x: x * x * x
print(cube(3))



even = lambda x: x % 2 == 0
print(even(10))


maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))



simple_interest = lambda p, r, t: (p * r * t) / 100
print(simple_interest(1000, 5, 2))



numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)



numbers = [1, 2, 3, 4]
result = list(map(lambda x: x ** 3, numbers))
print(result)



a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)



numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)



def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: prime(x), numbers))
print(result)



numbers = [-5, 2, -3, 7, 8, -1]
result = list(filter(lambda x: x > 0, numbers))
print(result)



numbers = [20, 55, 70, 30, 90]
result = list(filter(lambda x: x > 50, numbers))
print(result)



words = ["apple", "orange", "bird", "python", "laptop"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)




students = [
    ("ovi", 70),
    ("rumji", 90),
    ("smith", 80)
]
result = sorted(students, key=lambda x: x[1])
print(result)




employees = [
    ("Ram", 30000),
    ("Sham", 50000),
    ("kamini", 40000)
]
result = sorted(employees, key=lambda x: x[1])
print(result)




students = [
    ("ameya", 70),
    ("ayush", 85),
    ("athrav", 90),
    ("aranav", 60)
]
marks = list(map(lambda x: x[1], students))
average = sum(marks) / len(marks)
print("Average:", average)
above_75 = list(filter(lambda x: x[1] > 75, students))
print("Above 75:", above_75)
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted:", sorted_students)






employees = [
    ("Anurag", "Data", 60000),
    ("Ashish", "HR", 45000),
    ("Anuja", "IT", 70000)
]
high_salary = list(filter(lambda x: x[2] > 50000, employees))
print(high_salary)
increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
print(increased)
sorted_emp = sorted(employees, key=lambda x: x[2])
print(sorted_emp)




products = [
    ("mouse", 700, 1),
    ("Bag", 800, 2),
    ("Laptop", 50000, 1)
]
values = list(map(lambda x: (x[0], x[1] * x[2]), products))
print(values)
expensive = list(filter(lambda x: x[1] > 1000, products))
print(expensive)
sorted_products = sorted(values, key=lambda x: x[1])
print(sorted_products)





words = ["strawberry", "pineapple", "rabbit", "laptop", "dog", "elephant"]
lengths = list(map(lambda x: len(x), words))
print("Lengths:", lengths)
long_words = list(filter(lambda x: len(x) > 5, words))
print("Long words:", long_words)
sorted_words = sorted(words, key=lambda x: len(x))
print("Sorted:", sorted_words)









































