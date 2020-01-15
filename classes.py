class Pizza:
    def __init__(self, size, style):
        self.size = size
        self.style = style
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def list_toppings(self):
        toppings_string = ""
        if len(self.toppings) == 1:
            toppings_string += self.toppings[0] + "."
        elif len(self.toppings) == 2:
            for topping in self.toppings:
                if self.toppings.index(topping) == len(self.toppings) -1:
                    toppings_string += f" and {topping}."
                else:
                    toppings_string += topping
        elif len(self.toppings) > 2:
            for topping in self.toppings:
                if self.toppings.index(topping) == len(self.toppings) -1:
                    toppings_string += f"and {topping}."
                else:
                    toppings_string += f'{topping}, '

        return toppings_string
        
    def print_order(self):
        message = f'I would like a {self.size}, {self.style} pizza.'
        if self.toppings:
            message = f'{message[:-1]} with {self.list_toppings()}'
            print(message)
        else:
            print(message)
        

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."

my_pizza = Pizza("large", "hand-tossed")
my_pizza.add_topping("pepperoni")
my_pizza.add_topping("mushrooms")
my_pizza.add_topping("green peppers")
print(len(my_pizza.toppings))
my_pizza.print_order()

