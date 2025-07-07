from abc import ABC, abstractmethod


# def __init__(self, order_product: OrderProduct):
#     self.order_product = order_product

class OrderStateInterface(ABC):

    @abstractmethod
    def confirm_order_state(self):
        raise NotImplementedError("Subclass should have to implement this method")

    @abstractmethod
    def cancel_order_state(self):
        raise NotImplementedError("Subclass should have to implement this method")

    @abstractmethod
    def pending_order_state(self):
        raise NotImplementedError("Subclass should have to implement this method")

    @abstractmethod
    def refund_order_state(self):
        raise NotImplementedError("Subclass should have to implement this method")

    @abstractmethod
    def get_state(self):
        raise NotImplementedError("Subclass should have to implement this method")
