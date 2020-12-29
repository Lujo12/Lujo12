x = float(input('Enter a number: '))
y = float(input('Enter a number: '))
z = x+y/2
# The order of operations in arithmetic (the division is evaluated before addition) the program will not give the right answer:
print ('The average of the two numbers you have entered is:',z) 

# To rectify this problem, we will simply add the parentheses: z = (x+y)/2
z = (x+y)/2
#At the end of an if, elif, else, for, while, class, or def statement. (Causes “SyntaxError: invalid syntax”)
if z == 3
print('Hello!')