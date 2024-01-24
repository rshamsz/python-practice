#! /usr/bin/env python3
import pexpect, os
from rich import print
from IPython.display import clear_output

def read_hosts (filename) :
    with open (filename, mode="r", newline="") as f :
        data = f.readlines()
        hosts = [ line.strip().split(",") for line in data if line.strip() ]
    return hosts
        
def login (tel_conn, username, password,prompt = "#") :
    tel_conn.expect ('[Uu]sername:')
    tel_conn.sendline (username)
    tel_conn.expect('[Pp]assword:')
    tel_conn.sendline(password)
    enable_status = tel_conn.expect(['>','#'])
    if not enable_status :
        tel_conn.sendline ('enable')
        tel_conn.expect ('[Pp]assword:')
        tel_conn.sendline (password)
        tel_conn.expect (prompt)
    tel_conn.sendline("terminal length 0") # Set number of lines on a screen for no pausing
    tel_conn.expect (prompt)
    return None

def send_cmd (tel_conn,cmd,prompt="#") :
    tel_conn.sendline (cmd)
    tel_conn.expect (prompt)
    #output = tel_conn.before.decode('utf-8')
    output = (tel_conn.before).replace ('\r\n', '\n')
    return output
            
if __name__ == "__main__" :
    commands = ["show ip int bri","show ip arp"]
    while True :
        filepath = input ("Enter the filename (default: 'hosts.txt'):") \
                   or "inputfiles/hosts.txt"
        if os.path.isfile (filepath) :
            print ( "Found the file :)")
            break
        else :
            raise ValueError ( "The file does not exist!")         
    hosts = read_hosts (filepath)
    results = {}
    for host in hosts :
        tel_conn = pexpect.spawn (f'telnet {host[0]}', timeout= 10, encoding="utf-8")
        login (tel_conn,host[1],host[2])
        for cmd in commands :
            results [f'{host[0]}-{cmd}'] = send_cmd (tel_conn,cmd) 
        print (f'"{host[0]} is done!\n"{"#"*40}')
        tel_conn.close()
    print (results)
    clear_output()    
        
    
        
     