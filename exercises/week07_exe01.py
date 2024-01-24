#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output


#define the device class
class NetworkDevice :
    def __init__( self,host,platform, username, password ) :
        self.host = host
        self.platform = platform
        self.username = username
        self.password = password
        return None
    
    def __str__ ( self ) :
        return (f"NetworkDevice: {self.host} ({self.platform})")

nd1 = NetworkDevice ("host1.domain.com", "cisco_xe", "user1", "password1")
nd2 = NetworkDevice ("host2.domain.com", "juniper_junos", "user2", "password2")

print (nd1)
print (nd2)
