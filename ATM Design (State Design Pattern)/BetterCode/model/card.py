from ATMState.card_type import CardType


class Card:
    def __init__(self, card_number, card_pin, card_holderName, card_type: "CardType", bankName):
        self.card_number = card_number
        self.card_pin = card_pin
        self.card_holderName = card_holderName
        self.card_type = card_type
        self.bankName = bankName

    def get_card_number(self):
        return self.card_number

    def get_card_pin(self):
        return self.card_pin

    def get_card_holderName(self):
        return self.card_holderName

    def get_card_type(self):
        return self.card_type

    def get_bankName(self):
        return self.bankName
