from flask import Flask, jsonify, render_template
from controller import Controller
from devices import Lamp, Fan, Pump, Sensor

app = Flask(__name__)

c = Controller()

c.add_device(Lamp(1, "спальня", 50))
c.add_device(Fan(2, "теплица", 5))
c.add_device(Sensor(3, "датчик температуры"))


@app.route("/")
def home():
    return render_template("sensor_emulator.html")


@app.route("/connect/<int:id>")
def connect_device(id):
    d = c.get_device(id)
    if d:
        data = d.connect()
        return jsonify(data)
    return jsonify({"error": "device not found"})


@app.route("/on")
def turn_on():
    c.turn_on_all()
    return jsonify({"status": "all on"})


@app.route("/off")
def turn_off():
    c.turn_off_all()
    return jsonify({"status": "all off"})


@app.route("/devices")
def devices():
    result = []
    for d in c.get_all_devices():
        result.append({
            "id": d.id,
            "name": d.name,
            "status": d.status
        })
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)