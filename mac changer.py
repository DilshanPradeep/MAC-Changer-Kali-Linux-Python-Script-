#!/user/bin/env python

import subprocess

print("Welcome To MAC Canger")

print ("**************************************************")

print("This is you current MAC address")

print("****************************************************")

subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig eth0 down", shell=True)

print("------------------------------------------------------------------------------------------")
changed_mac = str(input("Enter new mac address: "))
print("------------------------------------------------------------------------------------------")

def mac_changer(changed_mac):
    subprocess.call("ifconfig eth0 hw ether " + changed_mac, shell=True)
    subprocess.call("ifconfig eth0 up", shell=True)

print("MAC Address changed successfully ")
    
    subprocess.call("ifconfig", shell=True)

mac_changer(changed_mac )
