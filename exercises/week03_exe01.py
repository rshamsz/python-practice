#! /usr/bin/env python3
from rich import print 
import sys
from IPython.display import clear_output

baseSubnet = "192.168.254."
askAgain = True
# Asking for a valid subnet length
clear_output()
while askAgain:
    try :
        mask = int (input (f"enter a subnet mask that its length is between 25 and 30: ") )
        if mask > 30 or mask < 25 : 
            print (f" {mask} is a wrong lenght, Try it again!")
        else :
            askAgain = False
    except :
        print ("Wrong input, it should be an integer number")

subnetSize = 2 ** (32 - mask)
print (f"{'-' * 20}\nThe subnet size is: {subnetSize}\n")
hostNumber = subnetSize - 2
print (f"{'-'*20}\nThe number of hosts in each subnet is:{hostNumber}\n")
numberOfSubnets = int (255 / subnetSize)

print (f"Subnets:\nNumber of subnets: {numberOfSubnets}\n\t")
for i in range (numberOfSubnets + 1) :
    print (f"Subnet Number: {baseSubnet}{i * subnetSize}\n\t")
    
print (f"{'-' * 20}\nThe first host IP of the first subnet is: {baseSubnet}1\n")
print (f"{'-' * 20}\nThe last host of the firsty subnet is: {baseSubnet}{hostNumber}")

#os.system("clear")