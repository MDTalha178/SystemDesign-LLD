import random
from BetterCode.API.backendAPI import BackendServer
from BetterCode.DTO.UpdateATMStateRequestDTO import UpdateATMStateRequestDTO
from BetterCode.DTO.CashDispenserDTO import CashDispenserDTO


class PythonBackendServer(BackendServer):
    def create_transaction(self, atm_id:str) -> int:
        return random.randint(0, 9)
    
    def update_atm_state(self, update_dto: 'UpdateATMStateRequestDTO'):
        update_dto.update_atm_status()
    
    def update_server_despense_cash(self, despense_dto:"CashDispenserDTO"):
        despense_dto.update_server_despense_cash()
    
    def get_atm_amount(despense_dto:"CashDispenserDTO"):
       return despense_dto.get_atm_amount()