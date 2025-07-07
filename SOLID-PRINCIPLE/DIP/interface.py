from abc import ABC, abstractmethod

class Refund(ABC):

    @abstractmethod
    def refund(self, amount):
        pass

class RefundInterFace:

    @abstractmethod
    def do_refund(self, amount):
        pass


class RefundInSameElement(RefundInterFace):

    def do_refund(self, amount):
        print(f"Refund of {amount} made  using same Refund Element")
    

class WalletRefund(RefundInterFace):

    def do_refund(self, amount):
        print(f"Refund of {amount} made  using wallet")