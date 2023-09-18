Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Examples on ==
# write a program to check two persons age same or not
age1 = 25
age2 = 25
age1 == age2 # 25 == 25 ? True
True
age2 = 30
age1 == age2 # 25 == 30 ? False
False
name = 'sai'
name1 = 'reddy'
name == name1
False
name1 = 'Sai'
name == name #? False, Python is case sensitive lanagus
True
name == name1
False
# !=
salary1 = 2000
salary2 = 3000
# give 500 hike to employe of less salary
salary1 != salary2
True
emp_loc = 'hyd'
emp2_loc = 'bng'
emp_loc != emp2_loc
True
# <
# give 500 hike to employe of less salary
sal1 = 200
sal2 = 400
sal1 < sal2 # 200 < 400? True
True
sal2 < sal1 # 400 < 200? False
False
if sal1 < sal2: # 200 < 400 ? True
    sal1 = sal1 + 500
    print("Sal 1", sal1)
else:
    sal2 = sal2 + 500
    print("Sal 2", sal2)

Sal 1 700
sal1 = 500
sal2
400
if sal1 < sal2: # 500 < 400 ? False
    sal1 = sal1 + 500
    print("Sal 1", sal1)
else:
    sal2 = sal2 + 500
    print("Sal 2", sal2)

Sal 2 900
'333' > '3'
True
'a' > 'A'
True
'A' > 'a'
False
ord('A')
65
ord('a')
97
ord('b')
98
ord("B")
66
ord("Z")
90
ord("z")
122
# >
30 > 20
True
20 > 30
False
'a' > 'A'
True
# comparion happen through asci values
# <=
20 < 20
False
pub_allowed_age = 18
peron_age = 18
if peron_age >= pub_allowed_age: # 18 >= 18 ? True
    print("Allowed")

Allowed
peron_age = 19
if peron_age >= pub_allowed_age: # 18 >= 18 ? True
    print("Allowed")

Allowed
peron_age = 17
if peron_age >= pub_allowed_age: # 18 >= 18 ? True
    print("Allowed")

if peron_age >= pub_allowed_age: # 18 >= 18 ? True
    print("Allowed")