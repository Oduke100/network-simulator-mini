from devices import Computer
from data import Packet

data = Packet("Hello World!")
data.make_packet()

ipAddrA = Computer("102.209.57.50")
ipAddrB = Computer("102.209.57.51")

# conf = data.send_packet(ipAddrA)
conf = data.receive_packet(ipAddrB)
print(conf)
