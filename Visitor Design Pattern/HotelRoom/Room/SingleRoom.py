from HotelRoom.Interfaces.Element import RoomElement
from HotelRoom.Interfaces.VisitorInterface import Visitor


class SingleRoom(RoomElement):

    def accept(self, visitor:Visitor):
        visitor.visit(self)