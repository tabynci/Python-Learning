# def pattern(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print("* ", end="")
#         print("\r")

# n=5
# pattern(n)


# Another method

# num= int(input("Enter the number"))

# for i  in range(1, num+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# def myfunc(n):
#     k=n-1
#     x= n+1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k-1
#         for j in range(0, i+1 ):
#             print("*", end=" ")
#         print("\r")
   
# # n=5    we can call that an argument inside athat functions
# myfunc(10)

# Write a program to print the following pyramid pattern.

# number =int(input("enter the  number for pyramid"))

# for i in range(0, number):
#     for j in range(0, number-1-i):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()


# Print number pattern
# def num(n):
#     num =1
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print(num, end="")
#             num= num+1
#         print()
# n=5
# num(5)


# Pyramid type with same number

# def pyramidNumber(numbers):

#     numbers=int(input("enter number"))

#     for i in range(0, numbers):
#         for j in range(0, numbers-i-1):
#             print( end=" ")
#         for j in range(0, i+1):
#             print(numbers, end=" ")
            
#         print()
# numbers=5
# pyramidNumber(numbers)

# pyramid type with different number

# def pyDifferentN(number):
#     number=int(input("enter number"))
#     num=1
#     for i in range(0, number):
       
#         for j in range(0, i+1):
#             print(num, end=" ")
#             num = num+1
#         print()
# number=5
# pyDifferentN(number)

# to print character pattern

# def character(n):
#     n=int(input("enter number of characters to print"))
#     num=65
#     for i in range(0, n):
#         for j in range(0, i+1):
#             ch = chr(num)
#             print(ch, end=" ")
#             num=num+1
#         print()
# n=5
# character(n)


def alphabets(n):
    n=int(input("enter the number of characters to print"))
    num=65
    for i in range(0, n):
        for j in range(0, n-i-1):
            print(end=" ")
        for j in range(0, i+1 ):
            ch = chr(num)
            print(ch, end=" ")
            num= num+1
        print()
n=5
alphabets(n)
