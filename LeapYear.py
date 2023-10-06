def leapYear(Year):


    if ((Year%400==0) or (Year%100!=0) and (Year%4==0)):
        print("the given year is leap year")
    else:
        print("the  given is not a leap year")

Year= int(input("enter the year"))

leapYear(Year)
