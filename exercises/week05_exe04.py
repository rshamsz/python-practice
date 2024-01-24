#! /usr/bin/env python3
import re
from rich import print
from IPython.display import clear_output

filename = "show_lldp.txt"

with open (filename, mode="r", newline="") as f :
    data = f.read()
    pattern = r"Chassis.*?Vlan ID: not advertised"
    remote_port_regex = f"^Port id:\s+(?P<remote_port>\S+)$"
    local_port_regex = f"^Local Port id:\s+(?P<local_port>\S+)$"
    remote_sys_regex = f"^System Name:\s+(?P<remote_sys>\S+)$"
    match = re.findall (pattern, data, flags=re.DOTALL)
    if match :
        print()
        print (f'{"Local port":^20}{"Remote Port":^20}{"Remote System":^20}') 
        for item in match :
            pattern = (
                rf"{remote_port_regex}.*{local_port_regex}.*{remote_sys_regex}"
            )
            info = re.search (pattern, item, flags=re.MULTILINE | re.DOTALL)
            if info :
                print (f"{info.group('remote_port'):^20}{info.group('local_port'):^20}{info.group('remote_sys'):^20}")
        print("-" * 25)         
           
clear_output()