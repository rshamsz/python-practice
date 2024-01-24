#! /usr/bin/env python3
from typing import List
from rich import print
from IPython.display import clear_output
from dataclasses import dataclass

#define the RouterFacts class
@dataclass
class RouterFacts : 
    hostname: str
    vendor: str
    network_os: str
    model: str
    os_version: str
    interfaces: list [str]
    uptime_sec : int
    serial_numner : str
    

#instantiate from the class RouterFacts
router1 = RouterFacts (
    hostname = 'la-rtr1',
    vendor =  'cisco',
    network_os =  'iosxr',
    model = '8201-SYS',
    os_version = '7.0.12',
    interfaces=   [
        'HundredGigE0/0/0/24',
        'HundredGigE0/0/0/25',
        'HundredGigE0/0/0/26',
        'HundredGigE0/0/0/27',
        'HundredGigE0/0/0/28',
        'HundredGigE0/0/0/29',
        'HundredGigE0/0/0/30',
        'HundredGigE0/0/0/31',
        'HundredGigE0/0/0/32',
        'HundredGigE0/0/0/33',
        'HundredGigE0/0/0/34',
        'HundredGigE0/0/0/35',
        'MgmtEth0/RP0/CPU0/0'
    ],
    uptime_sec = 93073,
    serial_numner = 'FOC2291AVYB'    
)

#print the class instance
print (router1)
clear_output()