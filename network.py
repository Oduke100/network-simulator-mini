import math
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

def get_ip(prefix="102"):
    START = 0
    END   = 255
    
    ip: [str] = []

    ip.append(prefix)
    
    for i in range(0, 3):
        i = random.randint(START, END)
        ip.append(str(i))

    ip = ".".join(i for i in ip)
    return ip

class Network:
    def __init__(self, name="Aether_networks", isp_name="Aether_5G"):
        self.name     = name
        self.isp_name = isp_name

    def issue_subnet(self, users):
        subnet = get_subnet(users)
        network_ip = get_ip()

        return subnet, network_ip
    
class User:
    def __init__(self):
        pass
        
    def create_uplink(self, users):
        uplink = Network()
        subnet = uplink.issue_subnet(users)

        return subnet

    def issue_ip(self):
        user_ip = get_ip()
        




michael = User()
michael_subnet = michael.create_uplink(1000)
michael_ip = michael.issue_ip()
print(michael_subnet)

# aether = Network()
# aether_subnet = aether.issue_subnet(50000000)
# print(aether_subnet)

# ip = get_ip()
# print(ip)
