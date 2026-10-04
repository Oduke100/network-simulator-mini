"""
this is where we will be making the IP addresses for the simulator
I did this in the old version, but looks like due to my ego and the architecture changes I want I may have to do them fresh

first ofc we have to interpret the subnet and find out how many addresses we can have, the math, we change to binary and count all the 0's 

now we have the subnet probe, maybe I rename it to available_hosts, coz that's what It checks for - decided against this
"""

# ==== imports ====

import random
from converter import decimal_to_binary_convert, binary_to_decimal_convert

def subnet_probe(subnet):
    subnet_values = []

    subnet_state_1 = subnet.split(".")

    for s in subnet_state_1:
        s = int(s)

        s_state_2 = decimal_to_binary_convert([s])
        subnet_values.append(s_state_2)

    zeros = 0
    octet_addresses = []
    host_address = []
    broadcast_address = []

    for s in subnet_values:
        if "0" in s:
            octet_base_value = binary_to_decimal_convert(s)

            octet_address_value = random.randint(octet_base_value, 255)
            octet_addresses.append(octet_address_value)
        else:
            octet_address_value = random.randint(0, 255)
            octet_addresses.append(octet_address_value)

    return octet_addresses

test = subnet_probe("255.255.240.0")
print(test)
