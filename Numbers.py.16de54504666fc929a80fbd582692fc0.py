userNum1 = int(input("Please enter number 1: "))
userNum2 = int(input("Please enter number 2: "))
userNum3 = int(input("Please enter number 3: "))
num_list = [userNum1, userNum2, userNum3]
print("The list of integers are: " + str(num_list))
sum_list = sum(num_list)
print("The sum of all the integers is: " + str(sum_list))
first_second = userNum1 - userNum2
print("The first number minus the second number is: " + str(first_second))
third_prod_first = userNum3 * userNum1
print("The third number multiplied by the first number is: " + str(third_prod_first))
sum3_div_third = (sum_list)/userNum3
print("The sum of all the numbers divided by the third number is: " +
      str(sum3_div_third))