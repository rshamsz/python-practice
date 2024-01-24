#! /usr/bin/env python3
from rich import print

filename = "show_arp.txt"
with open (filename, mode = 'r') as f :
    show_arp = f.readlines()

#a. Print out the Python data type of 'show_arp' variable.
print (f"The {filename} type is:\n {type(show_arp)}")

#b.Print out the length of the 'show_arp' variable.
print (f"The length of the {filename} is:\n {len(show_arp)}")

#c. Print out the header line from the 'show_arp' variable.
print (f"This is the header line from the {filename}:\n {show_arp[0]}")

#d. Print out both the first and the last line of the tabular data from the 'show_arp' variable.
print (f"The first line of the tabular data is:\n {show_arp[1]}" )
print (f"The last line of the tabular data is:\n {show_arp[-1]}" )

#e. Split the header line into fields using the .split() method. Save this into a variable named fields. Print out this 'fields' variable.
fields = show_arp[0].split()
print (f"These are the field names in the {filename}:\n {fields}")

#f. Print out the Python data type of this 'fields' variable.
print (f"The 'fields' data type is: {type (fields)}")

#g. Print out the current number of entries in the 'fields' variable.
print (f"The fields variable has {len (fields)} entries")

#h. Print out the first field and the last field.
print (f"The first entry of the fileds varibale is: '{fields[0]}'\n and the last entry is '{fields[-1]}'")

#i. Fising the columns
fields.remove ('(min)')
index = fields.index("Hardware")
fields [index] = fields [index]+'_'+fields [index +1]
fields.remove ('Addr')
print (f"These are the field names in the {filename}:\n {fields}")
