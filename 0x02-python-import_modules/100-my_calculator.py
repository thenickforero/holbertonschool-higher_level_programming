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
    if len(argv) > 1:
        a = int(argv[1])
        b = int(argv[3])
        operation = argv[2]
        c = operations.get(operation)
        result = c(a, b)
        print('{:d} {:s} {:d} = {:d}'.format(a, operation, b, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
