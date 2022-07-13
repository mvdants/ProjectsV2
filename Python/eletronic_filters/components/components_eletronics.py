from math import pi
from math import log
from math import e


air_permittivity = 8.85 * 10E-12
air_permeability = 4 * pi * 10E-7


class Resistor:
    def __init__(self, value: float = None):
        self.__resistance = value

    @property
    def resistance(self):
        return self.__resistance

    @staticmethod
    def calculate_resistance(rho: float, length: float, surface: float):
        """
        Measurement of the resistance value.

        :param rho: resistivity material
        :param length: material length
        :param surface: material surface
        :return: measurement of the material resistance
        """
        return (rho * length)/surface


class Capacitor:
    def __init__(self, value):
        self.__capacitance = value

    @property
    def capacitance(self):
        return self.__capacitance

    @staticmethod
    def calculate_capacitance(model: str = "parallel", *args, **kwargs):
        """
        Measurement of a capacitance. This component can has two models : "parallel" and "cylinder". The most
        commons types of capacitors in the market.

        :param model: capacitor model -> "parallel" or "cylinder".
        :param args: this parameter depend about which capacitor model you choose.
                    "parallel" model -> surface: float, distance: float
                    "cylinder" model -> length: float, rayon_in: float, rayon_out: float

        :return: The result of the capacitance model
        """
        if model == "parallel":
            return Capacitor.parallel_capacitance(*args, **kwargs)
        elif model == "cylinder":
            return Capacitor.cylinder_capacitance(*args, **kwargs)
        else:
            raise ValueError("any model recognized")

    @staticmethod
    def parallel_capacitance(surface: float, distance: float, material_permittivity: float = 1.0):
        """
        Measurement of the value of a parallel capacitance.

        :param surface: surface of the parallel plates
        :param distance: distance between the parallel plates
        :param material_permittivity: permittivity material value. air == 1
        :return: measurement result
        """
        return (surface * air_permittivity * material_permittivity)/distance

    @staticmethod
    def cylinder_capacitance(length: float, rayon_in: float, rayon_out: float, material_permittivity: float = 1.0):
        """
        Measurement of the value of a cylinder capacitance.

        :param length: cylinder length
        :param rayon_in: cylinder inner rayon value
        :param rayon_out: cylinder outer rayon value
        :param material_permittivity: permittivity material value. air == 1
        :return: measurement result
        """
        return 2 * pi * air_permittivity * (length/(log(rayon_out/rayon_in, e)))


class Inductor:
    def __init__(self, value):
        self.__inductance = value

    @property
    def inductance(self):
        return self.__inductance

    @staticmethod
    def calculate_inductance(number_of_turns: int, surface: float, length: float, material_permeability: float):
        """
        Measurement of the inductance from the base calculation.

        :param number_of_turns: absolute number of turns of wire
        :param surface: center surface where the magnetic field passes
        :param length: the length of the core
        :param material_permeability: the value of the material permeability
        :return: the measurement of the inductance
        """
        return pow(number_of_turns, 2) * surface * air_permeability * (1 / length)


if __name__ == "__main__":
    cap = Capacitor.calculate_capacitance("parallel", surface=100E-6, distance=1E-6)
    print(cap)