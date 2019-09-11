#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if i % 3 == 0:
            print("{:s}".format("Fizz"), end=" ")
        if i % 5 == 0:
            print("{:s}".format("Buzz"), end=" ")
        if i % 5 != 0 and i % 3 != 0:
            print(i, end=" " if i != 100 else "")
