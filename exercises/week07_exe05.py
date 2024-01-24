#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

#Define the Interface class
class Interface :
    def __init__(self, intf_name, intf_mode = "access", 
                 access_vlan = 1, speed = "1Gbps", duplex= "full") :
        
        self.intf_name = intf_name
        self._intf_mode = intf_mode
        self._access_vlan = access_vlan
        self.speed = speed
        self.duplex = duplex
        
        if self._intf_mode not in ("access", "trunk") :
            raise ValueError ("Wrong Interface mode, it should be either 'access' or 'trunk'")
        elif self._intf_mode == "access" :
            if not isinstance (self._access_vlan, int) :
                raise ValueError ("The access vlan number is wrong, it should be between (1-4095)")
        else :
            self._access_vlan = None
            
    @property
    def intf_mode (self) :
        return self._intf_mode
    
    @property
    def access_vlan (self) :
        return self._access_vlan
    
    @intf_mode.setter
    def intf_mode (self, mode) :
        self._intf_mode = mode
        if mode in ("trunk" , "access") :
            if mode == "trunk" :
                self._access_vlan = None
        else :
            raise ValueError (f"Intf mode should be either 'trunk' or 'access' not {mode}!")
        return None
        
    @access_vlan.setter
    def access_vlan (self, vlan) :
        if not isinstance (vlan, int) :
            raise ValueError ("Wrong vlan number!")
        else :
            if self._intf_mode == "trunk" :
                self._access_vlan = None
            else :
                self._access_vlan = vlan
        return None
    
        
    def __str__(self) :
        if not self._access_vlan :
            return (f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, "
                    f"Mode: {self._intf_mode})")
        else :
            return (f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, "
                    f"Mode: {self._intf_mode}, Vlan: {self._access_vlan})")            


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
    for intf in (intf1, intf2, intf3, intf4, intf5, intf6, intf7):
        print(intf)
    print("-" * 50)
    print()

    print()
    print("Testing behavior...of setter")
    intf1.intf_mode = "trunk"
    print(f"{intf1.intf_mode=}")
    print(f"{intf1.access_vlan=}")
    intf1.intf_mode = "access"
    intf1.access_vlan = 42
    print(f"{intf1.intf_mode=}")
    print(f"{intf1.access_vlan=}")
    try:
        intf1.intf_mode = "invalid"
    except ValueError:
        print("Expected exception handled")
    try:
        intf1.access_vlan = "zzzz"
    except ValueError:
        print("Expected exception handled")
    print()
    clear_output()