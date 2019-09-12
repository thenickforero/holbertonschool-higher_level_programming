#!/usr/bin/python3
if __name__ == "__main__":
    def reducer(container, func):
        response = 0
        for i in container:
            response = func(i, response)
        return response

    def add(a, b):
        return int(a) + int(b)
    import sys
    argc = len(sys.argv) - 1
    response = 0
    if argc:
        nums = sys.argv[1:]
        response = reducer(nums, add)
        print(response)
