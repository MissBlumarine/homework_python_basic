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

    def start(self, started, fuel):
        if started == True:
            return "Двигатель уже работает"
        if started == False and fuel > 0:
            started = True
            return "Двигатель запущен"
        if started == False and fuel <= 0:
            raise LowFuelError('Внимание! Пустой бак')

    def move(self, distance, fuel, fuel_consumption):
        d = distance / fuel_consumption
        c = fuel - d
        if c >= 0:
            return c
        if c < 0:
            raise NotEnoughFuel('Внимание! Необходима дозаправка!')
