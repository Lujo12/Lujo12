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
                  
total = 0
count = 0
num = 0
name = "" 
countName =0
 
while name!="Winnie":
    name =input("Enter your name: ")
    countName +=1
 
print("number of tries to enter correct name: ", countName)
 
while(num!=-1):
    num=int(input("Enter a number: "))
    if num!=-1:
        count+=1
        total +=num
        if num==-2:
            break
 
if count==0:count =1
if num==-2:
    print("Exit without printing chosen")
else:
    average = total/count
    print ("Average is:", average)

                
                
