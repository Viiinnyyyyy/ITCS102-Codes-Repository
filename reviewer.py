age = int(input("ENTER YOUR AGE --->  "))
rev = float(input('HOW MUCH IS YOUR MONTHLY REVENUE? --->  '))
cs = int(input("WHAT IS YOUR CREDIT SCORE? --->  "))
years = float(input("HOW LONG ARE YOUR BUSINESS IN THE INDUSTRY? --->  "))
defa = eval(input("DID YOU ALREADY FILE FOR BANKRUPCY? --->  "))
col = input("WHAT IS YOUR COLLATERAL? --->  ")
colval = float(input("HOW MUCH DOES  YOUR COLLATERAL WORTH? --->  "))

maxloan = 0
basefee = 0

if age >= 21 and defa == False and years >= 2.0 :
    print("YOU PASSED THE BASELINE")
    if cs >= 720 :
        print("YOUR CREDIT SCORE IS VERY HIGH")
        maxloan = rev * 3
        print("YOUR MAX LOAN OFFER IS",maxloan)
        if rev >= 50000 :
            basefee = maxloan * 0.015
            print("YOUR BASE FEE IS", basefee)
        else:
            basefee = maxloan * 0.025
            print("YOUR BASE FEE IS", basefee)
        if colval >= maxloan :
            print("COLLATERAL ",col," WITH THE VALUE OF ",colval,' IS ACCEPTED')
        else:
            print("REJECTED: INSUFFUCIENT COLLATERAL VALUE FOR ",col)
        surgefee = maxloan * basefee
        print("ADDITIONAL CHARGE OF ",surgefee)
        if maxloan % 5000 :
            print("ADDITIONAL CHARGE ADDED") 
            surgefee += 250
            print("UPDATED BASE FEE IS ", surgefee)

    elif 620 <= cs <= 720 :
        print("GOOD CREDIT SCORE")
        maxloan = rev * 1.5
        print("YOUR MAX LOAN OFFER IS", maxloan)
        if years >= 5.0 :
            basefee = maxloan *  0.02
            print("YOUR BASE FEE IS", basefee)
        else : 
            basefee = maxloan * 0.035
            print("YOUR BASE FEE IS", basefee)
        if colval >= maxloan :
            print("COLLATERAL ",col," WITH THE VALUE OF ",colval,' IS ACCEPTED')
        else:
            print("REJECTED: INSUFFUCIENT COLLATERAL VALUE FOR ",col)
        surgefee = maxloan * basefee
        print("ADDITIONAL CHARGE OF ",surgefee)
        if maxloan % 5000 :
            print("ADDITIONAL CHARGE ADDED") 
            surgefee += 250
            print("UPDATED BASE FEE IS ", surgefee)

    elif 1 <= cs < 620:
        print("SCORE TOO LOW")
    else:
        print("INVALID")
else:
    print("REJECTED")