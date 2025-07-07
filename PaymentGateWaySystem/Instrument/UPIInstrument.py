from dataclasses import dataclass

from Instrument.Instrument import Instrument


@dataclass
class UPIInstrument(Instrument):
    VPA:str
    def __post_init__(self):
        if self.VPA is None:
            raise ValueError("VPA is required for UPI")

        if '@' not in self.VPA:
            raise ValueError("Invalid VPA Format")