#1
class Car:
    number_of_cars = 0
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        #4
        Car.number_of_cars += 1

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

#2
    def age_of_car(self, current_year=2024):
        age = current_year - self.year
        print(f"The car is {age} years old.")

#5
    def total_cars(cls):
        return cls.number_of_cars

#3
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        #ინგლისურში გადავიყვანე, რადგან ყველაფრის დაბეჭდვა ინგლისურად მაქვს დაწყებული
        print(f"The battery life of this car is {self.battery_life} hours.")

