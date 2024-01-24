#! /usr/bin/env python3

from rich import print
from IPython.display import clear_output
import re

filename = "arista_show_ip_arp.txt"
with open (filename, mode= "r", newline="") as f :
    data = f.read()
    ip_addr = r"\d+\.\d+\.\d+\.\d+"
    mac_addr = r"\w+\.\w+\.\w+"
    pattern = rf"^({ip_addr}).*({mac_addr})\s+Vlan"
    match = re.findall (pattern, data, flags=re.M)
    if match :
        arp_dict = dict (match)
        print (arp_dict)
    clear_output()