"""
Conditional statements are used to make decisions based on conditions


1) if statement/condition
2 if .. else
3) if..elif .. else

"""
"""
syntax:
if <condition statement/expression>:
    pass

"""
#example #1:
if 5 > 10:
    print("inside if block")
# note: python used indentation(4 spaces) for defining the blocks

print("Out side if block")


# example #1:
# even number or odd
num = 9
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# write a program to check the ration card eligibility?
# income = less than 40000
# four_wheel should be hold

income = 30000
have_4_wheeler = False
thresold_income = 40000

if income <= thresold_income and not have_4_wheeler:
    print("You are eligible for white card")
else:
    print("Sorry, note eligible.")

# note: else will execute only when if condition failed

"""
elif syntax
----------
if <cond>:
    pass
elif <cond>:
    pass
elif <cond>:
else:
   pass
"""
# write a program to find the suitable vehicle

location = 'chennai'

if location in ['bangalore', 'chennai']:
    print("please prefer flight")
elif location == 'guntur':
    print("Please prefer train")
elif location == 'nalgonda':
    print("Please prefer bus")
else:
    print("Please prefer car")



# write a program to take online order
items = ['fried_rice', 'manchuria', 'noodils']

customer_ordered_item = 'fried_rice'
if customer_ordered_item in items:
    print("Okay, taken order")
else:
    print("Sorry, order not taken due to unavailability")





