class Controller:

    def __init__(self):
        self.devices = []

    def add_device(self, d):
        self.devices.append(d)

    def get_device(self, id):

        for d in self.devices:
            if d.id == id:
                return d

        return None