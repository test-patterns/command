""" Sample problem featuring the command pattern. """

class Order():
    """ A pizza order """

    def __init__(self, quantity, size, crust, toppings):
        """ Initializes a new order """
        self.quantity = quantity
        self.size = size
        self.crust = crust
        self.toppings = toppings
