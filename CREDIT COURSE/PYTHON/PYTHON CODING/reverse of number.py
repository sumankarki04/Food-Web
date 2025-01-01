a = int(input("Enter a number: "))
rev = 0

while a > 0:
    c = a % 10
    rev= (rev * 10) + c
    a = a // 10

print("Reversed number:", rev)
