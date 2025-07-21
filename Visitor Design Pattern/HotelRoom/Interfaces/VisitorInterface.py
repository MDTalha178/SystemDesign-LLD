from abc import ABC
from functools import singledispatchmethod
from HotelRoom.Room.SingleRoom import SingleRoom
from HotelRoom.Room.DoubleRoom import DoubleRoom


class Visitor(ABC):
    @singledispatchmethod
    def visit(self, visitor:"Visitor"):
        """Fallback method if no handler is registered for the room type."""
        raise NotImplementedError(f"No visit handler")

    @visit.register
    def _(self, room: SingleRoom):
        raise NotImplementedError("Subclass must implement visit for SingleRoom")

    @visit.register
    def _(self, room: DoubleRoom):
        raise NotImplementedError("Subclass must implement visit for DoubleRoom")
