# now I have "extensively" researched the whole IP addressing idea and I am ready to impliment it
# now Idealy the network starts at the ISP(the guy with the largest subnet mask) but in our sim we need the system to be able to
# 1, accept subnets and map the number of usable addresses
# 2, issue addresses in the subnet given.

import random

def subnet(subnet_mask):

    #conversion of subnet to binary so we do the calculation
    octets = subnet_mask.split(".")
    #subnet_mask=subnet_mask.replace(".", "")
    subnet=[]

    for octet in octets:
        octet=format(int(octet), '08b')
        subnet.append(octet)
        
    # subnet= ' '.join(format(ord(char), '08b') for char in octets)
    return subnet

def get_blocked_ip(subnet_mask):
    b=subnet(subnet_mask)

    blocked_broadcast_ips = []
    blocked_network_ips = []
    for i in range(len(b)):
        if i == 0:
            continue

        octet = b[i]
        counter = 0
        decimal_ip_value = 0
        
        if "0" in octet:
            for char in octet:
                if char == "0":
                    counter += 1

                
                # decimal conversion of binary
                for char in octet:
                    decimal_ip_value = decimal_ip_value * 2 + int(char)

                broadcast_ip = decimal_ip_value + (2**counter - 1)
                network_ip = decimal_ip_value - decimal_ip_value
            blocked_broadcast_ips.append(broadcast_ip)
            blocked_network_ips.append(network_ip)

        else:
            broadcast_ip = decimal_ip_value
            network_ip = decimal_ip_value - decimal_ip_value
            
            blocked_broadcast_ips.append(broadcast_ip)
            blocked_network_ips.append(network_ip)

    blocked_broadcast_ips.insert(0, 10)
    blocked_network_ips.insert(0, 10)

    blocked_broadcast_ip = ".".join(str(x) for x in blocked_broadcast_ips)
    blocked_network_ip = ".".join(str(x) for x in blocked_network_ips)

    return blocked_broadcast_ip, blocked_network_ip

def assign_ip_addr(subnet_mask):

    s=subnet(subnet_mask)
    # i=get_blocked_ip()
    
    # for octet in s:
    #   for char in octet:
    #       if char != "1":
    #            counter += 1

    # return counter
    # this IP addressing algo is an actual thing man, had to think like I was in an exam LOL

    subnet_values = []
    for i in range(len(s)):
        if i == 0:
            continue

        octet = s[i]
        counter = 0
        
        if "0" in octet:
            for char in octet:
                if char == "0":
                    counter += 1

                decimal_value = 0
                # decimal conversion of binary
                for char in octet:
                    decimal_value = decimal_value * 2 + int(char)

                subnet_value = decimal_value + random.randint(0, (2**counter - 1))
            subnet_values.append(subnet_value)

        else:
            subnet_value = random.randint(0, 255)
            subnet_values.append(subnet_value)

    subnet_values.insert(0, 10)

    full_ip = ".".join(str(x) for x in subnet_values)
    
    return full_ip

def ip_addr(subnet_mask):
    # get the blocked_ips
    a=get_blocked_ip(subnet_mask)
    # get the assigned ip
    c=assign_ip_addr(subnet_mask)
    # return a

    # check
    if c in a:
        c = assign_ip_addr(subnet_mask)
    else:
        return c
    
#blocked_ip=get_blocked_ip("255.255.0")
#print(blocked_ip)
