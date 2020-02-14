#! /usr/bin/python
# ======================================================================
# NAME
#   range2ip.py    - Generate IP list of addresses from ranges
#
# SYNOPSIS
#   ranges2ip.py {FILE}
#
# DESCRIPTION
#   This script will take a file with list of IP addresses and ranges
#   and produce a sorted list IP addresses.
#
#   Example:
#       10.100.1.2
#       10.100.1.5-10.100.1.7
#       10.2.10
#
#       ...will generate...
#       10.100.1.2
#       10.100.1.5
#       10.100.1.6
#       10.100.1.7
#       10.100.2.10
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
# create_ip()
#   Create list of IP addresses from IP addresses and ranges
# --------------------------------------------------
def create_ip(data):

    iplist = []
    for line in data:
        if "-" not in line:
            iplist.append(line)
        else:
            ipstart, ipend = line.split("-")
            for ip in range(ipaddress.ip_address(unicode(ipstart)),ipaddress.ip_address(unicode(ipend))+1):
                iplist.append(ipaddress.ip_address(ip))

    return iplist

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

    data = create_ip(data)

    for x in data:
        print x

    sys.exit()

    data = sortList(data)

    for ip in data:
        print(ip)


if __name__ == "__main__":
    main()
