Python 3.15.0b3 (tags/v3.15.0b3:cf16a33, Jun 23 2026, 10:03:50) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=15
>>> a+b
25
>>> a-b
-5
>>> a*b
150
>>> a/b
0.6666666666666666
>>> a//b
0
>>> a && b
SyntaxError: invalid syntax
>>> a and b
15
>>> a or b
10
>>> a +=
SyntaxError: invalid syntax
>>> a +=3
>>> a+=3
>>> a==b
False
>>> a !=b
True
>>> a=b
>>> a+=3
>>> a
18
>>> a-=4
>>> a
14
>>> a*=5
>>> a
70
>>> a/=2
>>> a
35.0
>>> a//=3
>>> a
11.0
>>> x<y and x>y
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x<y and x>y
NameError: name 'x' is not defined
x=56
y=89
x<y and x>y
False
x>y or x<y
True
x>y not x<y
SyntaxError: invalid syntax
h=10
n=m>j
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    n=m>j
NameError: name 'm' is not defined
d=40
p=60
s=p>d
not s
False
list=[1,2,3,3, 4, 5, 6 ,7 ,8]
6 in list
True
9 not in list
True
list.append(43)
list
[1, 2, 3, 3, 4, 5, 6, 7, 8, 43]
tuple=(5,6,7,89)
tuple.append(87)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tuple.append(87)
AttributeError: 'tuple' object has no attribute 'append'. Did you mean to use a 'list' object?
list[5]
5
tuple[5]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tuple[5]
IndexError: tuple index out of range
tuple[3]
89
set={1,6,7,8,9,50 }
set
{1, 50, 6, 7, 8, 9}
set[4]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    set[4]
TypeError: 'set' object is not subscriptable
dict=[1:5,2:"t"]
SyntaxError: invalid syntax
dict=[1:"5" , 2"y"]
SyntaxError: invalid syntax
dict=[0:"gh" ,1:"tg" ,2:"we"]
SyntaxError: invalid syntax
dict={1:"jk" ,2:"ml"}
dict
{1: 'jk', 2: 'ml'}
{1: 'jk', 2: 'ml'}
{1: 'jk', 2: 'ml'}
dict={1:"5" , 2"y"}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
dict=[1:"5" , 2:"y"]
SyntaxError: invalid syntax
list.insert(4,55)
list
[1, 2, 3, 3, 55, 4, 5, 6, 7, 8, 43]
list.extend(34,67,45)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    list.extend(34,67,45)
TypeError: list.extend() takes exactly one argument (3 given)
list.extend([88,99,77])
list
[1, 2, 3, 3, 55, 4, 5, 6, 7, 8, 43, 88, 99, 77]
list.remove(5)
list
[1, 2, 3, 3, 55, 4, 6, 7, 8, 43, 88, 99, 77]
list.pop()
77
