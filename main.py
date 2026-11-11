import os
from devices import Computer
from data import Packet
from network import Network

directory = "network"

os.makedirs(directory, exist_ok=True)

# safaricom = Network("safaricom", "saf_5G")
# safaricom_ip = safaricom.issue_ip()
# print(safaricom_ip)

hellen = Computer("hellen")
oduke  = Computer("oduke")


hellen.nyx()
oduke.nyx()
