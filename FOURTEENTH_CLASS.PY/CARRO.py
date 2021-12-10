class Car:
    def __init__(self, trademark, model, year):
        self.trademark = trademark
        self.model = model
        self.year = year
        self.odometer_value = 0
        self.tank = 0
        
    def get_descriptive_name(self):
        return f"{self.trademark}  {self.model}  {self.year}"

    def read_odometer(self):
        print(f" This car has {self.odometer_value} kilometer on it.")

    def set_odometer_value(self, kilometers):
        if kilometers > self.odometer_value:
            self.odometer_value = kilometers
        
        else:
            print("The odometer das not go back")

    def fill_gas_tank(self):
        self.tank = 100


    

my_car = Car("Audi", "A4", 2021)

print( my_car.get_descriptive_name())

my_car.read_odometer()