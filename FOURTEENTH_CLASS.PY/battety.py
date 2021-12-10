class Battery:
    def __init__(self, size, temperature) -> None:
        self.size = size
        self.cycles = 0
        self.temperature = temperature
        self.charge = 0

    def describe_battery(self):
        print(f"This car has a {self.size} KWH battery, cycles {self.cycles} and temperature {self.temperature}")

    def recharge(self):
        self.charge = 100
        self.cycles += 1