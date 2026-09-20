from misc.mac_generator import make_mac

class Computer:
    def __init__(self, name, model):
        self.name=name
        self.model=model

    def info(self):
        MAC=make_mac(self.model)

        # print(MAC)
        
        print(
            f"This is {self.name} with MAC: {MAC}"
            )



samsung=Computer("Samsung", "computer")
dell=Computer("dell", "computer")

samsung.info()
dell.info()
