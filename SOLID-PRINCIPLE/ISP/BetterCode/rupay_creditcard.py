from credicard import CreditCard
from interface import Refund
from rupay_refund_strategy import RupayRefundStrategy

class RupayCrediCard(CreditCard, Refund):
    def init__(self):
        self.refund_strategy = RupayRefundStrategy()
    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card")
    
    def tab_and_pay(self):
        print("Tab and pay")

    def do_refund(self, amount):
        print(f"Refund of {amount} made using rupay credit card")
        self.refund_strategy.do_refund(amount)

    def online_pay(self, amount):
        print("online pay using visa rupay card")
    
    def swipe_and_pay(slef, amount):
        print("swipe and pay using rupay credit card")



