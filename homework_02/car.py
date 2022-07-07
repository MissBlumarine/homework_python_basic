"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, engine):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = Engine

    def set_engine(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons
        self.engine = Engine(volume=volume, pistons=pistons)



