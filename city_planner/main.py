from building import Building
from city import City

# Create 5 building instances
b1 = Building("123 Street St", 450)
b2 = Building("456 Street Ave", 3)
b3 = Building("8 Eigth Ave", 9)
b4 = Building("223 Baker St", 100)
b5 = Building("7 Wallaby Rd", 1)

# Have each one get purchased by a real estate magnate
b1.purchase("Johnny Johnson")
b2.purchase("Fred Frederickson")
b3.purchase("Natalie Nettles")
b4.purchase("George Washington III")
b5.purchase("Abe Laboriel JR")

# After purchased, construct each one
b1.construct()
b2.construct()
b3.construct()
b4.construct()
b5.construct()

# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

gotham = City("Gotham")

bldgs = [b1, b2, b3, b4, b5]

for bldg in bldgs:
    gotham.add_building(bldg)

for building in gotham.buildings:
    if building.stories == 1:
        print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} story.')
    else:
        print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')
    print()