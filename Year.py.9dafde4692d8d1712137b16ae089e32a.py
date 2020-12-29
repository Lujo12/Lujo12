year = int(input("Enter the Start Year"))
amount = int(input("h"))
end = year + amount
for i in range(year, end):
  if i % 4 != 0:
    print(i,"Is leap year")
  else:
    print(i, "Is not a leap year")