print("Hello, World")

if 5>2:
    print("five is greater than two!")

# This is comment
print("Hello, World") #this is comment

# print("Hello, World")
# print("Hello, World")
# print("Hello, World")

x=8
y="Jon"
print(x)
print(y)

x=str(3)
y=int(3)
z=float(3)
print(x)
print(type(x))  # this is to recognise type

print(y)
print(z)

# Assign Multiple variables in one line
a,b,c ="Orange", "Mango", "Orange"
print(a)
print(b)
print(c)
# can display all the items in one print statements
print(a,b,c)

A="Tabasum"
B=34
# print one  number and text
print(A,B)


# GLobal variables and create a functions

x="Tabasum"
def myFunct():
    print("My name is " + x)

myFunct()

# creating same name as global variable declared before

m="Fantastic"

def myFunction():
    m="Awesome"
    print("My phython is " + m)

myFunction()

print("my python is " + m)

# used global variable inside function 

def myFunction1():
    global y
    y="Fantastic"
myFunction1()  
print(y)


for i in "Mango":
    print(i)


# using for loop in function

def MyName():
    for i in "Tabasum":
        print("Name "+i)

MyName()
a = "Hello, World!"
print(len(a))

u="tammy"
print(len(u))

# To check specific word in a text

text="I love You"

print("love" in text)
print("'love'" not in text)

print("hate" in text)


if  "love" in text:
    print("yes, 'love' is present")

if "hate" not in text:
    print("No, 'hate' is NOT present")

r="Taqi,Ur Zaki Ur"

print(r[0:3])
# print from start to the postion
print(r[:4])

# print from position two to the end

print(r[4:])

# make a all the letter are in lower letter
lowerLetter="HeLLo World"
print(lowerLetter.lower())


UpperLetter="fklsdlskd"
print(UpperLetter.upper())

# Assign multiple string to a three single  quote or three double quote

ab= """Hello, 
I am Tabasum Kouser,
completed higher diploma in web development."""

print(ab)




am="    Hello ,world!          "
print(am.strip())   #strip used to remove white spaces starting or end

ai=" Hello, Tabasum"
print(ai.replace("H", "B"))    #replace method used to replace string

ao=" Hello, Tabasum"
print(ai.replace("Tabasum", "Taby"))    #replace method used to replace string


Ae="Tabasum & Kouser"
be=Ae.split(" , ")
print(be)


w="Zaki"
y="Taq"
z=w+y  # + operetor used to merge to string
print(z)

# Add a space between two letters
n= w + " & "+ y
print(n)

# string format
age=36
txt1="My name is Tabasum and my  age {}"

print(txt1.format(age))












