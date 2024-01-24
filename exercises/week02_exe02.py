#! /usr/bin/env python3

from rich import print

filename = "show_version.txt"
header_chars = "-" * 80
header = f"[deep_sky_blue4]{header_chars}[/deep_sky_blue4]"

#Open the file
f = open (filename,"r")
data = f.read()
f.close()

firstline = data.splitlines()[0]
allLines=   data.splitlines()

print (f"The 'data' type is: {type (data)}" )
print (header)
data = data.splitlines()
print (f"The 'data' type is: {type (data)}" )
print (header)
print (f"The 'firstline' type is: {type (firstline)}" )
print (f"\nThe first line is:\n {firstline}")
print (header)
print (f"\nThe 2nd line is:\n {allLines[1]}")
print (header)

print (header)
with open (filename, mode="r") as f:
    data = f.readlines()
print (f"The 'data' type is: {type (data)}" )
print (header)
print (f"\nThe first line is:\n {data[0].strip()}")
print (header)
print (f"\nThe 2nd line is:\n {data[1].strip()}")
print (header)
