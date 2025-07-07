from model.card import Card
from model.visa import Visa
from model.debitCard import DebitCard

class VisaDebitCard(Card, Visa, DebitCard):
    def __init__(self, card_number, card_pin, card_holderName, card_type, bankName):

        """
        Initializes a VisaDebitCard object with the given parameters.

        Parameters
        ----------
        card_number : str
            The card number of the card.
        card_pin : str
            The PIN of the card.
        card_holderName : str
            The name of the card holder.
        card_type : str
            The type of the card, for example "VISA".
        bankName : str
            The name of the bank that issued the card.
        """

        super().__init__(card_number, card_pin, card_holderName, card_type, bankName)
    

    def makePinPayment(self):
        """
        Makes a payment using the card's PIN.

        Connects to the Visa payment network and then prints a message to
        indicate that the payment was made using the card's PIN.
        """
        self.connectToVisa()
        print("Pin Based Payment")
    
    def connectToVisa(self):
        """
        Connects to the Visa payment network.

        Prints a message to indicate that the connection to the Visa payment
        network was successful.
        """

        print("Connecting to Visa")
    