import random
from devices import Device

class Sensor(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.value = 0

    def emulate(self):
        self.value = random.randint(0, 100)

    def connect(self):
        self.emulate()
        self.status = "on"
        return {"value": self.value}

    def disconnect(self):
        self.status = "off"