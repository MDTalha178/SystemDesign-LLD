import datetime
from models.ParkingSlotModel.FindSlotStrategy import FindSlotStrategy
from models.ParkingSlotModel.Parkinglot import Parkinglot
from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.Tickets.tickets import Ticket
from models.VehcileModels.Vehcile import Vehicle


class ParkingService:

    def __init__(self, find_slot: FindSlotStrategy, parking_lot: Parkinglot):
        self.find_slot = find_slot
        self.parking_lot = parking_lot

    def park_car(self, vehicle: Vehicle):
        parking_slot = self.find_slot.find_slot(vehicle=vehicle, parking_lot=self.parking_lot)

        if not parking_slot:
            print("Parking is Full..Slot not available!")
            return

        parking_slot.set_vehicle(vehicle=vehicle)
        self.parking_lot.parking_slot_in_memory[vehicle.get_registration_number()] = parking_slot.slot_number
        print("Your Vehicle Parked at :", parking_slot.slot_number)
        parking_slot.display()

        # create a Ticket
        ticket: Ticket = Ticket(
            entry_time=datetime.datetime.now(),
            parking_slot=parking_slot,
            vehicle=vehicle,
            pricing_strategy=self.parking_lot.pricing_strategies

        )
        self.parking_lot.ticket_in_memory[vehicle.get_registration_number()] = ticket
        print("Ticket is created for -> ", vehicle.get_registration_number(), + " " + "Ticket Number: ",
              ticket.get_ticket_id())

    def leave_parking(self, vehicle: Vehicle):

        if self.parking_lot.parking_slot_in_memory.get(vehicle.get_registration_number()):
            slot: ParkingSlot = self.parking_lot.parking_slot_in_memory[vehicle.get_registration_number()]
            del self.parking_lot.parking_slot_in_memory[vehicle.get_registration_number()]

            slot.remove_vehicle()

            #Pay before Leave
            ticket: Ticket = self.parking_lot.ticket_in_memory.get(vehicle.get_registration_number())
            ticket.set_exit_time(datetime.datetime.now())
            ticket.calculate_and_pay()

        print("Vehicle not Found!")
