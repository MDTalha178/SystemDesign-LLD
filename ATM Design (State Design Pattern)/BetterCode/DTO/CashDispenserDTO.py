class CashDispenserDTO:

    def __init__(self, atm):
        self.atm = atm
    
    def update_server_despense_cash(self, transaction_id, amount):
        print(f"Updating a the amount for the Transaction ID is: {self.transaction_id}  and amount is {self.amount}")
    
    def get_atm_amount(self):
        return 1000