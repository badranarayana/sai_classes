"""
loop control statements:
loop control statements are used to control the loop execution
1) continue
2) break

"""

"""
1) continue:
-----------
The continue keyword is used to end the current iteration 
in a for loop (or a while loop), 
and continues to the next iteration
"""

# write a porgam to print 1 to 10 except 4 and 9
for i in range(1, 11): # i = 9
    if i in [4, 9]:# False
        continue

    print(i)

# write a program to print the char in name except vowels
name = 'sai reddy'
for char in name:
    if char in ['a', 'e', 'i', 'o', 'u']:
        continue

    print(char)


"""
break statement:
---------------
--> break statement is used to end/terminate the loop

"""
# write a program to print chars in a name until vowel char reached?
name = "srrr reddy"
for char in name:
    if char in ['a', 'e', 'i', 'o', 'u']:
        break

    print(char)



# write a program to find name in names list?

names = ['sai', 'ramu', 'priya', 'manasvi']
for name in names:
    if name == 'sai':
        print("found")
        break

