#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output
from telnetlib import Telnet
import time
import re
from getpass import getpass


def read ( telnet_conn, sleep = 1.5) :
    time.sleep (sleep)
    data = telnet_conn.read_very_eager ().decode ()
    return ( data )

def write ( telnet_conn, data) :
    byte_data = data.encode()
    telnet_conn.write (byte_data)
 
def login ( telnet_conn, username, password) :
    debug = False
    
    data = read (telnet_conn)
    output = data
    if re.search (user_prompt, data, flags=re.M) :
        write (telnet_conn, f"{username}\n")
        data = read(telnet_conn)
        output += data
        
    if re.search (pass_prompt, data, flags=re.M) :
        write (telnet_conn, f"{password}\n")
        data=read(telnet_conn)
        output += data
        
    if debug :
        print (output)
        
    if re.search (prompt_terminator, data) :
        return True
    else :
        return False
        
def show_cmd (telnet_conn, cmd="show ip interface brief") :
    write (telnet_conn, f"{cmd}\n")
    return ( read (telnet_conn) )
    
if __name__ == "__main__" : 
    host = "192.168.3.11"
    username = "reza"
    user_prompt = r"^Username:\s+"
    pass_prompt = r"^Password:\s+"
    prompt_terminator = r"\w+#"
    password = getpass("What is the password:")    
    
    #Create Telnet connection
    tn = Telnet (host)
    
    status = login (telnet_conn=tn, username=username, password=password) 
    print(f"\nLogin status: {status}\n") 
    output = show_cmd(tn)
    print(f"\n{output}\n")

    output = show_cmd(tn, cmd="show ip arp")
    print(f"\n{output}\n")
    
    clear_output()

    