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

def ip_addr(subnet_mask):

    s=subnet(subnet_mask)
    
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

#ip=ip_addr("255.255.0.0")
#print(ip)
