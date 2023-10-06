# height=int(input("enter height"))
# base=int(input("enter base"))

# Area = (height*base)/2

# print(Area)


# Another method

# Get the 3 sides of a triangle from the user
s1 = int(input('Enter first side value: '))
s2 = int(input('Enter second side value:'))
s3 = int(input('Enter third-side value:'))

#Calculating the semi-perimeter of a triangle
sp = (s1 + s2 + s3) / 2

#Calculating the area of a triangle
area = (sp*(sp-s1)*(sp-2)*(sp-s3)) ** 0.5

#Printing the area of the triangle
print('The area of the triangle is: ', area)
