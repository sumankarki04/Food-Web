mar=""
age=0
gen=''
while True:
    mar=input("Enter your marital status (u for unmarried, M for married:")
    if mar=="m":
        print("you are insured")
    elif mar=="u":
        gen=input("Enter gender(m/f)?")
        age=int(input("Enter your age"))
        if gen>="m" and age>=30:
            print("you are insecured despite beign male and unmarried")
    elif gen=="f" and age>=25:
        print("you are insured despite beign female and unmarried ")
    else:
        print("you are not insured and unsecured")
        ch=input("press(e) to exit")
        if ch.lower()=="e":
            break
        

