import math
P=float(input("Please enter the amount you would like to deposit : R"))
i=float(input("Please enter the interest rate(as percentage. e.g . 8: "))
t=int(input("Please enter the number of years of the investment: "))
interest=input("Please enter wheater you want simple or compund interest:")
intUpper=interest.upper()
if intUpper == "SIMPLE":
    simpleCalc = round(P *(1 + ((i/100)*t)), 2)
    print(str(simpleCalc))
elif intUpper == "COMPOUND":
    compoundCalc = round(P * math.pow((1+(i/100)), t), 2)
    print(str(compoundCalc))
else:
    print("It seems you have entered invalid entry, kindly start again.")