#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

filename = "arubacx_show_vlan.txt"
vlans = {}
clear_output()

def tolist (str) :
    intf_list = str.split(",")
    vlan_intf = []
    for item in intf_list :
        if '-' in item :
            index = item.index('-')
            first_intf = int (item[index-1])
            last_intf = int (item [-1])
            intf_pfx = item[0:index-1]
            vlan_intf += [f"{intf_pfx}{i}" for i in range (first_intf,last_intf+1)] 
        else :
            vlan_intf.append(item)
    return vlan_intf
                         
with open (filename , mode = "r", newline ="") as file :
    data  = file.readlines()
    for line in data :
        columns = line.split()
        if not columns[0].strip().isdigit() :
            continue
        vlans[int (columns[0])] = set (tolist(columns[5].strip()))


# Pritning results
print (f"{'-' * 40}\n") 
print ("The list of interfaces that are common between vlans 1,2,3:\n",
       f"{(vlans[1] & vlans [2] & vlans [3] )}\n")
print (f"{'-' * 40}\n") 
# This is wrong
# print ("The list of interfaces that are associaed with any vlan:\n",
#        f"{(vlans[1] ^ vlans [2] ^ vlans [3] )}") 
print ("The list of interfaces that are associaed with any vlan:\n",
       {intf for intf_set in vlans.values() for intf in intf_set})
print (f"\n {'-' * 40}\n") 
print ("The list of interfaces that are associaed with vlan 12 or vlan13:\n",
       f"{(vlans[12] | vlans [13])}") 