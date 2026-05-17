from abc import ABC, abstractmethod
import random


class Device(ABC):

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.status = "off"

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class Lamp(Device):

    def __init__(self, id: int, name: str, brightness: int):
        super().__init__(id, name)
        self.brightness = brightness

    def connect(self):
        self.status = "on"

    def disconnect(self):
        self.status = "off"

    def execute_command(self, cmd):

        if cmd == "on":
            self.connect()
            return {"lamp": "on"}

        if cmd == "off":
            self.disconnect()
            return {"lamp": "off"}

        if cmd.startswith("brightness:"):
            try:
                value = int(cmd.split(":")[1])
                self.brightness = value
                return {"brightness": self.brightness}
            except:
                return {"error": "invalid brightness"}

        return {"error": "unknown command"}


class Fan(Device):

    def __init__(self, id: int, name: str, speed: int):
        super().__init__(id, name)
        self.speed = speed

    def connect(self):
        self.status = "on"

    def disconnect(self):
        self.status = "off"

    def execute_command(self, cmd):

        if cmd == "on":
            self.connect()
            return {"fan": "on"}

        if cmd == "off":
            self.disconnect()
            return {"fan": "off"}

        if cmd.startswith("speed:"):
            try:
                value = int(cmd.split(":")[1])
                self.speed = value
                return {"speed": self.speed}
            except:
                return {"error": "invalid speed"}

        return {"error": "unknown command"}


class Pump(Device):

    def connect(self):
        self.status = "on"

    def disconnect(self):
        self.status = "off"

    def execute_command(self, cmd):

        if cmd == "on":
            self.connect()
            return {"pump": "on"}

        if cmd == "off":
            self.disconnect()
            return {"pump": "off"}

        return {"error": "unknown command"}


class Sensor(Device):

    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.value = 0
        self.linked_heater = None

    def emulate(self):
        self.value = random.randint(10, 35)

    def connect(self):
        self.emulate()
        self.status = "on"

        # 🔥 АВТОМАТИКА
        if self.linked_heater:
            self.linked_heater.auto_power(self.value)

        return {"temperature": self.value}

    def disconnect(self):
        self.status = "off"


class Heater(Device):

    def __init__(self, id: int, name: str, threshold: float = 25):
        super().__init__(id, name)
        self.threshold = threshold

    def connect(self):
        self.status = "on"

    def disconnect(self):
        self.status = "off"

    def auto_power(self, temperature):

        try:
            t = float(temperature)

            if t < self.threshold:
                self.connect()
                return {"heater": "ON", "temp": t}

            else:
                self.disconnect()
                return {"heater": "OFF", "temp": t}

        except:
            return {"error": "bad temperature"}

    def execute_command(self, cmd):

        if cmd == "on":
            self.connect()
            return {"heater": "on"}

        if cmd == "off":
            self.disconnect()
            return {"heater": "off"}

        if cmd.startswith("set:"):
            try:
                self.threshold = float(cmd.split(":")[1])
                return {"threshold": self.threshold}
            except:
                return {"error": "invalid threshold"}

        return {"error": "unknown command"}