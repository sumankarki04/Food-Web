a = int(input("Enter a number: "))
rev = 0
d=0
while a > 0:
    c = a % 10
    rev= (rev * 10) + c
    a = a // 10

d=rev+a


print("Reversed number:", rev)
print("sum of reverse  number:",d)
