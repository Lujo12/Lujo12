n = 0
addNumber = 0
while(True):
    number = int(input("please eneter a number:"))
    addNumber += number
    n += 1
    if number == -1:
        break
n = n -1
addNumber = addNumber + 1
average = round (addNumber/n, 2)
print ("You've entered the following amount of numbers: "+ str(n))
print ("They add up to: "+ str(addNumber))
print ("And their average is:"+ str (average))


