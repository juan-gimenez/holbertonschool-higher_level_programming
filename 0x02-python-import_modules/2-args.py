#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments.".format(len(sys.argv) - 1))        
