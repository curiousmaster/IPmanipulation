#! /bin/python

import argparse

def parseArgs():
    global ARGS

    ap = argparse.ArgumentParser(description="PF configuration parser")
    ap.add_argument("-f", "--file", required=True, help="parse file")

    ARGS = vars(ap.parse_args())

    return ARGS
