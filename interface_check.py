#This is a script to check interface statuses on network devices without having to login
#For coding practice purposes
#Thanks to Kirk Byers for Netmiko library

from __future__ import print_function
from netmiko import ConnectHandler
from functions import get_count, get_brand, get_ip, get_int, get_user, get_pw

username = get_user()
password = get_pw()

count = get_count()
iterations = 0

while iterations < count:
        
        device = get_brand().lower()
        ip_addr = get_ip()
        interface = get_int()

        if device == 'c':
                cisco = {
                'device_type': 'cisco_ios',
                'host':  ip_addr,
                'username': username,
                'password': password
                }
                
                net_connect = ConnectHandler(**cisco) #connect to cisco device
                output = net_connect.send_command('show interface ' + interface)
                print(output)
                iterations += 1

        elif device == 'h':
                huawei = {
                'device_type': 'huawei',
                'host':  ip_addr,
                'username': username,
                'password': password
                }
                net_connect = ConnectHandler(**huawei) #connect to huawei device
                output = net_connect.send_command('dis interface ' + interface)
                print(output)
                iterations += 1
        
        else:
                arista = {
                'device_type': 'arista_eos',
                'host':  ip_addr,
                'username': username,
                'password': password
                }
                net_connect = ConnectHandler(**cisco) #connect to cisco device
                output = net_connect.send_command('show interface ' + interface)
                print(output)
                iterations += 1
