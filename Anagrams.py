def check(s1, s2):
    if(sorted(s1) == sorted(s2)):
        print("The string are anagrams        ")
    else:
        print("The strings are not anagrams      ")

s1=input("Enter a string")
# input1: "listen"
s2 =input("enter second string")
# input2: "silent"
check(s1, s2)

# Output: the strings are anagrams.