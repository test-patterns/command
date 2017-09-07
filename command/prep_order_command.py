""" Sample problem featuring the command pattern. """

from command import Command

class PrepOrderCommand(Command):
    """ A command to prep an order """

    def execute(self):
        """ Base method to execute the commmand """
        for _ in range(int(self._order.quantity)):
            print("Prepped 1 " + self._order.size + " " + self._order.crust + " crust")
            for topping in self._order.toppings.split(','):
                print("Prepped 1 " + topping.strip())
