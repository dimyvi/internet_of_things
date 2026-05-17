import random
from devices import Device


class Sensor(Device):

    def __init__(self, id, name):
        super().__init__(id, name)
        self.value = 0
        self.linked_heater = None

    def emulate(self):
        self.value = random.randint(10, 35)

    def connect(self):
        self.emulate()
        self.status = "on"

        if self.linked_heater:
            self.linked_heater.auto_power(self.value)

        return {"temperature": self.value}

    def disconnect(self):
        self.status = "off"

    def execute_command(self, cmd):

        if cmd == "read":
            return self.connect()

        return {"error": "unknown command"}
