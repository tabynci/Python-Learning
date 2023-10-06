# Write a program to find a factorial of a number

import math
# num= int(input("enter number"))

# factorial= 1

# if num <0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1" )

# else:
#     for i in range(1, num+1):
#         factorial= factorial*i
#     print("The factorial of", num, "is" , factorial)


# Another method

def factorial(num):
    return(math.factorial(num))

num = int(input("enter number"))

print("the factroial of ", num, "is", factorial(num))