from components.components_eletronics import Capacitor, Resistor
from math import pi, sqrt
from numpy import ndarray, array
import matplotlib.pyplot as plt


class HighPassOrderOne:
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


class HighPassOrderTwo:
    def __init__(self, res1: float, cap1: float, res2: float, cap2: float):
        self.__resistor1 = Resistor(res1)
        self.__resistor2 = Resistor(res2)
        self.__capacitor1 = Capacitor(cap1)
        self.__capacitor2 = Capacitor(cap2)
        self.__cutoff_frequency = self.__calculate_cutoff_frequency(res1, cap1, res2, cap2)
        self.__transfer_function: ndarray = array([])

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

    @property
    def cutoff_frequency(self):
        return self.__cutoff_frequency

    @staticmethod
    def __calculate_cutoff_frequency(res1: float, cap1: float, res2: float, cap2: float):
        return 1 / (2 * pi * sqrt(res1 * res2 * cap1 * cap2))

    def calculate_transfer_function(self, f: float):
        """Here we are considering that the gain of the circuit is 1"""

        upper = (self.__resistor1.resistance * self.__capacitor2.capacitance) + \
                (self.__resistor2.resistance * self.__capacitor2.capacitance)

        lower = self.__resistor1.resistance * self.__resistor2.resistance * \
                self.__capacitor1.capacitance * self.__capacitor2.capacitance

        ew = upper / lower
        s = 2 * pi * f

        return pow(s, 2) + 2 * ew * s + pow((2 * pi * self.__cutoff_frequency), 2)


if __name__ == "__main__":
    hp = HighPassOrderTwo(res1=10E3, cap1=1E-9, res2=10E3, cap2=1E9)
    print(hp.cutoff_frequency)
    arr = array([range(1, int(hp.cutoff_frequency + 10000), 1)])
    for value in arr:
        arr = hp.calculate_transfer_function(value)

    plt.plot(arr)
    plt.show()
