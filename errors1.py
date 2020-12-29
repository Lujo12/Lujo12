# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.
print("Welcome to the error program")
print("\n")
ageStr = 24  # I'm 24 years old. This comment has bad structure as it doesn't say much. It should read, "declare variable with age" after the correct structure has been implemented.
age = int(ageStr)
print("I'm " + str(ageStr) + " years old.")
three = 3
answerYears = age + three
print("The total number of years: " + str(answerYears))
answerMonths = (answerYears*12) + 6
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")
# HINT, 330 months is the correct answer
