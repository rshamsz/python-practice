#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output
import re

filename = "show_version.txt"
with open (filename, mode="r", newline= "") as f :
    data = f.read()
    ## Method#1
    
    # model = r"^cisco\s(C\d+-\w).*$"
    # serial_number = r"^Processor.*ID\s(\w+)$"
    # match = re.search (model, data, flags=re.MULTILINE )
    # if match :
    #     model = match.group(1)
    # match = re.search (serial_number, data, flags=re.MULTILINE )
    # if match :
    #     serial_number = match.group(1)
    
    ## Method#2
    model = re.findall (r"cisco\s(C\d+-\w).*",data)
    serial_number = re.findall (r"Processor.*ID\s(\w+)",data)  

print()
print("#" * 25)
print(f"{model=}")
print(f"{serial_number=}")
print("#" * 25)
clear_output()
