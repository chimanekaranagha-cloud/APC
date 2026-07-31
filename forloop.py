n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)




n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i) 



n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)




n = int(input("Enter number of terms: "))

a = 1

for i in range(n):
    print(a, end=" ")
    a = a * 2



n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)



x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 1

for i in range(1, n + 1):
    fact = 1
    power = 2 * i

    for j in range(1, power + 1):
        fact = fact * j

    term = (x ** power) / fact

    if i % 2 == 1:
        sum = sum - term
    else:
        sum = sum + term

print("cos(x) =", sum)




import math

n = int(input("Enter number: "))

root = int(math.sqrt(n))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

print("Square Root =", root)

if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")




for i in range(3):
    print("A B C")



n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()




n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()





n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()    



    

       