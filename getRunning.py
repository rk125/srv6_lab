# Import our libraries
from genie.conf import Genie
import os
import sys, getopt
import datetime


# directory= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
directory= "."

list_of_cmds_xr=[
              "show run", 
              "show segment-routing srv6 locator",
              "show segment-routing srv6 locator POD0 detail",
              "show isis segment-routing srv6 locators detail",
              "show segment-routing srv6 sid",
              "show route ipv6 isis",
              "show bgp vpnv4 unicast summary",
              "show segment-routing srv6 locator POD0 sid",
              "show bgp vpnv4 unicast received-sids",
              "show route vrf 1",
              "show cef vrf 1 192.168.1.0/24", 
              "show cef vrf 1 192.168.4.0/24",
              "show bgp vrf 1 192.168.1.0/24",
              "show bgp vrf 1 192.168.4.0/24",
              "show evpn evi vpn-id 200 mac",

]
list_of_cmds_xe=[
              "show run", 
              
]

# Create a testbed object for the network
testbed = Genie.init("srv6_testbed.yaml")

try:
    os.mkdir(directory)
except FileExistsError:
    pass

for device in testbed.devices:
    # Connect to the device
    testbed.devices[device].connect(init_exec_commands=[],init_config_commands=[],log_stdout=False)
    # print ("tips "+ testbed.devices[device].type)
    if (testbed.devices[device].type=="iosxr"):
        cmds=list_of_cmds_xr
    if (testbed.devices[device].type=="iosxe"):
        cmds=list_of_cmds_xe
    for command in cmds:
        d=directory+"/"+testbed.devices[device].name
        try:
            os.mkdir(d)
        except FileExistsError:
            pass
        c=command.replace(" ","_")
        c=command.replace(".","_")
        c=command.replace("/","_")
        fname=os.path.join(d, c +".txt") 
        f = open(fname, "w")
        # f.write("\n********************* "+command+" *********************\n")
        f.write(testbed.devices[device].execute(command)+"\n")
    f.close()
