Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# identity operatos
x = [1, 2, 3]
y = [1, 2, 3]
x is y
False
x = x
z = x
z
[1, 2, 3]
x
[1, 2, 3]
x is z
True
x is not z
False
x is not y
True
# int
age = 10
age1 = 10
age is age1
True
val1 = (1, 2, 3)
val2 = (1, 2, 3)
val1 is val2
False
name = "sai"
name1 = "sai"
name is name1
True
name2 = "Sai"
name is name2
False
name2 = "Sai, Manasvi"
# mutable
# imutable
