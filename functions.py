#This file contains the functions required to run other scripts

from base64 import b64decode
import os

def get_count():
#function to obtain number of devices to check from user input
        
        try:
                num_of_devices = int(raw_input("Enter the number of devices you want to check: "))
        except NameError:
                num_of_devices = int(input("Enter the number of devices you want to check "))
        return num_of_devices

def get_brand():
#function to obtain brand that user is trying to check
        
        try:
                brand = str(raw_input("Enter 'c' for Cisco or 'h' for Huawei or simply hit 'Enter' for Arista: "))
        except NameError:
                brand = str(input("Enter 'c' for Cisco or 'h' for Huawei or simply hit 'Enter' for Arista: "))
        return brand

def get_ip():
#function to get OOB IP from user
        
        try:
                ip_addr = str(raw_input("Enter OOB IP address: "))
        except NameError:
                ip_addr = str(input("Enter OOB IP address: "))
        return ip_addr

def get_int():
#Function to obtain interface from user
        
        try:
                interface = str(raw_input("Enter the interface: "))
        except NameError:
                interface = str(input("Enter the interface: "))
        return interface

def get_user():
#function to get username
        
        username = b64decode(os.environ.get("DEVICEUSER")).decode().rstrip()
        return username

def get_pw():
#function to get password
        
        password = b64decode(os.environ.get("PASS")).decode().rstrip()
        return password


def get_region():
#function to get user input on region
        
        try:
                country = str(raw_input("Enter the region of the device you want to check: "))
        except NameError:
                country = str(input("Enter the region of the device you want to check:"))
        return country

def get_peer():
#function to obtain BGP neighbour's IP address
        
        try:
                peer_ip = str(raw_input("Enter neighbour's IP address: "))
        except NameError:
                peer_ip = str(input("Enter neighbour's IP address: "))

        return peer_ip
