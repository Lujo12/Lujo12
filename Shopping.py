item1=input("Please enter the name of item 1 on your shopping list: ")
item2=input("Please enter the name of item 2 on your shopping list: ")
item3=input("Please enter the name of item 3 on your shopping list: ")
price1=float(input("Please enter the price of item 1 on your shopping list(to the nearest cent) :R "))
price2=float(input("Please enter the price of item 2 on your shopping list(to the nearest cent) :R "))
price3=float(input("Please enter the price of item 3 on your shopping list(to the nearest cent) :R "))
total=round(price1+price2+price3,2)
avg_price=round(total/3,2)
print(f"The total for  {item1 } {item2} {item3} is R {total} and the average price per item is R {avg_price}")