n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i += 1


n = int(input("Enter n: "))
i = 2
while i <= n:
    print(i)
    i += 2


n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i += 2


n = int(input("Enter n: "))
i = 1
s = 0
while i <= n:
    s += i
    i += 1
print("Sum =", s)



n = int(input("Enter n: "))
i = 1
s = 0
while i <= n:
    s += i
    i += 2
print("Sum =", s)



n = int(input("Enter n: "))
i = 2
s = 0
while i <= n:
    s += i
    i += 2
print("Sum =", s)



n = int(input("Enter n: "))
while n >= 1:
    print(n)
    n -= 1



n = int(input("Enter n: "))
a = 0
b = 1
i = 1
while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1



n = int(input("Enter number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial =", fact)




n = int(input("Enter number: "))
i = 2
count = 0
while i < n:
    if n % i == 0:
        count += 1
    i += 1

if count == 0 and n > 1:
    print("Prime")
else:
    print("Not Prime")



n = int(input("Enter number: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum =", s)



n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")



n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reverse =", rev)



n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1




n = int(input("How many numbers: "))
i = 1
largest = int(input("Enter number: "))
while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i += 1
print("Largest =", largest)



n = int(input("How many numbers: "))
i = 1
smallest = int(input("Enter number: "))
while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i += 1
print("Smallest =", smallest)




