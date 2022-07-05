"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, engine):
        Vehicle.__init__(self, weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        """
        не могу понять как наследовать от dataclass Engine
        и как установить на car экземпляр engine"""
        pass


