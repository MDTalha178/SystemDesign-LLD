class CreditCard:
    def __init__(self, card_number, cvv, expiration_date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiration_date = expiration_date
    

    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card")
    
    def tab_and_pay(self):
        pass

    def do_refund(self, amount):
        pass

    def online_pay(self, amount):
        pass
    
    def swipe_and_pay(slef, amount):
        pass

""""
Here the problem is that when some credit card doesn't support do refund policy int this case those classes wiill throw error
for that we need to segreate a interface
"""