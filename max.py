# def max(a, b):
#     if (a> b):
#        return a
#     else:
#         return b

# a= int(input("enter a number"))
# b=int(input("ENter number"))

# # max(a,b)
# print(max(a,b))




# Min value to check


# def min(a, b):
#     if(a<b):
#         return a
#     else:
#         return b
# print(min(a, b))


#  to check the number is maximum or minimum


# num =int(input("Enter a number"))

# def numCheck():
#     if num>0:
#         print(num, " is a maximum number")
#     else:
#         print(num, "is minmum number")

# numCheck()

# Write a program to find a maximum of three numbers

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
        
    return largest
a = int(input("Enter a number: "))
# Input1: 20
b = int(input("Enter a number: "))
# Input2: 14
c = int(input("Enter a number: "))
# Input3: 12
print(maximum(a, b, c))
# Output: 20

def mimimum(x, y, z):
    if (x>=y) and (x>=z):
        smallest =x
    if (y>=x) and (y>=z):
        smallest =y    
    else:
        smallest = z
    print(smallest, "is the smallest number")

x = int(input("enter a number"))
y= int(input("enter number"))
z= int(input("enter number"))

print(mimimum(x, y, z))
