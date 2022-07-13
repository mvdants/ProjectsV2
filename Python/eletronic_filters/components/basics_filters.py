from .components_eletronics import Resistor, Capacitor, Inductor
from math import pi


class LowPassOrderOne:
    def __init__(self, res1: float, cap1: float):

        self.__resistor: Resistor = Resistor(res1)
        self.__capacitor: Capacitor = Capacitor(cap1)
        self.__cutoff_frequency: float = self.__calculate_cutoff_frequency(res1, cap1)

    @staticmethod
    def __calculate_cutoff_frequency(resistance, capacitance):
        return 1 / (2 * pi * resistance * capacitance)

    @property
    def resistor(self):
        return self.__resistor

    @property
    def capacitor(self):
        return self.__capacitor

    @property
    def cutoff_frequency(self):
        return self.__cutoff_frequency


class LowPassOrderTwo:
    def __init__(self, res1: float, cap1: float, res2: float, cap2: float):

        self.__resistor1 = Resistor(res1)
        self.__resistor2 = Resistor(res2)
        self.__capacitor1 = Capacitor(cap1)
        self.__capacitor2 = Capacitor(cap2)


if __name__ == "__main__":
    lp = LowPassOrderOne(1E3, 10E-6)
    print(lp.resistor.resistance)
    print(lp.capacitor.capacitance)