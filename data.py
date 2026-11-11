class Packet:
    def __init__(self, data):
        self.data = data
    
    def make_packet(self, sourceIp="0.0.0.0", destinationIp="0.0.0.0"):
        packet = {}

        packet = {
            "sourceIp"      : sourceIp,
            "data"          : self.data,
            "destinationIp" : destinationIp
        }

        return packet

    def send_packet(self, sourceIp, destinationIp):
        return self.make_packet(sourceIp, destinationIp)

    def receive_packet(self, sourceIp, destinationIp):
        return self.make_packet(sourceIp, destinationIp)
