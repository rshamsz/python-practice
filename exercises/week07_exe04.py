#! /usr/bin/env python3
from rich import print
from IPython.display import clear_output


#define the device class
class NetworkDevice :
    def __init__( self,host,platform, username, password ) :
        self.host = host
        self.platform = platform
        self.username = username
        self._password = password
        return None
    
    @property
    def password (self) :
        return "*" * len (self._password)
    
    @password.setter
    def password (self, new_pass) :
        if new_pass != self._password :
            self._password = new_pass
        else :
            raise ValueError ("!!!You cannot use the previous password!!!")
    
    def __str__ ( self ) :
        return (f"NetworkDevice: {self.host} ({self.platform})")

nd1 = NetworkDevice ("host1.domain.com", "cisco_xe", "user1", "password1")
nd2 = NetworkDevice ("host2.domain.com", "juniper_junos", "user2", "password2")

print (nd1)
print (nd2)

print ("Password is hidden using the Getter method: ",nd1.password)
nd1.password = "password1"
print ()
print ( "-" * 50)
nd1.password = "newpass123"
clear_output()
