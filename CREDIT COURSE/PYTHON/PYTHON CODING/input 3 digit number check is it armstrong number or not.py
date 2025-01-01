a = int(input("Enter a number: "))
m = a  
p = 0

while a > 0:
    c = a % 10
    p = p + c ** 3  
    a = a // 10

if m == p:
    print(f" is an Armstrong number.")
else:
    print(f"is not an Armstrong number.")
