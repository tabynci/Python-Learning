# python program to check armstrong number

#Taking the input from user to check armstrong number

# An Armstrong number is a 3 digit number for which the sum of cube of its digits is equal to the number itself. An Armstrong number is a 3 digit number for which the sum of cube of its digits is equal to the number itself. 
num= int(input("Enter Number"))

temp=num

sum=0
while temp >0:
    digit= temp%10
    sum +=digit**3
    temp//=10
if num == sum:
    print(num, "number is Armstrong")
else:
    print(num, "is not an Armstrong number")


# Another method
number=int(input("Enter the number to check armstrong number: "))

arms= number
length= len(str(number))
SUM=0

while number !=0:
    rem= number%10
    SUM = SUM +(rem**length) 
    number= number//10

if arms == SUM :
    print(" The given number", arms, " is armstrong number")
else:
    print("The given number ", arms, "is not an armstrong number")
