## this is where we create the packet's structure and tell it how it will look when we are transmitting it

class Packet():
    def __init__(self, source_ip, destination_ip, protocol, payload, ttl=64):
        # if you have a value you want the func to default to when we dont pass one, supply it as I have in the init func
        
        self.source_ip=source_ip
        self.destination_ip=destination_ip
        self.protocol=protocol
        self.payload=payload
        self.ttl=ttl

    def ack(self):
        print(
            f"""
            Source IP: {self.source_ip}
            Destination IP: {self.destination_ip}
            Protocol: {self.protocol}
            Payload: {self.payload}
            TTL: {self.ttl}
            """
            )

# test_pkt=Packet("10.230.189.94", "10.230.187.80", "UDP", "This is a test message")
test_pkt=Packet("10.230.189.94", "10.230.187.80", "UDP", "This is a test message", ttl=32)
test_pkt.ack()
