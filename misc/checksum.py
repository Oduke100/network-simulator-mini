# this is the checksum hq this is where we do the checksum, all algos are here and only differ with a func call

from converter import convert

# even-parity check
# here we check the number of ones and confirm, if sender sent even and we count odd, we request a resend and if sender sent odd and we get an even same. we only accept if checksum matches what the sender intended

def even_parity(data, checksum):
    data = convert(data, "binary")
    counter = 0

    for char in data:
        if char == "0":
            counter += 1

        else:
            continue

        checksum_value = counter % 2

    if (checksum == "even") and (checksum_value == 0):
        print("Data Uncorrupted")
    else:
        print("Data Corrupted")


test = even_parity("Oduke", "even")
