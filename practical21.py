n = int(input("Enter a number: "))

if n == 0:
    print("The number is Zero")
else:
    print("The number is Non-Zero")


print("_____________________________________")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)



print("_____________________________________")


n = int(input("Enter a number: "))

if n >= 0:
    print("The number is Positive")
else:
    print("The number is Negative")


print("_____________________________________")



ch = input("Enter a character: ")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("It is a Vowel")
else:
    print("It is a Consonant")

print("_____________________________________")

marks=float(input("Enter the marks: "))
if marks >=90:
          print("excellent performances")
elif marks >=80:
          print("very good performances")
elif marks >=70:
          print("good performances")
elif marks >=60:
          print("average performances")
else:
          print("poor performances")

print("_____________________________________")

num1 = int(input("Enter  num1: "))
num2= int(input("Enter  num2: "))
num3 = int(input("Enter num3: "))


if num1 > num2:
    if num1>num3:
         print("num1 is largest")
    else:
        print("num3 is largest")
else:
    if num2 > num3:
        print("num2 is largest")
    else:
        print("num3 is largest")

print("_____________________________________")

num1 = int(input("Enter  num1: "))
num2= int(input("Enter  num2: "))
num3 = int(input("Enter num3: "))


if num1 < num2:
    if num1<num3:
         print("num1 is smallest")
    else:
        print("num3 is smallest")
else:
    if num2 < num3:
        print("num2 is smallest")
    else:
        print("num3 is smallest")
print("_____________________________________")

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

print("_____________________________________")

if (y% 4 == 0):
    if (y % 100==0):
        if (y %400==0):
            print( "is a Leap Year")
        else:
             print( " not a Leap Year")
     else:
         print( "is a Leap Year")
else:
     print( " not a Leap Year")

print("_____________________________________")

married = input("Is the driver married? (yes/no): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if married.lower() == "yes":
    print("Driver is Insured")

elif married.lower() == "no":
    if gender.lower() == "male" and age > 30:
        print("Driver is Insured")
    elif gender.lower() == "female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")


print("_____________________________________")


             
     
    
            


        



        
    

    
    
    
          
          
    
          
          


    



