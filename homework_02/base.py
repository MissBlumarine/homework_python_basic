from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 2000
    started = False
    fuel = 35
    fuel_consumption = 10

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Внимание! Пустой бак')

    def move(self, distance):
        fuel = self.fuel - (distance/100) * self.fuel_consumption
        if fuel >= 0:
            self.fuel = fuel
        else:
            raise NotEnoughFuel('Внимание! Необходима дозаправка!')

