from abc import ABC, abstractmethod
from DTO.UpdateATMStateRequestDTO import UpdateATMStateRequestDTO
from DTO.CashDispenserDTO import CashDispenserDTO


class BackendServer(ABC):

    @abstractmethod
    def create_transaction(self, atm_id: str) -> int:
        """
        Starts a new transaction and returns a unique transaction id.
        Transaction id can be used to verify the transaction.

        Args:
            atm_id (str): The id of the atm machine

        Returns:
            int: A unique transaction id
        """
        pass

    @abstractmethod
    def update_atm_state(self, update_dto: 'UpdateATMStateRequestDTO'):
        """
        Updates the state of the ATM machine.

        Args:
            update_dto (UpdateATMStateRequestDTO): The data transfer object that contains the atm machine state.
        """

        pass

    @abstractmethod
    def update_server_despense_cash(self, despense_dto:"CashDispenserDTO"):
        NotImplementedError("Sub class should be Implement this")
    
    @abstractmethod
    def get_atm_amount(self, despense_dto:"CashDispenserDTO"):
        NotImplementedError("Sub class should be Implement this")

