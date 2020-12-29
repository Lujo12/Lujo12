year = int(input("Enter the Start Year"))
amount = int(input("Enter the end year"))
end = year + amount
for i in range(year, end):
  if i % 4 != 0:
    print(i,"Is leap year")
  else:
    print(i, "Isn't a leap year")