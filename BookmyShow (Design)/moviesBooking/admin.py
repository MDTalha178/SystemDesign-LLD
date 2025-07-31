from django.contrib import admin

from moviesBooking.models.Audutorium import Auditorium
from moviesBooking.models.City import City
from moviesBooking.models.Movie import Movie
from moviesBooking.models.Seats import Seats
from moviesBooking.models.Show import Show
from moviesBooking.models.ShowSeats import ShowSeats
from moviesBooking.models.Theatre import Theatre
from moviesBooking.models.Tickets import Tickets
from moviesBooking.models.User import User


# Register your models here.
admin.site.register(User)
admin.site.register(Auditorium)
admin.site.register(City)
admin.site.register(Show)
admin.site.register(Seats)
admin.site.register(ShowSeats)
admin.site.register(Theatre)
admin.site.register(Tickets)
admin.site.register(Movie)