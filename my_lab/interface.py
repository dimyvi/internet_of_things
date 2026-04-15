from controller import Controller


class UserInterface:
    def __init__(self, c):
        self.c = c

    def run(self):
        while True:
            print("\n1) включить все девайсы")
            print("2) выключить все девайсы")
            print("3) логаут")

            try:
                v = int(input("выбери: "))
            except:
                print("Нужна цифра")
                continue

            if v == 3:
                self.c.logout()
                break
            elif v == 1:
                self.c.turn_on_all()
            elif v == 2:
                self.c.turn_off_all()


class AdminInterface:
    def __init__(self, c):
        self.c = c

    def run(self):
        while True:
            print("\n1) добавить девайс")
            print("2) удалить девайс")
            print("3) получить девайс по id")
            print("4) получить список всех девайсов")
            print("5) включить все девайсы")
            print("6) выключить все девайсы")
            print("7) логаут")

            try:
                v = int(input("выбери: "))
            except:
                print("Нужна цифра")
                continue

            if v == 7:
                self.c.logout()
                break

            elif v == 1:
                print("пока не реализовано")

            elif v == 2:
                try:
                    id = int(input("id девайса: "))
                    d = self.c.get_device(id)
                    if d:
                        self.c.remove_device(d)
                    else:
                        print("нет такого")
                except:
                    print("ошибка")

            elif v == 3:
                try:
                    id = int(input("id: "))
                    d = self.c.get_device(id)
                    if d:
                        st = "on" if d.status == "on" else "off"
                        print(f"  {st} {d.name}")
                    else:
                        print("нет")
                except:
                    print("ошибка")

            elif v == 4:
                devs = self.c.get_all_devices()
                if not devs:
                    print("пусто")
                else:
                    for d in devs:
                        st = "on" if d.status == "on" else "off"
                        print(f"  [{d.id}] {st} {d.name}")

            elif v == 5:
                self.c.turn_on_all()

            elif v == 6:
                self.c.turn_off_all()