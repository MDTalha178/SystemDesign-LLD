from model.atm import ATM
from ATMState.atmState import ATMState

class UpdateATMStateRequestDTO:
    def __init(self, atm: 'ATM', state: 'ATMState'):
        self.atm = atm
        self.state = state
    
    def get_atm(self):
        return self.atm.atm_id
    
    def get_state(self):
        return self.state
    
    def update_atm_status(self):
        print(f"Updating the ATM state at Server: {self.atm.atm_id}")
