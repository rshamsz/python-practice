#!/usr/bin/env python3
from rich import print
import emoji

# Life is better with emojis
celebration = emoji.emojize(":confetti_ball: ")
party = emoji.emojize(":party_popper: ")
balloons = emoji.emojize(":balloon: ")


_BaseAddr = "192.168.254."
_maskLength = int (input ("Enter the subnet lenght between 25 to 30: "))
while _maskLength> 30 or _maskLength < 25 :
    _maskLength = int (input ("Enter the subnet lenght between 25 to 30: "))

_numOfHosts = 2 ** ( 32 - _maskLength ) -2

banner_chars = "-" * 80
banner = f"[deep_sky_blue4]{banner_chars}[/deep_sky_blue4]"
print(banner)

print (f"The number of available hosts in this subnet is {_numOfHosts}")
print (f"The fist network number is {_BaseAddr}0\n")
print (f"The 2nd subnet is {_BaseAddr}{_numOfHosts +2}\n")
print (f"The first address of the first subnet is {_BaseAddr}1")
print (f"The last address of the first subnet is {_BaseAddr}{_maskLength-1}")

print(f"\n{celebration}{party}{balloons}\n")