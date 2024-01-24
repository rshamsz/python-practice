#! /usr/bin/enc python3
from rich import print
from IPython.display import clear_output

filename = "show_ip_int_brief.txt"
mapping = {}
clear_output()

with open (filename, mode ="r", newline="") as datafile :
    ip_intf = datafile.readlines()
    print (type(ip_intf),"\n",ip_intf)
    for line in ip_intf :
        line_items = line.split()
        intf_name = line_items[0].strip()
        ip_addr = line_items[1].strip()  
        if ip_addr not in ["unassigned","IP-Address"] :
            mapping[intf_name] = ip_addr
print (mapping)
   
