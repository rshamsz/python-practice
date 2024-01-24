#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

#Define the parent calss 'NetworkDevice'
class NetworkDevice :
    def __init__(self, host) -> None:
        self._host = host
        
    @property
    def host (self) : 
        return self._host
    
#Define a child class of 'NetworkDevice" class
class Router (NetworkDevice) : 
    def __init__(self, *args , **kwargs ) :
        if "model" in kwargs:
            self.model = kwargs.pop ("model")
        else :
            self.model = None
        return super().__init__(*args , **kwargs)
    
    def __repr__(self) -> str:
        return (f"Router ('{self.host}')")
    
    def print_model (self) :
        if self.model is None  : 
                raise ValueError ("Model is not set")
        else :
            print (self.model)
        
   
   #Define a child class of parent class "NetworkDevice"
class Switch ( NetworkDevice) :
    def __repr__(self) -> str:
        return (f"Switch ('{self.host}')")

#Define a child class of parent class "NetworkDevice"
class AccessPoint ( NetworkDevice) :
    def __repr__(self) -> str:
        return (f"AccessPoint ('{self.host}')")
    
     
#Create a Router class instance
rtr1 =  Router ("rtr1.test.com", model="c9300")
print (f"{rtr1.host=}, {rtr1.model=}")
print (rtr1)
rtr1.print_model()
print ("*" * 50)
rtr2 =  Router ("rtr2.test.com")
print (f"{rtr2.host=}")
print (rtr2)
rtr2.print_model()

clear_output()

