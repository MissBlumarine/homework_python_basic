from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 2000
    started = False
    fuel = 35
    fuel_consumption = 11

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
        d = distance / self.fuel_consumption
        c = self.fuel - d
        if c >= 0:
            return c
        raise NotEnoughFuel('Внимание! Необходима дозаправка!')
