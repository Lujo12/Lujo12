userPrime = int(input("Please enter any number greater than 1: "))
n = 2
toggle = 0
if userPrime <= 1:
    while userPrime <= 1:  
        userPrime = int(input("That is not a number greater than one. Please enter a number greater than 1. "))
if userPrime > 1:
    while n < userPrime:
        userPrime/n
        if userPrime % n == 0:  
            toggle = 1  
            print(str(userPrime) + " is not a prime number!")
            break  
        n = n + 1  
    if toggle == 0:  
        print(str(userPrime) + " is a prime number!")  

 