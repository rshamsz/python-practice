#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output
from telnetlib import Telnet
import time
import re
from getpass import getpass

host = "192.168.3.11"
username = "reza"
user_prompt = r"^Username:\s+"
pass_prompt = r"^Password:\s+"
password = getpass()

def read ( telnet_conn, sleep = 1.5) :
    time.sleep (sleep)
    data = telnet_conn.read_very_eager ().decode ()
    return ( data )

def write ( telnet_conn, data) :
    byte_data = data.encode()
    telnet_conn.write (byte_data)
     
#Create Telnet connection
tn = Telnet (host)
d = read (tn)
if re.search (user_prompt, d , flags=re.M) :
    write (tn, f"{username}\n")
    d= read (tn)    
    #print (d)
    
if re.search (pass_prompt, d, flags=re.M) :
    write (tn, f"{password}\n")
    d= read (tn)
    print (d)
    
clear_output()

    