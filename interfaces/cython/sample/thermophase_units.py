import cantera as ct
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

class ThermoPhaseUnits(ct.ThermoPhase):
    @property
    def TP(self):
        T, P = self.thermo.TP
        return Q_(T, "K"), Q_(P, "Pa")
    @TP.setter
    def TP(self, T, P):
        if T is not None:
            T = T.to("K").magnitude 
        else:
            self.thermo.T
        if P is not None:
            P = P.to("Pa").magnitude 
        else:
            self.thermo.P
        self.thermo.TP = T, P
