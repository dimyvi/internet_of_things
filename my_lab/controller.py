from devices import *
from db import Database

class Controller:
    def __init__(self):
        self.devices = []
        self.current_user = None
        self.db = Database()

    def add_device(self, device):
        self.devices.append(device)
        self.db.save_device(device)
        print(f"Устройство {device.name} добавлено")

    def remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
            self.db.remove_device(device)
            print("Девайс был удален")
        else:
            print("Устройство не найдено")

    def get_device(self, id):
        for device in self.devices:
            if device.id == id:
                return device
        return None

    def get_all_devices(self):
        return self.devices

    def turn_on_all(self):
        for device in self.devices:
            device.connect()
        print("Все устройства включены")

    def turn_off_all(self):
        for device in self.devices:
            device.disconnect()
        print("Все устройства выключены")

    def login(self):
        print("Введите логин и пароль")
        username = input("Username: ")
        password = input("Password: ")
        if self.db.check_user(username, password):
            self.current_user = username
            print("Вы вошли в систему")
            return True
        else:
            print("Неверный логин или пароль")
            return False

    def logout(self):
        self.current_user = None
        print("Вы вышли из системы")


