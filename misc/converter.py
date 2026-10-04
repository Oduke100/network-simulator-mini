"""
FYI: 4-bits is called a nibble

this is the conversion HQ, I will need;
decimal - binary
binary - decimal
binary - hexadecimal

and any other
"""

def decimal_to_binary_convert(data, width=8):
    bite_string = ""
    
    for char in data:
        bits = []
        
        while char:
            
            quotient = char // 2 
            bit = char % 2
            
            char = quotient
            bits.append(bit)

        # padding
        while len(bits) < width:
            bits.append(0)

        binary = "".join(str(bits[b]) for b in range(len(bits)-1, -1, -1))
        bite_string += binary
    
    return bite_string

def binary_to_decimal_convert(binary):
    power = 0
    values = []

    for b in range(len(binary)-1, -1, -1):
        if binary[b] == "1":
            value = 2**power
            power += 1
            values.append(value)
        else:
            value = 0
            power += 1
            values.append(value)

    decimal_value = sum(values)

    return decimal_value


def binary_to_hexadecimal_convert(byte):
    ref_list = []
    ref_string = "0123456789ABCDEF"

    for r in ref_string:
        ref_list.append(r)

    byte = binary_to_decimal_convert(byte)

    hex_value = ref_list[byte]

    return hex_value

