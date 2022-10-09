Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={'name':['akash','akshat','sunny'],'semester':[2,1,2]}
d1
{'name': ['akash', 'akshat', 'sunny'], 'semester': [2, 1, 2]}
d1['name']+=['bunny']
d1
{'name': ['akash', 'akshat', 'sunny', 'bunny'], 'semester': [2, 1, 2]}
d1['name']+='bunny'
d1
{'name': ['akash', 'akshat', 'sunny', 'bunny', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'][1]+=['ashish']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d1['name'][1]+=['ashish']
TypeError: can only concatenate str (not "list") to str
d1['name'][1]=['bunny']
d1['name'][3]=['akshat']
d1
{'name': ['akash', ['bunny'], 'sunny', ['akshat'], 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'][1]='bunny'
d1['name'][3]='akshat'
d1
{'name': ['akash', 'bunny', 'sunny', 'akshat', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['name'].insert(1,'ashish')
d1
{'name': ['akash', 'ashish', 'bunny', 'sunny', 'akshat', 'b', 'u', 'n', 'n', 'y'], 'semester': [2, 1, 2]}
d1['sem']=d1.pop('semester')
d1
{'name': ['akash', 'ashish', 'bunny', 'sunny', 'akshat', 'b', 'u', 'n', 'n', 'y'], 'sem': [2, 1, 2]}
#f-string/string format
a='Akshat'
b='Upflairs'
'hi'
'hi'
f'Hi {a} welcome to {b}'
'Hi Akshat welcome to Upflairs'
f'Hi {b} welcome to {a}'
'Hi Upflairs welcome to Akshat'
'Hi {} welcome to {}'.format('Akshat','Upflairs')
'Hi Akshat welcome to Upflairs'
for i in [1,2,3,4,5]:
    print(i)

    
1
2
3
4
5
for i in('a','b','c','d'):
    print(i)

    
a
b
c
d
for i in 'Helloworld':
    print(i)

    
H
e
l
l
o
w
o
r
l
d
for i in "HelloWorld":
    print('HelloWorld')

    
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
for x in "HelloWorld":
    print(x)

    
H
e
l
l
o
W
o
r
l
d
for x in "HelloWorld":
    print(x)
    print('hello')

    
H
hello
e
hello
l
hello
l
hello
o
hello
W
hello
o
hello
r
hello
l
hello
d
hello
for x in "HelloWorld":
    print(x)
    print('hello')
 print('helloworld')
 
SyntaxError: unindent does not match any outer indentation level
for x in "HelloWorld":
    print(x)
    print('hello')
print('helloworld')
SyntaxError: invalid syntax

============================== RESTART: D:/Training/p2.py ==============================
H
hello
e
hello
l
hello
l
hello
o
hello
W
hello
o
hello
r
hello
l
hello
d
hello
helloworld
for i in range(6):
    print(i)

    
0
1
2
3
4
5
for i in range(1,6):
    print(i)

    
1
2
3
4
5

============================== RESTART: D:/Training/p2.py ==============================
Traceback (most recent call last):
  File "D:/Training/p2.py", line 3, in <module>
    t.insert(t+1)
AttributeError: 'int' object has no attribute 'insert'

============================== RESTART: D:/Training/p2.py ==============================
Traceback (most recent call last):
  File "D:/Training/p2.py", line 3, in <module>
    t.append(t+1)
AttributeError: 'int' object has no attribute 'append'

============================== RESTART: D:/Training/p2.py ==============================
13 16 19 21 

============================== RESTART: D:/Training/p2.py ==============================
[13, 16, 19, 21]

============================== RESTART: D:/Training/p2.py ==============================
Traceback (most recent call last):
  File "D:/Training/p2.py", line 11, in <module>
    if x>10 and x%2 and x==t[i]:
NameError: name 'x' is not defined

============================== RESTART: D:\Training\p2.py ==============================
Traceback (most recent call last):
  File "D:\Training\p2.py", line 11, in <module>
    if t>10 and t%2:
TypeError: '>' not supported between instances of 'list' and 'int'

============================== RESTART: D:\Training\p2.py ==============================
15

============================== RESTART: D:\Training\p2.py ==============================
15

============================== RESTART: D:\Training\p2.py ==============================
12
15
18
20
16

============================== RESTART: D:\Training\p2.py ==============================
12
18
20
16

============================== RESTART: D:\Training\p2.py ==============================
Hello
Hello
Hello
Hello
Hello

============================== RESTART: D:\Training\p2.py ==============================
Traceback (most recent call last):
  File "D:\Training\p2.py", line 21, in <module>
    while true:
NameError: name 'true' is not defined. Did you mean: 'True'?

============================== RESTART: D:\Training\p2.py ==============================
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loop
This loop is an infinite loopTraceback (most recent call last):
  File "D:\Training\p2.py", line 22, in <module>
    print('This loop is an infinite loop')
KeyboardInterrupt
>>> 
============================== RESTART: D:\Training\p2.py ==============================
10
9
8
7
6
5
4
3
2
1
>>> 
============================== RESTART: D:\Training\p2.py ==============================
1
2
abc
23
20
>>> 
============================== RESTART: D:\Training\p2.py ==============================
1
2
abc
>>> 
============================== RESTART: D:\Training\p2.py ==============================
