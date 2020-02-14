#! /usr/bin/python
# ======================================================================
# NAME
#   ip2ranges.py    - Generate IP ranges from list of IP addresses
#
# SYNOPSIS
#   ip2ranges.py {FILE}
#
# DESCRIPTION
#   This script will take a file with list of IP addresses and produce
#   a sorted list of IP ranges.
#
#   Example:
#       10.100.1.6
#       10.100.1.5
#       10.100.1.7
#       10.100.2.10
#       10.100.1.2
#
#       ...will generate...
#       10.100.1.2
#       10.100.1.5-10.100.1.7
#       10.2.10
#
# AUTHOR
#   14 Apr, 2020 / Stefan Benediktsson
#
# ======================================================================

import sys
import operator
import itertools
import collections
import ipaddress
import csv


# --------------------------------------------------
# readList()
#   Read a list of IP addresses
# --------------------------------------------------
def readList(file):
    with open(file) as fp:
        data = fp.read().splitlines()

    return data


# --------------------------------------------------
# sortList()
#   Sort a list of IP addresses
# --------------------------------------------------
def sortList(data):

    tmp = []
    sortedData = []
    for ip in data:
        tmp.append(ipaddress.ip_address(unicode(ip)))

    tmp.sort()

    for ip in tmp:
        sortedData.append(str(ip))

    return sortedData


# --------------------------------------------------
# create_range()
#   Create a list of single IP addresses and ranges
# --------------------------------------------------
def create_range(ip_addresses):
    ranges=[]
    range=""
    ip_prev = "1.1.1.1"

    for line in ip_addresses:

        ip = line

        if len(range) == 0:
            range = ip
        else:
            ipn = ipaddress.ip_address(unicode(ip))
            ipp = ipaddress.ip_address(unicode(ip_prev))
            if ipp == ipn-1:
                range = range.split("-")[0] + "-" + ip

            else:
                ranges.append(range)
                range = ip

        ip_prev = ip

    if range not in ranges:
        ranges.append(range)

    return ranges


# ------------------------------
# main()
# ------------------------------
def main():

    if len(sys.argv) > 1:
        file = sys.argv[-1]
    else:
        print(sys.argv[-1] + ": missing file argument")
        sys.exit()

    data = readList(file)
    data = sortList(data)


    ranges = create_range(data)

    for range in ranges:
        print(range)


if __name__ == "__main__":
    main()
