from typing import Dict, List

from Instrument.CardInstrument import CardInstrument
from Instrument.NetBankingInstrument import NetBankingInstrument
from Instrument.UPIInstrument import UPIInstrument
from Models.Banks.Banks import BankInterface
from Models.Client import Client
from Models.PaymentMethod import PaymentMethod


class PaymentProcessor:

    def __init__(self):
        self.banks:List[BankInterface] =[]

    def add_banks(self, banks:BankInterface):
        self.banks.append(banks)

    @staticmethod
    def validate_instrument(paymentMode:PaymentMethod, instrument_details:Dict):
        if  paymentMode == paymentMode.UPI:
            return UPIInstrument(VPA=instrument_details.get('vpa'))

        elif  paymentMode in (PaymentMethod.CREDIT_CARD, PaymentMethod.DEBIT_CARD):
            return CardInstrument(
                card_number=instrument_details.get('card_number'),
                expiry=instrument_details.get('expiry'),
                cvv=instrument_details.get('cvv')
            )

        elif paymentMode == PaymentMethod.NET_BANKING:
            return(
                NetBankingInstrument(
                    username=instrument_details.get('username'),
                    password=instrument_details.get('password')
                )
            )
        else:
            raise ValueError("Unsupported Payment Mode")

    @staticmethod
    def validate_payment_method(client:Client, paymentMode:PaymentMethod):
        supported_payment_mode = client.get_supported_payment_mode()
        if paymentMode not in supported_payment_mode:
            print(f"{paymentMode.value}: Mode Payment mode is not Supported for {client.name}")
            raise ValueError("Un supported payment Mode")
        return


    @staticmethod
    def process_payment(bank:BankInterface, payMode:PaymentMethod, amount):
        return bank.process_payment(
            payment_mode=payMode,
            amount=amount

        )