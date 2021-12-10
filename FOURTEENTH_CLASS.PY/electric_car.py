from CARRO import Car
from battety import Battery

class ElectricCar(Car):
    
    def __init__(self, trademark, model, year):
        super().__init__(trademark, model, year)

        self.baterry = Battery(75, 30)


    def fill_gas_tank(self): #polimorfismo
        #return super().fill_gas_tank()
        print("You don't need to fill the tank, this is a electric car")

    def describe_battery(self):
        self.baterry.describe_battery()
    
    def recharge_battery(self):
        self.baterry.recharge()


my_tesla = ElectricCar("Tesla", "S", 2020)

my_tesla.fill_gas_tank()

