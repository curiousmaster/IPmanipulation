#! /usr/bin/python


from netaddr import *
import pprint
import sys
from lib.args import *


TOT=0

def main():
        global TOT

        ARGS = parseArgs()

        for line in open(ARGS['file'],"r"):
            line = line.strip()
            if "-" in line:
                s,e = line.split('-')

                s = IPAddress(s)
                e = IPAddress(e)
                TOT += len(range(s,e+1))

            else:
                TOT += 1


        print TOT

if __name__ == "__main__":
    main()
