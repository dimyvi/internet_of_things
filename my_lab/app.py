from flask import Flask, jsonify, render_template, request
from controller import Controller
from devices import Lamp, Fan, Pump, Sensor

app = Flask(__name__)

c = Controller()

c.add_device(Lamp(1, "спальня", 50))
c.add_device(Fan(2, "теплица", 5))
c.add_device(Pump(3, "полив"))
c.add_device(Sensor(4, "датчик температуры"))


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


@app.route("/command/<int:id>")
def send_command(id):

    d = c.get_device(id)

    if not d:
        return jsonify({"error": "device not found"})

    cmd = request.args.get("cmd")

    result = d.execute_command(cmd)

    return jsonify(result)


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