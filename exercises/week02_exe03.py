#! /usr/bin/env python3

from rich import print
line_separator = "*" * 80

ip_list = ["1.1.1.1", "1.1.1.2", "1.1.1.3", "1.1.1.4", "1.1.1.5"]
print (f"Intial IP list:\n {ip_list}")
print (line_separator)

#a. Add individual addresses using append()
ip_list.append("1.1.1.6")

#b. Add a list of new addresses using extend()
ip_list.extend (["2.1.1.1","2.1.1.2"])

#c. Let's concatenate as well...
ip_list +=  ["3.1.1.1","3.1.1.2"]

#d. Printing
print (f"IP addresses after all the additions: \n {ip_list}\n")
print (f"Printing the first IP:\n {ip_list[0]}\n")
print (f"Printing the last IP address in the list:\n {ip_list[-1]}")
print (line_separator)

#e. Remove some addresse
ip_list.pop(0)
ip_list.pop()

# f. Change the new first address
ip_list[0] = "2.2.2.2"

# g. Print out final list of addresses.
print(f"Printing the first new IP address:\n {ip_list}")