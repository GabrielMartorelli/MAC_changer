#! /usr/bin/env python

import subprocess

interface = input("[-]Enter the interface: ")
newmac = input("[-]Enter the new MAC address: ")

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newmac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print("Your new MAC address: " + newmac)
