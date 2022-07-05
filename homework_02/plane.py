"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo):
        Vehicle.__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, a, cargo, max_cargo):
        if (a + cargo) <= max_cargo:
            cargo += a
            return cargo
        if (a + cargo) > max_cargo:
            raise CargoOverload("Внимание, перегруз!")

    def remove_all_cargo(self):
        cargo = cargo - a
        return cargo


