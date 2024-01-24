#!/usr/bin/env python3 
ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"

print ("\nstring concatenation\n",ip_addr + " --> " + mac_addr)
print (f"\nf-string\n{ip_addr} --> {mac_addr}")
print ("\nformat() method\n{} --> {}".format(ip_addr, mac_addr))

