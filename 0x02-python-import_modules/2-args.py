#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    print("{} ".format(count), end="")
    if count == 0:
<<<<<<< HEAD
        print("argument.")
=======
        print("arguments.")
>>>>>>> aef00195b751a939343ba680191e91b1f194056e
    else:
        if count == 1:
            print("argument:".format(count))
        else:
            print("arguments:".format(count))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
