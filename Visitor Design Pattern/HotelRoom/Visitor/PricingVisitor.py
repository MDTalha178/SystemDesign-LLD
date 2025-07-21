from HotelRoom.Interfaces.VisitorInterface import Visitor
from HotelRoom.Room.DoubleRoom import DoubleRoom
from HotelRoom.Room.SingleRoom import SingleRoom
from functools import singledispatch

class PricingVisitor(Visitor):

    @singledispatch
    def visit(self, vis:Visitor):
        raise NotImplementedError("There is such kind of visitor")

    @visit.regsiter
    def _(self, visitor:SingleRoom):
        print("Single Room pricing: 100")

    @visit.regsiter
    def _ (self, visitor:DoubleRoom):
        print("Double Room pricing: 200")