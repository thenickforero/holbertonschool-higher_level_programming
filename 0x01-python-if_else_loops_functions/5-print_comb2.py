#!/usr/bin/python3
for i in range(0, 100):
    print("{:s}".format(str(i) if i > 9 else "0" + str(i)),
          end="\n" if i == 99 else ", ")
