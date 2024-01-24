#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

filename = "junos_show_arp.txt"
mapping = {}
with open (filename , mode = "r", newline ="") as reader :
    data = reader.readlines()
    for line in data :
        items = line.strip().split()
        if items[1] and "." in items[1]:
            mac_addr = items[0].replace (":", "-")
            ip_addr = items[1]
            mapping [ip_addr] = mac_addr
print (mapping)
clear_output()
    