#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    response = []
    data = 0
    for i in range(list_length):
        try:
            data = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            data = 0
            print("{:s}".format('division by 0'))
        except TypeError:
            data = 0
            print("{:s}".format('wrong type'))
        except IndexError:
            data = 0
            print("{:s}".format('out of range'))
        finally:
            response.append(data)
    return response
