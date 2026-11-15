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

    def send_packet(self, destinationIp):
        packet = self.make_packet(self.data)

        packet["destinationIp"] = destinationIp

        return f"data sent to {destinationIp}"

    def receive_packet(self, sourceIp):
        packet = self.make_packet(self.data)

        packet["sourceIp"] = sourceIp

        return f"data received from {sourceIp}"
