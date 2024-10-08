# Grant Washington
# 10/06/24
# P2Lab
# program that creates a dictionary with key and value pairs

cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
keys = cars.keys()
print(keys)
vehicle_entered = input("Enter vehicle to see is mpg:")
print(f'The {vehicle_entered} gets {cars.get(vehicle_entered)} mpg.')
miles = float(input("How many miles are you planning on driving?"))
gallons_needed = (miles/cars.get(vehicle_entered))
print(f'{round(gallons_needed,2)} gallon(s) of gas are needed to drive the {vehicle_entered} {miles} miles.')
