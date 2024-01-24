#!/usr/bin/env python3
line = "Processor board ID FAL127990LA"
check = "Processor board ID" in line
print (f"\nMembership check should be Tru|Flase: {check}")
*junk,SN = line.split()
print (SN)
