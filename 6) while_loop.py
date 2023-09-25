"""
While loop is an condition based loop and
iterate until the condition became false


syntax:
------

while <condition>:
    <statements>

"""
# write a program to print 1 to 10 numbers using while loop

start = 1
end = 10

while start <= end:
    print(start)
    start += 1
print("out side while loop")

# write a program to reverse a string

# index position: 0 to n-1
# hello --> olleh
index = 1
#        -5-4-3-2-1
string = "hello"
#         01234
end = len(string)

out_str = ''
# using -ve index
while index <= end:
    #print(string[-index])
    out_str += string[-index]
    index += 1

print(out_str)

# using +ve index
string = "hello"
start = len(string) - 1 # 5 -1 = 4
end = 0
out = ''
while start >= end:
    out += string[start]
    start -= 1
print(out)


# write a program to print even number between 1 to 20

# start = 1
# end = 20
#
# while start <= end: # 1 <= 20 --> True
#
#     if start % 2 == 0:
#         print("Even number ", start)
#
#     start += 1


# write an interactive program to keep ask for new values
# while True:
#     val = int(input("Please enter value: "))
#     if val % 2 == 0:
#         print("Even number ", val)
#     else:
#         print("odd number ", val)

