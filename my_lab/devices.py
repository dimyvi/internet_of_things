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

    def execute_command(self, cmd):

        return {"result": "unknown command"}


class Lamp(Device):

    def __init__(self, id: int, name: str, brightness: int):

        super().__init__(id, name)

        self.brightness = brightness
        self.status = "off"

    def connect(self):

        self.status = "on"

        print(f"Лампа {self.name} включена")

    def disconnect(self):

        self.status = "off"

        print(f"Лампа {self.name} выключена")

    def change_brightness(self, brightness):

        self.brightness = brightness

    def execute_command(self, cmd):

        if cmd == "on":

            self.connect()

            return {"result": "lamp on"}

        elif cmd == "off":

            self.disconnect()

            return {"result": "lamp off"}

        elif cmd.startswith("brightness:"):

            value = int(cmd.split(":")[1])

            self.change_brightness(value)

            return {
                "result": "brightness changed",
                "brightness": self.brightness
            }

        return {"result": "unknown command"}


class Fan(Device):

    def __init__(self, id: int, name: str, speed: int):

        super().__init__(id, name)

        self.speed = speed
        self.status = "off"

    def connect(self):

        self.status = "on"

        print(f"Вентилятор {self.name} включен")

    def disconnect(self):

        self.status = "off"

        print(f"Вентилятор {self.name} выключен")

    def change_speed(self, speed):

        self.speed = speed

    def execute_command(self, cmd):

        if cmd == "on":

            self.connect()

            return {"result": "fan on"}

        elif cmd == "off":

            self.disconnect()

            return {"result": "fan off"}

        elif cmd.startswith("speed:"):

            value = int(cmd.split(":")[1])

            self.change_speed(value)

            return {
                "result": "speed changed",
                "speed": self.speed
            }

        return {"result": "unknown command"}


class Pump(Device):

    def __init__(self, id: int, name: str):

        super().__init__(id, name)

    def connect(self):

        self.status = "on"

        print(f"Насос {self.name} включен")

    def disconnect(self):

        self.status = "off"

        print(f"Насос {self.name} выключен")

    def execute_command(self, cmd):

        if cmd == "on":

            self.connect()

            return {"result": "pump on"}

        elif cmd == "off":

            self.disconnect()

            return {"result": "pump off"}

        return {"result": "unknown command"}


class Sensor(Device):

    def __init__(self, id: int, name: str):

        super().__init__(id, name)

        self.value = 0

    def emulate(self):

        self.value = random.randint(15, 30)

    def connect(self):

        self.emulate()

        self.status = "on"

        return {"value": self.value}

    def disconnect(self):

        self.status = "off"

    def execute_command(self, cmd):

        if cmd == "read":

            self.emulate()

            return {
                "value": self.value
            }

        return {"result": "unknown command"}