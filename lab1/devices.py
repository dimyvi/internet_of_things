from abc import ABC, abstractmethod

class Device(ABC):

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.status = "off"

    @abstractmethod
    def connect(self):
        self.status = "on"

    @abstractmethod
    def disconnect(self):
        self.status = "off"


class Lamp(Device):
    def __init__(self, id: int, name: str, brightness: int):
        super().__init__(id, name)
        if brightness < 0 or brightness > 100:
            raise ValueError("яркость должна быть от 0 до 100")
        self.brightness = brightness
        self.status = "on"
        print(f"Лампа {self.name} успешно создана, ей назначена яркость {self.brightness}")

    def change_brightness(self, brightness: int):
        if brightness < 0 or brightness > 100:
            raise ValueError("яркость должна быть от 0 до 100")
        self.brightness = brightness
        print(f"Яркость лампы {self.name} изменена на {self.brightness}")

    def connect(self):
        self.status = "on"
        print(f"Лампа {self.name} подключена")

    def disconnect(self):
        print(f"Лампа {self.name} Отключена")


class Fan(Device):
    def __init__(self, id: int, name: str, speed: int):
        super().__init__(id, name)
        if speed < 0 or speed > 10:
            raise ValueError("скорость должна быть от 0 до 10")
        self.speed = speed
        self.status = "on"
        print(f"Вентилятор {self.name} создан, поставлена скорость {self.speed}")

    def change_speed(self, speed: int):
        if speed < 0 or speed > 10:
            raise ValueError("скорость должна быть от 0 до 10")
        self.speed = speed
        print(f"Скорость вентилятора {self.name} изменена на {self.speed}")

    def connect(self):
        self.status = "on"
        print(f"Вентилятор {self.name} подключен")

    def disconnect(self):
        print(f"Вентилятор {self.name} Отключен")

class Pump(Device):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.status = "off"
        print(f"Насос {self.name} создан. Статус {self.status}")

    def change_status(self, status: str):
        if status == "on":
            self.status = "on"
        elif status == "off":
            self.status = "off"

    def connect(self):
        self.status = "on"
        print(f"Насос {self.name} подключен")

    def disconnect(self):
        self.status = "off"
        print(f"Насос {self.name} Отключен")

