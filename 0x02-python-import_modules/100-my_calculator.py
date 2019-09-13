#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, mul, div, sub
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if len(argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
    operator = argv[2]
    operation = operations.get(operator)
    if operation is None:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        result = operation(a, b)
        print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, result))
