class Data:
    def __init__(self, data: [int]):
        self.data = data

    def convert_to_binary(self, pad=8):
        binary_data = []
        for i in self.data:
            bits = []
            
            while i:
                quotient = i // 2
                bit      = i % 2
                i        = quotient

                bits.append(bit)
                
            while len(bits) < pad:
                bits.append(0)

            bits = bits[::-1]
            bits = "".join(str(b) for b in bits)
            
            binary_data.append(bits)

        return binary_data

    def convert_to_decimal(self):
        values = []
        for char in self.data:
            value = 0
            count = 0
            for c in range(len(char)-1, -1, -1):
                if char[c] == "0":
                    count += 1
                
                else:
                    value = value + 2**(count)
                    count += 1
            
            values.append(value)

        return values
