#! /usr/bin/env python3
from IPython.display import clear_output
from rich import print

#Read the file
filename = "show_ip_int_brief.txt"
intf_name = []
ip_addr = []
ip_intf_map = {}
header = "-" * 40
with open (filename, mode = "r", newline ="") as data :
    lines = data.readlines ()
    for item in lines :
        if "10." in item :
            intf_name.append(item.split()[0])
            ip_addr.append(item.split()[1])
            ip_intf_map [item.split()[0]] = item.split()[1]

print (f"\n{header}\n{intf_name}\n{ip_addr}\n{header}")
print(ip_intf_map)
clear_output()

            