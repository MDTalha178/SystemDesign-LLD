from dataclasses import dataclass

from Instrument.Instrument import Instrument


@dataclass
class CardInstrument(Instrument):
    card_number:str
    expiry:str
    cvv:str

    def __post_init__(self):
        if self.card_number is None:
            raise ValueError("Card Number is required")

        if self.expiry is None:
            raise ValueError("Expiry Number is required")

        if self.cvv is None:
            raise ValueError("Expiry Number is required")