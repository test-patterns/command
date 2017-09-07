""" Sample problem featuring the command pattern. """

class Command(object):
    """ An interface for commands """

    def __init__(self, order):
        self._order = order

    def execute(self):
        """ Base method to execute the commmand """
        raise NotImplementedError
