from components.components_eletronics import Resistor, Capacitor
from math import pi, sqrt


class LowPassOrderOne:
    def __init__(self, res1: float, cap1: float):

        self.__resistor: Resistor = Resistor(res1)
        self.__capacitor: Capacitor = Capacitor(cap1)
        self.__cutoff_frequency: float = self.__calculate_cutoff_frequency(res1, cap1)

    @staticmethod
    def __calculate_cutoff_frequency(resistance: float, capacitance: float):
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
        self.__cutoff_frequency = self.__calculate_cutoff_frequency(res1, cap1, res2, cap2)

    @property
    def resistor1(self):
        return self.__resistor1

    @property
    def capacitor1(self):
        return self.__capacitor1

    @property
    def resistor2(self):
        return self.__resistor2

    @property
    def capacitor2(self):
        return self.__capacitor2

    @staticmethod
    def __calculate_cutoff_frequency(res1: float, cap1: float, res2: float, cap2: float):
        return 1/(2 * pi * sqrt(res1 * res2 * cap1 * cap2))


if __name__ == "__main__":
    lp = LowPassOrderTwo(1E3, 10E-6)
    print(lp.resistor1.resistance)
    print(lp.capacitor1.capacitance)
    print()
