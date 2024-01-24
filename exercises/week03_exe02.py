#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

#Readinig the file
filename = "show_ip_int_brief.txt"
network = "10.220."
intf_name = []
ip_addr = []
interfaces = {}
clear_output()
with open (filename, mode = "r", newline ="") as read :
    file = read.readlines ()
    for line in file :
        if network in line :
            intf_name.append(line.split()[0])
            ip_addr.append (line.split()[1])
            interfaces[line.split()[0]] = line.split()[1]


print (intf_name,ip_addr)
print (interfaces)