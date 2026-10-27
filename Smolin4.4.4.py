class Device:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        return f"Пристрій {self.name} увімкнено."

    def turn_off(self):
        return f"Пристрій {self.name} вимкнено."


class Smartphone(Device):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def turn_on(self):
        return f"Смартфон {self.brand} ({self.name}) завантажується та увімкнений."

    def open_app(self, app_name):
        return f"На смартфоні {self.name} відкрито додаток '{app_name}'."


class Television(Device):
    def __init__(self, name, screen_size):
        super().__init__(name)
        self.screen_size = screen_size

    def turn_on(self):
        return f"Телевізор {self.name} з екраном {self.screen_size} дюймів увімкнено."

    def change_channel(self, channel_number):
        return f"Телевізор {self.name} перемкнуто на канал {channel_number}."


if __name__ == "__main__":
    phone = Smartphone("iPhone", "Apple")
    tv = Television("Samsung", 55)

    print(phone.turn_on())
    print(phone.open_app("Telegram"))
    print(phone.turn_off())

    print("-" * 30)

    print(tv.turn_on())
    print(tv.change_channel(5))
    print(tv.turn_off())