from dataclasses import dataclass

from Instrument.Instrument import Instrument

@dataclass
class NetBankingInstrument(Instrument):
    username:str
    password:str

    def __post_init__(self):
        if self.username is None:
            raise ValueError("Username is required!")

        if self.password is None:
            raise ValueError("Password is required!")