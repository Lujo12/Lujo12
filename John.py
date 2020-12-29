answer = "John" # The name of the user
nameString = []
nameInput = input("Enter a name") # the name which will be entered 
while nameInput != answer: 
    nameString.append(nameInput)
    nameInput = input("Enter a name") # The correct name which will enetered
print("Incorrect Names: ", nameString)