#This is a script to check for interface status and logs on IPLC devices
#For testing purposes, please do not use without permission
#Thanks to Kirk Byers for Netmiko library

from __future__ import print_function
from netmiko import ConnectHandler
from functions import get_count, get_ip, get_int, get_user, get_pw, get_region


username = get_user()
password = get_pw()

print("Hello!")
print("This script aims to show the description of the interface, as well as capture the logs of the interface you want to check.\n")


brand = ""
device_list = {'I':'Huawei', 'S':'Cisco', 'V':'Cisco', 'T':'Cisco', 'T':'Cisco'} #dictionary for list of IPLC devices
iteration = 0

count = get_count()

while iteration < count:

        idc = get_region().upper()
        ip_addr = get_ip()
        interface = get_int().capitalize()

        for region,dev_brand in device_list.items():    #iterate through dictionary
                if idc == region:                       #if user input == key in dictionary
                        brand = dev_brand               #set input to corresponding value
                        if brand == 'Cisco':            #if corresponding value is c, run cisco commands
                                cisco = {
                                'device_type': 'cisco_ios',
                                'host':  ip_addr,
                                'username': username,
                                'password': password
                                }

                                net_connect = ConnectHandler(**cisco) #connect to cisco device

                                #command to send to device

                                cmd1 = ('show interface des | i ' + interface[-8::]) #grab the last 7 characters from user input
                                cmd2 = ('sh logg | i ' + interface[-8::])            #grab the last 7 characters from user input
                                output1 = net_connect.send_command(cmd1)
                                output2 = net_connect.send_command(cmd2)
                                print(output1 + '\n' + output2)
                                iteration += 1

                        elif brand == 'Huawei':

                                huawei = {
                                'device_type': 'huawei',
                                'host': ip_addr,
                                'username': username,
                                'password': password,
                                }

                                net_connect = ConnectHandler(**huawei) #connect to huawei device
                                cmd1 = ('dis int description | i ' + interface[-8::])
                                cmd2 = ('dis logb bri' + interface[-8::])
                                output1 = net_connect.send_command(cmd1)
                                output2 = net_connect.send_command(cmd2)
                                print(output1 + '\n' + output2)

                else: # indented at different level as there is no entry in dictionary for US devices
                        arista = {
                        'device_type': 'arista_eos',
                        'host': ip_addr,
                        'username': username,
                        'password': password
                        }

                        net_connect = ConnectHandler(**arista) #connect to arista device

                        cmd1 = ('show int des | i ' + interface[-3::])
                        cmd2 = ('show logg | i ' + interface[-3::])
                        output1 = net_connect.send_command(cmd1)
                        output2 = net_connect.send_command(cmd2)
                        print(output1 + '\n' + output2)
                        iteration += 1
                break

