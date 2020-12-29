import math
b_num = list(input("Input a binary number: ")) # A binary number is inputted 
value = 0 # the value

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)