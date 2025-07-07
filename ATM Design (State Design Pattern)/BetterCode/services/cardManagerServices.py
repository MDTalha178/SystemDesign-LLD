from abc import ABC, abstractmethod
from model.card import Card


class CardManager(ABC):

    @abstractmethod
    def validateCard(self, card: "Card", pin: str) -> bool:
        """
        Validates a card and a pin.

        Parameters
        ----------
        card : Card
            The card to validate.
        pin : str
            The pin to validate.

        Returns
        -------
        bool
            True if the card and pin are valid, False otherwise
        """

        pass

    @abstractmethod
    def validate_widthrwal(self, transaction_id: int, amount: int) -> bool:
        """
        Validates whether the amount to withdraw is valid for the given card.

        Parameters
        ----------
        card : Card
            The card to validate.
        amount : int
            The amount to withdraw.

        Returns
        -------
        bool
            True if the amount to withdraw is valid, False otherwise
        """

        pass

    @abstractmethod
    def dotTransaction(self, card: "Card", amount: int, transaction_id: int) -> bool:
        """
        Performs a transaction on the given card.

        Parameters
        ----------
        card : Card
            The card to perform the transaction on.
        amount : int
            The amount to withdraw.
        transaction_id : int
            The unique id of the transaction.

        Returns
        -------
        bool
            True if the transaction is successful, False otherwise
        """

        pass
