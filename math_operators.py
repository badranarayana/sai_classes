Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# +, -, /, //, *, %
# example on +
20 + 30
50
20.5 + 30
50.5
age = 30
age
30
type(age)# used to find the object data type
<class 'int'>
age = 40
type(age)
<class 'int'>
type(30)
<class 'int'>
# example on +
# write a program to find the sum of all salaries
emp1_sal = 3000
emp2_sal = 5000
emp3_sal = 5000
total = emp1_sal + emp2_sal + emp3_sal # 3000 + 5000 + 5000
total
13000
# int + int
10 + 20 # valid
30
10 + '30' # not valid? + operation won't support between data type int and string
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    10 + '30' # not valid? + operation won't support between data type int and string
TypeError: unsupported operand type(s) for +: 'int' and 'str'
#<left operand>  + <right operand>
10 + 30
40
# int + float
20 + 30.5 # valid?
50.5
# note: experesion always return float if one of operand is float
type(30.4)
<class 'float'>
30.5 + 20.5
51.0
20 + 30
50
# 10 + 30 # Valid
# 20.5 + 30 # valid
# 30.5 + 30.5 # valid
# 30.5 + '333.5' # invalid
# list + list
[1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
# list + tuple
[1, 2, 3] + (6, 7, 8)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    [1, 2, 3] + (6, 7, 8)
TypeError: can only concatenate list (not "tuple") to list
(6, 7, 8) + [1, 2, 3]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    (6, 7, 8) + [1, 2, 3]
TypeError: can only concatenate tuple (not "list") to tuple
(55,555) + (33,33)
(55, 555, 33, 33)
# list + list ? valid
# list + tuple ? Invalid
# tuple + tuple ? Valid
1,6,8 + 4,5,6
(1, 6, 12, 5, 6)
1, 4, 5
(1, 4, 5)
# -
# substraction
# int - int
30 -4
26
4 -40
-36
# int - float
30 - 55.7
-25.700000000000003
44.77 - 4
40.77
[1, 2,3] - [4,5,6]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    [1, 2,3] - [4,5,6]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
[1] - 4
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    [1] - 4
TypeError: unsupported operand type(s) for -: 'list' and 'int'
[1] - [4]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    [1] - [4]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
20 - '44'
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    20 - '44'
TypeError: unsupported operand type(s) for -: 'int' and 'str'
'44' - '44'
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    '44' - '44'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
'44' + '44'
'4444'
'44' + '12'
'4412'
# *
# int * int
20 * 20
400
# int * float
33 * 44.6
1471.8
# float * float
33.4 * 44.6
1489.6399999999999
# int * str
2 * 'sai'
'saisai'
sai
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    sai
NameError: name 'sai' is not defined
3 * 'sai '
'sai sai sai '
3 *      'sai'
'saisaisai'
3*'sai'
'saisaisai'
2 * [1,2,3]
[1, 2, 3, 1, 2, 3]
3 * [1,2,3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
2 * [1,2]
[1, 2, 1, 2]
# [1,1, 2,2]
sorted(2 * [1,2])
[1, 1, 2, 2]
# /
20/5
4.0
20//5
4
# %
30 % 2
0
100 % 20
0
100 % 33
1
# even number
num = 20
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

Even
# real time program
shirt_price = 1000
GST = 18
# GST = (1000 * 18)/100
# total bill = shirt_price + GST
GST = (1000 * 18)/100
GST
180.0
shirt_price + GST
1180.0
