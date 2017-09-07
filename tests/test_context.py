""" Sample problem featuring the command pattern. """

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../command')))

# pylint: disable=E0401,W0611,C0413
from order import Order
