from state.readyState import ReadyState
from API.backendAPI import BackendServer
from state.state import State
from DTO.UpdateATMStateRequestDTO import UpdateATMStateRequestDTO


class ATM:
    atm_id = None
    state = None

    def __init__(self, atm_id: str):
        self.atm_id = atm_id
        self.backend_server = BackendServer
        self.state = ReadyState(self)

    def get_atm_id(self):
        return self.atm_id

    def update_status(self, atm_state: 'State'):
        self.state = atm_state

        # called a backend to update the state
        self.backend_server.update_atm_state(UpdateATMStateRequestDTO(self, self.state.get_state()))


atm_obj = ATM("1234")
