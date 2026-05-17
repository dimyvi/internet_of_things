from flask import Flask, jsonify, render_template, request
from controller import Controller
from devices import Sensor, Heater, Lamp, Fan

app = Flask(__name__)

c = Controller()

# устройства
lamp = Lamp(1, "lamp", 50)
fan = Fan(2, "fan", 5)
sensor = Sensor(3, "sensor")
heater = Heater(4, "heater", 25)

c.add_device(lamp)
c.add_device(fan)
c.add_device(sensor)
c.add_device(heater)

# связь сенсор → обогреватель
sensor.linked_heater = heater


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/command/<int:id>")
def command(id):

    d = c.get_device(id)

    if not d:
        return jsonify({"error": "not found"})

    cmd = request.args.get("cmd")

    return jsonify(d.execute_command(cmd))


if __name__ == "__main__":
    app.run(debug=True, port=5001)