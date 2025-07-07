class CreditCard:
    def __init__(self, credit_card_number, cvv, expiration_date):
        self.credit_card_number = credit_card_number
        self.cvv = cvv
        self.expiration_date = expiration_date
    

    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card")
    
    def tab_and_pay(self):
        pass


    def online_pay(self, amount):
        pass
    
    def swipe_and_pay(slef, amount):
        pass 