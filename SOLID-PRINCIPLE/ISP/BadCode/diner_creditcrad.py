from credicard import CreditCard


class DinnerCrediCard(CreditCard):
    def make_payment(self, amount):
        print(f"Payment of {amount} made using credit card")
    
    def tab_and_pay(self):
        print("Tab and pay")

    def do_refund(self, amount):
        print(f"Refund of {amount} made using dinner credit card")

    def online_pay(self, amount):
        print("online pay using visa dinner card")
    
    def swipe_and_pay(slef, amount):
        print("swipe and pay using dinner credit card")

