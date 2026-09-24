# this is the whole project's conversion HQ it will be a chain if check and will convert to the form we want
def convert(data, data_type):
    if data_type == "binary":
        converted_data=binary(data)
        return converted_data


# binary
def binary(data):
    text = data
    binary_text = " ".join(format(ord(x), '08b') for x in text)

    return binary_text


