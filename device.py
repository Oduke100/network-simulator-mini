from misc.mac_generator import make_mac

class Computer:
    def __init__(self, name):
        self.name=name

    def info(self):
        MAC=make_mac()
        
        print(
            f"This is {self.name} with MAC: {full_mac}"
            )

samsung=Computer("Samsung")
samsung.info()
