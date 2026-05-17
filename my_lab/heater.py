class Heater:
    def __init__(self, id, name, threshold=25):
        self.id = id
        self.name = name
        self.threshold = threshold
        self.status = "off"

    def auto_power(self, temperature):
        if temperature < self.threshold:
            self.status = "on"
        else:
            self.status = "off"

    def execute_command(self, cmd):
        if cmd.startswith("set:"):
            try:
                self.threshold = float(cmd.split(":")[1])
                return {"threshold": self.threshold}
            except:
                return {"error": "bad format"}

        return {"error": "unknown command"}
