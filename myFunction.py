WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']

def days_of_week(y_run):
    y_run = print(" ----> ".join(WEEKDAYS))
    return y_run
days_of_week(WEEKDAYS)
NIGHTS = int(input(
    "\nRequest user to enter the number of nights you will be staying\nat the Hotel @ R 3,899.99 / night: "))
DESTINATIONS = {'1. Cape Town': 3840.99,'2. Venice': 13820.99, '3. Dublin': 15471.99}
print("\nFlights available to:\n" + str(DESTINATIONS)
      [1:-1] + "\n") 

PLANE = int(
    input("Plane Ticket: Request user to enter the number that match your destination in the list above: "))
CARRENTAL = int(
    input("\nRequest user to enter how many days you will be renting a car for @ R1200 / day: "))
def hotel_cost(hc_cost):
    price_per_night = 3899.99
    hc_cost = round(NIGHTS * price_per_night, 2)
    return hc_cost
def plane_ticket(pt_cost):
    if PLANE == 1:
        pt_cost = DESTINATIONS['1. Cape Town']
    if PLANE == 2:
        pt_cost = DESTINATIONS['2. Venice']
    if PLANE == 3:
        pt_cost = DESTINATIONS['3. Dublin']
    return pt_cost
def car_rental(c_rent):
    price_per_day = 1399.00
    c_rent = round(CARRENTAL * price_per_day, 2)
    return c_rent
def total_holiday_cost(hc_cost, pt_cost, c_rent):
    hotel_costing = hotel_cost(hc_cost)
    plane_t_costing = plane_ticket(pt_cost)
    car_rent_costing = car_rental(c_rent)
    return hotel_costing + plane_t_costing + car_rent_costing
print(
    f"\nTotal cost of the holiday is: R {round(total_holiday_cost(NIGHTS, PLANE, CARRENTAL), 2)}")
