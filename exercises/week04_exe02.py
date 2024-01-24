#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

intf_list= {}
intf_list2= {}
filename = "show_ip_int_brief.txt"
clear_output()
with open (filename, mode="r", newline="") as file :
    data = file.readlines()
    for line in data :
        items = line.split()
        #ip_addr,
        intf = items[0].strip()
        if intf not in  ["Interface"] :
            intf_list[intf] = {
                "ip_addr" : items[1].strip(),
                "line_status" :items[4].strip(),
               "protocol_status" : items[5].strip()
            }
            #Or this way
            intf_list2[intf] ={}
            intf_list2[intf]["ip_addr" ] = items[1].strip()
            intf_list2[intf]["line_status" ] = items[4].strip()
            intf_list2[intf]["protocol_status" ] = items[5].strip()
           

print (intf_list2)
        
        
