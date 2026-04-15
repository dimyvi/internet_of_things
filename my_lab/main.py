from devices import Lamp, Fan, Pump
from controller import Controller
from interface import UserInterface, AdminInterface
from db import Database

db = Database()
c = Controller()

c.add_device(Lamp(1, "спальня", 50))
c.add_device(Lamp(2, "кухня", 70))
c.add_device(Fan(3, "тепл", 5))
c.add_device(Pump(4, "полив"))

print("\n=== УМНАЯ ТЕПЛИЦА ===")

while True:
    while not c.login():
        pass

    if c.current_user == "admin":
        AdminInterface(c).run()
    else:
        UserInterface(c).run()