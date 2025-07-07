from Credit_Card import CreditCard
from interface import Refund, WalletRefund

class RupayCreditCard(CreditCard, Refund):
    def __init__(self, credit_card_number, cvv, expiration_date, refund_logic):
        self.refund_logic = refund_logic
        super().__init__(credit_card_number, cvv, expiration_date)

    def swipe_and_pay(self, amount):
        print("swipe and pay using rupay credit card") 
    
    def online_pay(self, amount):
        print("online pay using rupay credit card")
    
    def tab_and_pay(self, amount):
        print(f"Tab and pay  {amount} from rupay credit card")
    
    def make_payment(self, amount):
        print(f"Payment of {amount} made using rupay credit card")
    
    def refund(self, amount):
        self.refund_logic.do_refund(amount)

rupay_card = RupayCreditCard("1234 1234 1234 1234", "123", "12/2023", WalletRefund())
rupay_card.make_payment(1000)
rupay_card.swipe_and_pay(1000)
rupay_card.online_pay(1000)
rupay_card.tab_and_pay(1000)
rupay_card.refund(1000)