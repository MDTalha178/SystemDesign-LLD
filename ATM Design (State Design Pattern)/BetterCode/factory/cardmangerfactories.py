from services.cardManagerServices import CardManager
from services.DebitCardmanager import DebitCardManager
from services.CreditCardManager import CreditCardManager
from ATMState.card_type import CardType


class CardManagerFactory:

    @staticmethod
    def get_card_manager(cart_type: "CardType"):
        card_manager: "CardManager" = None

        if CardType.DEBIT_CARD == cart_type:
            card_manager = DebitCardManager()

        if CardType.CREDIT_CARD == cart_type:
            card_manager = CreditCardManager()

        return card_manager
