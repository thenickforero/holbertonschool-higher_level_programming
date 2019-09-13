#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as data
    names = dir(data)
    for i in names:
        if not i.startswith('__'):
            print('{:s}'.format(i))
