#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output

class OSPFRouter :
    def __init__ (self, instance_id, area_id, router_id, is_dr=False, is_bdr= False) :
        self.instance_id = instance_id
        self.area_id = area_id
        self.router_id = router_id
        self.is_bdr = is_bdr
        self.is_dr = is_dr
        self._neighbours = set()
    
    def add_neighbour (self, neighbour_id) :
        self._neighbours.add (neighbour_id)
        
    def del_neighbour ( self, neighbour_id) :
        self._neighbours.remove (neighbour_id)
    
    @property    
    def neighbours (self) :
        return self._neighbours
        
    def __str__(self) -> str:
        return (f"InstanceID: {self.instance_id}, AreaID: {self.area_id}, "
                f"RouterID: {self.router_id}, Is DR: {self.is_dr}, Is BDR: {self.is_bdr}\n"
                f"Neighbours : {self.neighbours}")



if __name__ == "__main__" :   
    #Define and instnace of the OSPFRouter class   
    cisco1 = OSPFRouter (instance_id=42,area_id=0, router_id= "10.220.88.29")

    #Add all the OSPF neighbours 
    for rid in ("10.220.88.28","10.220.88.30","10.220.88.31","10.220.88.32","10.220.88.33", 
            "10.220.88.34","10.220.88.35") :
        cisco1.add_neighbour (rid)
        
    #Print the Cisco1 OSPF information     
    print (cisco1)
    print()
    print ("-" * 50)
    cisco1.add_neighbour ("1.1.1.1")
    print (cisco1)
    print ("*" * 50)
    cisco1.del_neighbour ("1.1.1.1")
    print (cisco1)
    
        