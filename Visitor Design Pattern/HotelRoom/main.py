from HotelRoom.Room.DoubleRoom import DoubleRoom
from HotelRoom.Visitor.PricingVisitor import PricingVisitor

price_visitor = PricingVisitor()

double_room = DoubleRoom().accept(visitor=price_visitor)