class Database:

    def __init__(self):

        self.devices_db = {}

    def save_device(self, device):

        self.devices_db[device.id] = {
            "name": device.name,
            "status": device.status
        }

    def remove_device(self, device):

        if device.id in self.devices_db:
            del self.devices_db[device.id]