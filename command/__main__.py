#!/usr/bin/env python
""" Sample problem featuring the command pattern. """

import argparse

from order import Order
from record_order_command import RecordOrderCommand
from prep_order_command import PrepOrderCommand

def main():
    """ Execute the program """
    args = parse_args()
    order = Order(args.quantity, args.size, args.crust, args.toppings)

    RecordOrderCommand(order).execute()
    PrepOrderCommand(order).execute()
    # MakeOrderCommand(order).execute()

def parse_args():
    """ Parse input arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q",
        "--quantity",
        help="The number of pizzas to order.",
        required=True)
    parser.add_argument(
        "-s",
        "--size",
        help="The size of pizza to order.",
        required=True)
    parser.add_argument(
        "-c",
        "--crust",
        help="The type of crust to order.",
        required=True)
    parser.add_argument(
        "-t",
        "--toppings",
        help="A comma-separated list of pizza toppings to order.",
        required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()
