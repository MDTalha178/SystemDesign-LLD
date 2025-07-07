from credicard import CreditCard
from interface import Refund

class VisaCrediCard(CreditCard, Refund):
    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card")
    
    def tab_and_pay(self):
        print("Tab and pay")

    def do_refund(self, amount):
        print(f"Refund of {amount} made using visa credit card")

    def online_pay(self, amount):
        print("online pay using visa credit card")
    
    def swipe_and_pay(slef, amount):
        print("swipe and pay using visa credit card")


