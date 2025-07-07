from enum import Enum
import random

class ATMState(Enum):
    IDLE = 'IDLE'
    TRNSACTION_IN_PROGRESS = 'TRNSACTION_IN_PROGRESS'
    CARD_INSERTED = 'CARD_INSERTED'
    AMOUNT_ENTERED = 'AMOUNT_ENTERED'
    CASH_DIPNESE = 'CASH_DIPNESE'

class ATMService:

    CARD_SUPPORT = ['VISA', 'RUPAY', 'MASTERCARD']
    DUMMPY_PIN = ['1234', '7098']

    def __init__(self, atm_Id):
        self._atm_Id =  atm_Id
        self.atm_state = ATMState.IDLE
    
    def start_transaction(self):
        if self.atm_state != ATMState.IDLE:
            raise ValueError('ATM machine Already in used!')
        
        self.atm_state = ATMState.TRNSACTION_IN_PROGRESS
        return self.generate_transaction_id()

    def generate_transaction_id(self):
        return str(random.randint(0, 9))
    
    def read_card(self, card_type, card_number, card_pin):
        if self.atm_state != ATMState.TRNSACTION_IN_PROGRESS:
            raise ValueError("Transaction is Not in Progress!")
        
        is_valid_card_type = self.validate_card_type(card_type)
        if is_valid_card_type is False:
            self.atm_state = ATMState.IDLE
            raise ValueError(f"Card Type is in Valid.. {card_type} is not supported fo this machine")
        
        is_valid_card = self.validate_card(card_number)
        if is_valid_card is False:
            self.atm_state = ATMState.IDLE
            raise ValueError('Card Number is Invalid!')

        is_valid_pin = self.validate_pin(card_pin)
        if is_valid_pin is False:
            self.atm_state = ATMState.IDLE
            raise ValueError('Pin is Invalid!')
        self.atm_state = ATMState.CARD_INSERTED
    
    def widthraw_cash(self, transation_id, amount):
        if self.atm_state != ATMState.CARD_INSERTED:
            self.atm_state = ATMState.IDLE
            raise('Crad Not Inerted!')
        
        is_valid_amount = self.validate_widthrwal_amount(amount)
        if is_valid_amount is False:
            raise ValueError('Amount is Inavlid!')
        
        print(f"Trnsaction is valid for {transation_id} and amount {amount}")
        self.atm_state = ATMState.CASH_DIPNESE
        return is_valid_amount

    def validate_widthrwal_amount(self, amount):
        return amount <= 1000
    
    def dispense_amount(self, amount):
        if self.atm_state != ATMState.CASH_DIPNESE:
            raise ("Transaction not Initiated!")
        print(f"Dispnesing cash Amount {amount}")
        self.dectuct_amount(amount)
        self.atm_state = ATMState.IDLE
    
    def dectuct_amount(self, amount):
        print(f"Amount is {amount} Detucted Succfully!")
    
    def validate_card_type(self, card_type:str):
        print(card_type.upper())
        if card_type.upper() in self.CARD_SUPPORT:
            return True
        return False
    
    def validate_card(self, card_number):
        if len(card_number) == 14:
            return True
        return False
    
    def validate_pin(self, pin):
        if pin in self.DUMMPY_PIN:
            return True
        
        return False
    

    
atm_obj = ATMService(1234)
transation_id = atm_obj.start_transaction()
transation_id = atm_obj.start_transaction()
atm_obj.read_card('visa', "12345678912345", "1234")
atm_obj.widthraw_cash(transation_id, 500)
atm_obj.dispense_amount(500)