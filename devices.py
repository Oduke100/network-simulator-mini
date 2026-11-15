from network import User
from nyx.main import OS

class Computer:
    def __init__(self, name="computer"):
        self.name = name
        self.user = User()
        self.os   = OS()

    def __str__(self):
        return self.name

    def nyx(self):
        self.os.start(self.name)
        
