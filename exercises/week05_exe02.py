#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output
import re

line = "=" * 40

filename = "show_ip_bgp_neighbors.txt"
with open (filename, mode="r", newline="") as f :
    data = f.read()
    bgp_neighbor = r"BGP neighbor is\s(?P<bgp_neighbor>[\d+\.]+),"
    remote_as = r"remote AS\s(?P<remote_as>\d+),"
    bgp_ver = r"BGP version\s(?P<bgp_ver>\d),"
    remote_routerid = r"remote router ID\s(?P<remote_routerid>[\d+\.]+)"
    bgp_state = r"^\s+BGP state = (?P<bgp_state>[\w]+),"
    
    # Method#2
    bgp_neighbor = re.findall (bgp_neighbor ,data)
    remote_as = re.findall (remote_as ,data)
    bgp_ver = re.findall (bgp_ver ,data)
    remote_routerid = re.findall (remote_routerid ,data)
    bgp_state = re.findall (bgp_state, data)
    
    # Method#1
    pattern = (
        r"^BGP neighbor is\s(?P<bgp_neighbor>[\d+\.]+),\s+remote AS\s(?P<remote_as>\d+),"
    )
    match = re.search (pattern, data, flags=re.MULTILINE)
    if match :
        bgp_neighbor = match.group ("bgp_neighbor")
        remote_as = match.group ("remote_as")
    
    pattern = (
        r"^BGP version\s(?P<bgp_ver>\d),\s+remote router ID\s(?P<remote_routerid>[\d+\.]+)"
    )
    match = re.search (pattern, data, flags=re.MULTILINE)
    if match : 
        bgp_ver = match.group ("bgp_ver")
        remote_routerid = match.group ("remote_routerid")
    
    pattern = r"^\s+BGP state = (?P<bgp_state>[\w]+),"
    match = re.search (pattern, data, flags=re.MULTILINE)
    if match : 
        bgp_state = match.group ("bgp_state")

# Print the output
print (f"{line}\n","Method #1\n",f"{line}\n")
print(f"{bgp_neighbor=}")
print(f"{remote_as=}")
print(f"{bgp_ver=}")
print(f"{remote_routerid=}")
print(f"{bgp_state=}")
print()
#        
print (f"{line}\n","Method #2\n",f"{line}\n")
print(f"{bgp_neighbor=}")
print(f"{remote_as=}")
print(f"{bgp_ver=}")
print(f"{remote_routerid=}")
print (f"{bgp_state=}")
clear_output()
    