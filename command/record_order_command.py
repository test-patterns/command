""" Sample problem featuring the command pattern. """

from command import Command

class RecordOrderCommand(Command):
    """ A command to record a new order """

    def execute(self):
        """ Base method to execute the commmand """
        pizza = "pizza"
        if int(self._order.quantity) > 1:
            pizza = "pizzas"
        print("Recorded a new pizza order: " +
              self._order.quantity + " " +
              self._order.size + " " +
              self._order.crust + " " + pizza + " with " +
              self._order.toppings)
