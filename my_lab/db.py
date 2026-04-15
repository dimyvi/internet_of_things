class Database:
    def __init__(self):
        self.devices_db = {}
        self.users = {"admin": "admin", "user": "12345"}

    def save_device(self, device):
        self.devices_db[device.id] = {
            "name": device.name,
            "status": device.status
        }

    def remove_device(self, device):
        if device.id in self.devices_db:
            del self.devices_db[device.id]

    def check_user(self, username, password):
        if username in self.users:
            return self.users[username] == password
        return False