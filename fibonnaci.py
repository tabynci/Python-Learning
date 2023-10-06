# Write a program to find a fibonacci of a number.
nterms=int(input("how many terms"))

n1, n2=0,1
count=0
if nterms<=0:
    print("Enter positive number")
elif nterms==1:
    print("Fibonacci series upto", nterms,":")
    print(n1)
else:
    print("Fibonnaci series")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1    
