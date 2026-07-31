
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height

print("Area of Triangle =", area)


pi = 3.14

r = float(input("Enter radius: "))

volume = (4/3) * pi * r * r * r

print("Volume of Sphere =", volume)




side = float(input("Enter side: "))

area = side * side

print("Area of Square =", area)


pi=3.14
r=float(input("enter radius: "))
h=float(input("enter height: "))
totalsurface= 2 * pi * r * h
print("total surface of cylinder =",totalsurface)



pound = float(input("Enter weight in pounds: "))

kg = pound * 0.453592

print("Weight in Kilograms =", kg)


km = float(input("Enter distance in kilometers: "))

miles = km * 0.621371

print("Distance in Miles =", miles)


n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)



n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")





n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")





n = int(input("Enter a decimal number: "))

print("Binary =", bin(n))




n = int(input("Enter a decimal number: "))

print("Octal =", oct(n))





n = int(input("Enter a decimal number: "))

print("Hexadecimal =", hex(n))




n = int(input("Enter a number: "))

print("Factors are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)




n = int(input("Enter ASCII value: "))

print("Character =", chr(n))       





    




      
      



             
