#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

#define the parent class
class NetworkDevice :
    def __init__(self,host) -> None:
        self._host = host
    
    @property
    def host (self) :
        return self._host
    

#Define a child class of parent class "NetworkDevice"
class Router (NetworkDevice) :
    def __repr__(self) -> str:
        return (f"Router ('{self.host}')")

#Define a child class of parent class "NetworkDevice"
class Switch ( NetworkDevice) :
    def __repr__(self) -> str:
        return (f"Switch ('{self.host}')")

#Define a child class of parent class "NetworkDevice"
class AccessPoint ( NetworkDevice) :
    def __repr__(self) -> str:
        return (f"AccessPoint ('{self.host}')")


#Define one instance of each child class
rtr1 = Router ("rtr1.test.com")
sw1 = Switch ("sw1.test.com")
ap1 = AccessPoint ("ap1.test.com")

#Print out the instances attributes
print (f"{rtr1.host=}")
print (rtr1)
print (f"{sw1.host=}")
print (sw1)
print (f"{ap1.host=}")
print (ap1)

clear_output()
