Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=[2,5,8,6,10,16]
a=print('hi how r u?')
hi how r u?
a
a
print(a)
None
def myfun():
    print('this is first fun')

    
myfun()
this is first fun
a=myfun()
this is first fun
print(a)
None
def second():
    return 'abc'

second()
'abc'
b=second()
print(b)
abc
def third(x):
    print('hello')

    
third()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
third('abc')
hello
def fourth(x):
    return x*10

fourth(2)
20
def fourth(x):
    print('hi')
    print('hello')
    print('how are you')
    return x*21

fourth(3)
hi
hello
how are you
63
def fourth(x):
    print('hi')
    return x**2
    print('hello')

    
fourth(2)
hi\
4
fourth(2)
hi
4
def five(x,y,z):
    return x+y+z

five(12,2,23)
37
def six(x):
    return x*7,x+7,x/7

six(2)
(14, 9, 0.2857142857142857)
five(y=2,x=4,z=6)
12
five(2,4)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    five(2,4)
TypeError: five() missing 1 required positional argument: 'z'
def seven(x,y,z=1):
    return x+y+z
seven(4,8,7)
SyntaxError: invalid syntax
seven(4,8,7)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    seven(4,8,7)
NameError: name 'seven' is not defined
def seven(x,y,z=1):
    return x+y+z

seven(4,8,7)
19
seven(4,8)
13
def seven(x=1,y,z=1):
    return x+y+z
SyntaxError: non-default argument follows default argument
def seven(x,y=1,z):
    return x+y+z
SyntaxError: non-default argument follows default argument
def seven(x,y=1,z=1):
    return x+y+z

seven(3)
5
def eight(*x):
    return x
eight()
SyntaxError: invalid syntax
def eight(*x):
    return x

eight()
()
eight(2)
(2,)
\
eight(2,3,4)
(2, 3, 4)
\
eight(2,3,4)
(2, 3, 4)
def nine(**x):
    return x

nine()
{}
nine(name='ashish',email='ashishlekhyani.cse25@jecrc.ac.in.com')
{'name': 'ashish', 'email': 'ashishlekhyani.cse25@jecrc.ac.in.com'}
nine(n1=0,n2=[11,10,20],n3=['ab','xy'])
{'n1': 0, 'n2': [11, 10, 20], 'n3': ['ab', 'xy']}
def ten(x):
    x=input('Enter the name of the person whose birthday it is: ')
    print('Happy birthday to you , Happy birthday to dear ')
    return x

ten()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    ten()
TypeError: ten() missing 1 required positional argument: 'x'
def ten():
    x=input('Enter the name of the person whose birthday it is: ')
    print('Happy birthday to you , Happy birthday to dear ')
    return x

ten()
Enter the name of the person whose birthday it is: Ashish
Happy birthday to you , Happy birthday to dear 
'Ashish'
def birthday(name):
    print(f'happy birthday to {name}')

    
birthday(Ashish)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    birthday(Ashish)
NameError: name 'Ashish' is not defined
def birthday('name'):
    print(f'happy birthday to {name}')
    
SyntaxError: invalid syntax
def birthday(name):
    print('Happy birthday to you')
    print(f'happy birthday to dear {name}')

    
birthday('Ashish')
Happy birthday to you
happy birthday to dear Ashish
def ten():
    x=input('Enter the name of the person whose birthday it is: ')
    print(f'Happy birthday to you , Happy birthday to dear {x} ')

    
ten
<function ten at 0x00000174B32D9090>
ten()
Enter the name of the person whose birthday it is: Ashish
Happy birthday to you , Happy birthday to dear Ashish 

five = lambda x,y,z:x+y+z
myadd(5,9,7)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    myadd(5,9,7)
NameError: name 'myadd' is not defined
five(5,9,7)
21
import math
math.pi
3.141592653589793
math.sqrt(81)
9.0
math.pow(2,3)
8.0
math.factorial(5)
120
import math as m
m.pi
3.141592653589793
m.sqrt(81)
9.0
from math import sqrt
sqrt(81)
9.0
import datetime as dt
aaj_ki_date=dt.date.today()
print(aaj_ki_date)
2022-09-19
import calendar
print(calender.calender(2022))
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print(calender.calender(2022))
NameError: name 'calender' is not defined. Did you mean: 'calendar'?
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

>>> print(calender.month(2022,9))
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print(calender.month(2022,9))
NameError: name 'calender' is not defined. Did you mean: 'calendar'?
>>> print(calendar.month(2022,9))
   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

