from Credit_Card import CreditCrad

class AmexCreditCard(CreditCrad):
    def tab_and_pay(self):
        print("Tab and pay from Amex credit card")
    
    def swipe_and_pay(self, amount):
        print("swipe and pay using Amex credit card")
    
    def online_pay(self, amount):
        print("online pay using Amex credit card")
    
    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card")
    

