from Credit_Card import CreditCard
from interface import Refund, RefundInSameElement
class VisaCreditCard(CreditCard, Refund):
    def __init__(self, credit_card_number, cvv, expiration_date, refund_logic):
        self.refund_logic = refund_logic
        super().__init__(credit_card_number, cvv, expiration_date)

    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card") 
    
    def online_pay(self, amount):
        print("online pay using visa credit card")
    
    def tab_and_pay(self):
        print("Tab and pay from Visa credit card")
    
    def online_pay(self, amount):
        print("online pay using visa credit card")
    
    def swipe_and_pay(self, amount):
        print("swipe and pay using visa credit card")
    
    def refund(self, amount):
        self.refund_logic.do_refund(amount)


visa_credit_obj = VisaCreditCard("1234 1234 1234 1234", "123", "12/2023", RefundInSameElement())

visa_credit_obj.make_payment(1000)
visa_credit_obj.online_pay(1000)
visa_credit_obj.tab_and_pay()
visa_credit_obj.swipe_and_pay(1000)
visa_credit_obj.refund(1000)