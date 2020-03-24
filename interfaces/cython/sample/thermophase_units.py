import cantera
from . import utilities

from pint import UnitRegistry

ureg = UnitRegistry()

Q = ureg.Quantity

class ThermoPhaseUnits:
    def __init__(self, *args, **kwargs):
        self.thermo = ThermoPhase(*args, **kwargs)
    @property
    def setState_TP():
        T,P = self.thermo.setState_TP
        return Q(T,"K"),Q(P,"Pa")
    @setState_TP.setter
    def setState_TP_units(self, T, P):
        if T is not None:
            T = T.to("K").magnitude 
        else:
            self.thermo.T
        if P is not None:
            P = P.to("Pa").magnitude 
        else:
            self.thermo.P
        self.thermo.TP = T, P
