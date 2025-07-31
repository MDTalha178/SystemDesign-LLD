from django.urls import path, include
from rest_framework.routers import DefaultRouter
from moviesBooking.views import *

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'theatres', TheatreViewSet)
router.register(r'auditoriums', AuditoriumViewSet, basename='audi')
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'seats', SeatsViewSet)
router.register(r'shows', ShowViewSet, basename='show')
router.register(r'show-seats', ShowSeatsViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'users', UserViewSet)
router.register(r'booking', BookingViewSet, basename='booking')
router.register(r'book-tickets', BookTicketViewSet, basename='book_tickets')


urlpatterns = [
    path('', include(router.urls)),
]
