#! /usr/bin/env python3
from rich import print

intf= "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields = intf.split()

intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_line_status = intf_fields[4]
intf_line_protocol = intf_fields[5]

print (f"{intf_name=}\n{intf_ip_addr=}\n{intf_line_status=}\n{intf_line_protocol=}\n")

status_is_up = intf_line_status == "up"
protocol_is_up = intf_line_protocol == "up"

print (f"{status_is_up=}, {protocol_is_up=}")
