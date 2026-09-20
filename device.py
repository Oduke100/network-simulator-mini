from misc.mac_generator import make_mac
from misc.ip_generator import ip_addr

class Computer:
    def __init__(self, name, model, subnet):
        self.name=name
        self.model=model
        self.subnet=subnet

    def info(self):
        MAC=make_mac(self.model)
        # print(MAC)
        print(
            f"This is {self.name} with MAC: {MAC}"
            )

    def connect(self):
        ip=ip_addr(self.subnet)
        print(
            f"Device {self.name} connected to internet with IP {ip}"
            )

samsung=Computer("Samsung", "computer", "255.0.0.0")
dell=Computer("dell", "computer", "255.0.0.0")

samsung.info()
dell.info()
dell.connect()
