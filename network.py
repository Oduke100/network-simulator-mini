import os
import math
import json
import random
from misc.converter import Data
from misc.converter import Data

"""
network class, this is the carrier and has the deets

"""

# ==== HELPERS ====
def get_subnet(users=1000):
    start_subnet = "255.255.255.255"
    start_subnet: [int] = start_subnet.split(".")

    subnet = []
    for s in start_subnet:
        subnet.append(int(s))

    data = Data(subnet)
    clean_subnet = data.convert_to_binary()

    subnet_string = ""
    for c in clean_subnet:
        subnet_string = subnet_string + c

    power = round(math.log(users, 2)) + 1

    foo = []
    for char in subnet_string:
        foo.append(char)

    counter = 0
    for char in subnet_string:
        if char == "0":
            counter += 1

    c = 0

    for i in range(len(foo)-counter-1, 0, -1):
        if c < power:
            foo[i] = 0
            c += 1

    foo = "".join(str(f) for f in foo)

    bin = []
    for f in range(0, len(foo)-1, 8):
        slice = foo[f:f+8]
        bin.append(slice)

    data = Data(bin)
    subnet_values = data.convert_to_decimal()
    subnet_values = ".".join(str(s) for s in subnet_values)

    return subnet_values

def get_ip(kind="user"):

    ref_table = {
        "network" : "102",
        "user"    : "10"
    }
    
    START = 0
    END   = 255
    
    ip: [str] = []

    prefix = ref_table[kind]
    ip.append(prefix)
    
    for i in range(0, 3):
        i = random.randint(START, END)
        ip.append(str(i))

    ip = ".".join(i for i in ip)
    return ip

# ==== CLASSES ====
class Network:
    dirpath = "network/ips"
    os.makedirs(dirpath, exist_ok=True)
        
    nfilepath = "network/ips/network_ips.json"
    
    def __init__(self, name="Aether_networks", isp_name="Aether_5G"):
        self.name     = name
        self.isp_name = isp_name
        
    def issue_subnet(self, users):
        subnet = get_subnet(users)

        return subnet
        
    def issue_ip(self, users=1000000, kind="network"):
        dirpath = "network/ips"
        os.makedirs(dirpath, exist_ok=True)
        
        nfilepath = "network/ips/network_ips.json"
        
        try:
            with open(nfilepath, "x") as file:
                file.close()
        except:
            print("file already exists!")
            
        ips = []
        subnet = self.issue_subnet(users)
            
        with open(nfilepath, "r") as file:
            for f in file:
                ips.append(json.loads(f))
                
        for i in ips:
            if i["isp_name"] == self.isp_name:
                return f"ISP live, reach at {i["ip"]}"

        ip = get_ip(kind)
        if any(i["ip"] == ip for i in ips):
            ip = get_ip(kind)

        ip_record = {}

        ip_record = {
            "name" : self.name,
            "isp_name" : self.isp_name,
            "ip"   : ip,
            "subnet" : subnet
        }

        with open(nfilepath, "a") as file:
            json.dump(ip_record, file)
            file.write("\n")

        return f"ISP registered, reach at {ip}"

class User:
    def __init__(self):
        pass
        
    def issue_ip(self, name, isp_name, kind="user"):
        dirpath = "network/ips"
        os.makedirs(dirpath, exist_ok=True)

        ufilepath = "network/ips/users_ips.json"
        
        try:
            with open(ufilepath, "x") as file:
                file.close()
        except:
            print("file already exists!")
            
        ips = []

        with open(ufilepath, "r") as file:
            for f in file:
                ips.append(json.loads(f))

        for i in ips:
            if i["name"] == name:
                return i["ip"]

        ip = get_ip(kind)
        if any(i["ip"] == ip for i in ips):
            ip = get_ip(kind)

        ip_record = {}

        ip_record = {
            "name" : name,
            "ip"   : ip
        }

        with open(ufilepath, "a") as file:
            json.dump(ip_record, file)
            file.write("\n")

        return ip
