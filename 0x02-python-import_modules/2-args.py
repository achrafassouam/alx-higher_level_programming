#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)

    if (num_args - 1) == 1:
        print("{} argument:".format(num_args - 1))
        print("{}: {}".format((num_args - 1), sys.argv[1]))
    elif num_args > 1:
        print("{} arguments:".format(num_args - 1))
        for i in range(1, num_args):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments.".format(num_args - 1))
