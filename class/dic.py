my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key,val in my_vehicle.items():
    print(key,val)

vehicle2 = my_vehicle.copy()

print(vehicle2)

vehicle2["number_of_tires"] = 4

del vehicle2["mileage"]

print(vehicle2)