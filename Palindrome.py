# UserString=input("please enter a string   ")

# reverseString= UserString[::-1]

# if(UserString==reverseString):
#     print(UserString," given string is palindrome    ")
# else:
#     print(UserString," given  string is not palidrome     ")


#  To check for number is palindrome or not
# n=int(input("enter number"))
# x=n
# rev=0
# while x>0:
#     r=x%10
#     rev= rev*10+r
#     x=x//10

#     print("Rever of given number is" , rev)

#     if rev==n:
#         print(n, "is a plaindrome")
#     else:
#         print(n, "is not a plaindrome")

# To check the palindrome

num=int(input("enter a number"))

temp=num

reverse= 0
while temp > 0:
    remaider= temp%10
    reverse=(reverse *10) + remaider
    temp= temp//10

if num == reverse:
    print("Palidrome")
else:
    print("Not Palindroem")
    

