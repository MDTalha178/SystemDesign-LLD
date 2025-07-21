from functools import singledispatch

from HotelRoom.Interfaces.VisitorInterface import Visitor
from HotelRoom.Room.DoubleRoom import DoubleRoom
from HotelRoom.Room.SingleRoom import SingleRoom
from HotelRoom.Visitor.PricingVisitor import PricingVisitor


class MaintenanceVisitor(PricingVisitor):

    @singledispatch
    def visit(self, vis: Visitor):
        raise NotImplementedError("There is such kind of visitor")

    @visit.regsiter
    def _(self, visitor: SingleRoom):
        print("Single Room  is Under Maintenance")

    @visit.regsiter
    def _(self, visitor: DoubleRoom):
        print("Double room is available ")