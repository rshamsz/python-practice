#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

#Define the Interface class
class Interface :
    def __init__(self, intf_name, intf_mode = "access", 
                 access_vlan = 1, speed = "1Gbps", duplex= "full") :
        
        self.intf_name = intf_name
        self.intf_mode = intf_mode
        self.access_vlan = access_vlan
        self.speed = speed
        self.duplex = duplex
        
        if self.intf_mode not in ("access", "trunk") :
            raise ValueError ("Wrong Interface mode, it should be either 'access' or 'trunk'")
        elif self.intf_mode == "access" :
            if not isinstance (self.access_vlan, int) :
                raise ValueError ("The access vlan number is wrong, it should be between (1-4095)")
        else :
            self.access_vlan = None
            
    def __str__(self) :
        if self.access_vlan is None:
            return (f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, "
                    f"Mode: {self.intf_mode})")
        else :
            return (f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, "
                    f"Mode: {self.intf_mode}, Vlan: {self.access_vlan})")            


if __name__ == "__main__" :
    print()
    print ("-" * 50)
    #define the interfaces instances
    intf1 = Interface (intf_name="Et1", access_vlan= 1 )
    intf2 = Interface (intf_name="Et1", access_vlan= 2 )
    intf3 = Interface (intf_name="Et1", access_vlan= 3 )
    intf4 = Interface (intf_name="Et1", access_vlan= 4 )
    intf5 = Interface (intf_name="Et1", access_vlan= 5 )
    intf6 = Interface (intf_name="Et1", access_vlan= 6 )
    intf7 = Interface (intf_name="Et7", intf_mode= "trunk" )

    #print the interface instances information
    print (intf1)
    print (intf2)
    print (intf3)
    print (intf4)
    print (intf5)
    print (intf6)
    print (intf7)
    print ("-" * 50)
    clear_output()
    