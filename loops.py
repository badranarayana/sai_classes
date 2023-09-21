"""
Loops in python
--------------
used to execute the business logic repeatedly until loop ends

1) for loop
2) while loop
3) nested loop

"""
"""
for loop:
* for loop is used to iterate over the sequence of elements
* loop will end after end of sequence iteration

syntax:
------
for <var> in <iterable/sequence>:
    <statements>


iterable/sequence --> like list, tuple, string etc..
"""

# for num in [1, 2, 3]:
#     print(num)

# for color in ['green', 'red', 'blue']:
#     print(color)


# write a program to print 1 to 10 numbers except 4 and 8
for i in range(1, 11):
    if i not in [4, 8, 3]:
        print(i)


# write a program to print all your friend names start with S char?
friends_list = ['ravi', 'somu', 'banu', 'sai']
filter_char = 's'

for name in friends_list:
    first_char = name[0]
    if first_char == filter_char: # s == s
        print(name)


