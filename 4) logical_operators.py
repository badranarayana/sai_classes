Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# logical operators
# 1) and
age = 30
# > 29, < 50
age > 29 and age < 50 # True and True --> True
True
age < 29 and age < 50 # False and True --> False
False
age == 10 and age == 20 # False and  False --> False
False
# 2) or
age > 29 or age < 20 # True
True
age < 29 or age < 20 # False
False
not age > 29
False
not age < 29
True
x = 10
not x
False
x = 0
not x
True
x = 'sai'
not x
False
x = ''
not x
True
x = None
not x
True
# Example to find the gretest number
x = 10
y = 30
z = 5
if x > y and x > z:
    print("X is greater val")
elif y > x and y > z:
    print("Y is greater val")
else:
    print("Z is greater val")

Y is greater val
z = 40
if x > y and x > z:
    print("X is greater val")
elif y > x and y > z:
    print("Y is greater val")
else:
    print("Z is greater val")

Z is greater val
y = 100
if x > y and x > z:
    print("X is greater val")
elif y > x and y > z:
    print("Y is greater val")
else:
    print("Z is greater val")

Y is greater val

# write program to check give val is there or not
val = ''
if not val:
    print("Value is empty")

Value is empty
if val:
    print("Value is empty")

val = 3
if val:
    print("Value is empty")

Value is empty
# Write a program to check given number is even number or not
# write a program to check given item in list
# item = 'apple'
# items = ['orage', 'apple', 'banana']
# write a program to check pin code matching or not
# pin_codes = [222, 333, 444, 555, 6666]
