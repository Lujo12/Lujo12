menu = ["Espresso", "Cappucino", "Appletiser", "Coke"] #items available on our menu
stock = {"Espresso": 16, "Cappucino": 15, "Appletiser": 20, "Coke": 16,} #Our inventory 
price = {"Espresso": 31.99, "Cappucino": 28.59, "Appletiser": 14.99, "Coke": 11,} #the prices
 
def totalStock(x, y, z): #x = list, y = dictionary, z = dictionary
    totalValue = 0 #total value of all stock
    for i in x: #iterates over the list - uses it has a key for the dictionaries
        totalValue += y[i] * z[i] #how much stock there is multiplied by the price on the menu
    return round(totalValue, 2) #returns the total value, rounded to two places
 
print(totalStock(menu, stock, price)) 

