haveLength = False 
upCase = False 
lowCase = False 
haveNum = False 
verifyCount = 0 
print("Answer the following questions about your password with a 'Yes' or 'No'")
lengthTest = input("Are there more than 6 characters in your password? ")
if lengthTest.lower() == "yes":
    haveLength = True
    verifyCount += 1
else:
    haveLength = False
upperTest = input("Is there at least one uppercase letter? ")
if upperTest.lower() == "yes":
    upCase = True
    verifyCount += 1
else:
    upCase = False
lowerTest = input("And is there a lower case letter? ")
if lowerTest.lower() == "yes":
    lowCase = True
    verifyCount += 1
else:
    lowCase = False
numTest = input("Finally, does your password have a number in it? ")
if numTest.lower == "yes":
    haveNum = True
    verifyCount += 1
else:
    haveNum = False
if verifyCount >= 3:
    print("Your password is valid!")
else:
    print("Your password is invalid. Please try again")