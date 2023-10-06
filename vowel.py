string=input("enter the string")

if string in ('a', 'e', 'i', 'o', 'u'):
    print("vowel")
else:
    print("consonant")

# #Python Program to Find Vowels From a String
#defining a function

def get_vowels(String):
    return [each for each in String if each in "aeiou"]

get_string1 = "Tabasum"
get_string2 = "kouser"
get_string3 = "Tabasum Kouser"

print("The Vowels Are:  ",get_vowels(get_string1))
print("The Vowels Are:  ",get_vowels(get_string2))
print("The Vowels Are:  ",get_vowels(get_string3))