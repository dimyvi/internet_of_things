from flask import Flask
from controller import Controller
from devices import Lamp, Fan, Pump

app = Flask(__name__)
c = Controller()

c.add_device(Lamp(1, "спальня", 50))
c.add_device(Fan(2, "теплица", 5))


@app.route("/")
def home():
    return "Умная теплица работает"


@app.route("/on")
def turn_on():
    print("ВКЛЮЧИТЬ ВСЕ УСТРОЙСТВА")
    c.turn_on_all()
    return "все включены"


@app.route("/off")
def turn_off():
    print("ВЫКЛЮЧИТЬ ВСЕ УСТРОЙСТВА")
    c.turn_off_all()
    return "все выключены"


@app.route("/devices")
def devices():
    print("ПОЛУЧИТЬ СПИСОК УСТРОЙСТВ")
    result = ""
    for d in c.get_all_devices():
        result += f"{d.id} {d.name} {d.status}<br>"
    return result


if __name__ == "__main__":
    app.run(debug=True)