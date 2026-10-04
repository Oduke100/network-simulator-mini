"""
this is where the system's mac addresses are cooked

the mac addresses will follow the industry standard 48-bit system but with a `1` universal flag so we always know the addresses are locally made


"""

# ==== imports ====
from converter import binary_to_decimal_convert, decimal_to_binary_convert, binary_to_hexadecimal_convert

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

def device_signature(model):
    name="nsm"
    
    model_code = get_code(model)    # returns a string ie, 001
    device_sn = get_sn()            # returns a number ie, 1
    model_id = int(model_code)
    hexadecimal_list = []

    if isinstance(name, str):
        name_state_1 = name.encode("utf-8")
    else:
        name_state_1 = name         # checks if data is str or otherwise

    name_state_2 = decimal_to_binary_convert(name_state_1)
    
    for n in range(0, len(name_state_2), 4):
        name_byte = name_state_2[n:n+4]
        name_byte_state_1 = binary_to_hexadecimal_convert(name_byte)
        hexadecimal_list.append(name_byte_state_1)

    model_code_state_1 = decimal_to_binary_convert([model_id], width=12)
    
    for m in range(0, len(model_code_state_1), 4):
        byte = model_code_state_1[m:m+4]
        byte_state_1 = binary_to_hexadecimal_convert(byte)
        hexadecimal_list.append(byte_state_1)

    device_sn_state_1 = decimal_to_binary_convert([device_sn], width=12)
    
    for s in range(0, len(device_sn_state_1), 4):
        sn_byte = device_sn_state_1[s:s+4]
        sn_byte_state_1 = binary_to_hexadecimal_convert(sn_byte)
        hexadecimal_list.append(sn_byte_state_1)

    return hexadecimal_list

def mac(model):
    mac_chunks = []
    device_mac = device_signature(model)

    device_mac_state_1 = "".join(device_mac)

    for d in range(0, len(device_mac_state_1), 2):
        mac_chunk = device_mac_state_1[d:d+2]
        mac_chunks.append(mac_chunk)

    device_mac_state_2 = ":".join(mac_chunks)

    # device_mac_state_2 is the mac_address of the device!!!
    return device_mac_state_2
        
samsung = mac("computer")
print(samsung)
# print(len(samsung))
