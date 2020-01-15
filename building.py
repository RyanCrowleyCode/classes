import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ''
        self.date_constructed = ''
        self.owner = ''
        self.address = address
        self.stories = stories

    def construct(self):
        cons_date = datetime.datetime.now()
        formatted_date = f'{str(cons_date)[5:7]}/{str(cons_date)[8:10]}/{str(cons_date)[:4]}'
        self.date_constructed = formatted_date

    def purchase(self, name):
        self.owner = name


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

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
buildings = [b1, b2, b3, b4, b5]
for building in buildings:
    if building.stories == 1:
        print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} story.')
    else:
        print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')
    print()

# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.
