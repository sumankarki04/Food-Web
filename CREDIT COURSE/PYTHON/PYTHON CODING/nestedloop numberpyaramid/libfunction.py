c = input("Enter a character: ")
c=c.lower()

if len(c) != 1 or not c.isalpha():
    print("Enter a single alphabetic character.")
elif c in "aeiou":
    print("Vowel")
else:
    print(f"{c} is a consonant")
