#this is our "local-manufacturer" this is where we generate the MAC addresses the devices in our system will use
#the implimentation will follow a structured 2-(24-bit) system where I settle on the first 24-bit(I am thinking a name converted to binary then to hexadecimal-settled for "nsm")
#this 24-bit ID will ensure the universal id flag is set to `1` so we have actually valid addresses-"nsm" conformed to this

name="nsm"
number=0

def get_code(model):
    if model=="computer":
        model_id="001"
    elif mode_idl=="phone":
        model="002"
    elif model=="router":
        model_id="003"
    else:
        model_id="004"

    return model_id

def get_sn():
    global number
    number += 1
    serial = number

    return serial

# code="001"

def make_mac(model):

    model_id=get_code(model)
    sn=get_sn()

    #we hit a snug where the direct conversion of code gives a 7th pair in the HEX conversion, consequently I have opted to convert each individually

    model_id = format(int(model_id), '02b')
    sn = format(int(sn), '04b')

    hexadecimal_code = f"{model_id}{sn}"
    
    #this is binary conversion of the name
    binary_name= ' '.join(format(ord(char), '08b') for char in name)
    # binary_code= ' '.join(format(ord(char), '08b') for char in code)

    #this is conversion of the binary to hexa(would have opted for name straight to hexadecimal but opted this route)

    # hexadecimal_name= hex(int(binary_name.replace(" ", ""), 2))  #this gives the answer still but with a '0x' prefix that is not used in MAC addressing

    hexadecimal_name = format(int(binary_name.replace(" ", ""), 2), 'X')  #simple more formatting needed then we are good
    # hexadecimal_code = format(int(binary_code.replace(" ", ""), 2), 'X')

    hexadecimal_name=hexadecimal_name.upper()
    hexadecimal_code=hexadecimal_code.upper()

    name_pairs = []
    code_pairs = []
    
    for i in range(0, len(hexadecimal_name), 2):
        npair=hexadecimal_name[i: i+2]
        name_pairs.append(npair)

        N= ":".join(name_pairs)

    # return N #tested and verified it works

    for i in range(0, len(hexadecimal_code), 2):
        cpair=hexadecimal_code[i: i+2]
        code_pairs.append(cpair)

        C= ":".join(code_pairs)

    full_mac=":".join([N, C])

    # print(full_mac)
    return full_mac
    # return code
    # return sn

    
#mac=make_mac()
