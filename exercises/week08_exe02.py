#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

#define Router class
class Rotuer :
    count = 0 
    all_hosts = []
    
    def __init__(self,host) -> None:
        self._host = host
        Rotuer.count += 1
        Rotuer.all_hosts.append (host)
    
    @property
    def host (self) :
        return self._host
    

#instantiate four test instance from the Router class
rtr1 = Rotuer ('r1.test.com')
rtr2 = Rotuer ('r2.test.com')
rtr3 = Rotuer ('r3.test.com')
rtr4 = Rotuer ('r4.test.com')

print ()
print (f"{Rotuer.count=}\n{Rotuer.all_hosts=}") 
clear_output()
        