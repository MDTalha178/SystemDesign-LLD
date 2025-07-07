"""
Before moving forward we will understand to terms
1:Thread Race Condition -> it is a situation when two or more thread are running at
the same time and try access a same code
2: Thread Synchronization -> it is a mechanism which is used to synchronize the thread
the same time and try access a same code
"""

# here we will create Thread Race condition
from threading import Thread, Lock


class FlightBookingRaceCondition:

    def __init__(self) -> None:
        self.flight_name = "Air India"
        self.total_number_of_seats = 100
        self.available_seats = 100
        self.__lock = Lock()

    def book_ticket(self, name, number_of_seats):

        print("Number of seats are viable {}".format(self.available_seats))
        try:
            with self.__lock:
                if self.available_seats >= number_of_seats:
                    print("Please wait we are in process...")
                    print("Great News seat are available please wait..")
                    self.available_seats = self.available_seats - number_of_seats
                    print("Congratulations {} your fight booking is Successful!".format(name))

                else:
                    print("Sorry {} seat are not available".format(name))
        except Exception as e:
            print("Seat are busy right now")


# here we are creating object for FlightBookingRaceCondition
flight_booking_race_obj = FlightBookingRaceCondition()

# here we are creating thread object for FlightBookingRaceCondition to book ticket
thread1 = Thread(target=flight_booking_race_obj.book_ticket, args=('Mohammad Talha', 34))
thread1.start()

# here we are creating thread object for FlightBookingRaceCondition to book ticket
thread2 = Thread(target=flight_booking_race_obj.book_ticket, args=('Mohammad Talha', 34))
thread2.start()

# here we are creating thread object for FlightBookingRaceCondition to book ticket
thread3 = Thread(target=flight_booking_race_obj.book_ticket, args=('Mohammad Talha', 34))
thread3.start()

"""
Now here let's understand Race condition suppose we have two thread which are 
running at the same time and try to access a same code at some seat will 
not avilable logically but i will bokk becuase it is running at the same time
but from different Thread to solve problem we will used Locking concept
"""