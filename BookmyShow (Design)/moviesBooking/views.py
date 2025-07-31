from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from moviesBooking.Service.AuditoriumService import AuditoriumService
from moviesBooking.Service.MovieService import MovieService
from moviesBooking.Service.ShowService import ShowService
# Create your views here.
from moviesBooking.serializer import *
from rest_framework import viewsets, status
from moviesBooking.models import (
    Auditorium, City, Movie, Seats, Show,
    ShowSeats, Theatre, Tickets, User
)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class TheatreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer


class AuditoriumViewSet(viewsets.ReadOnlyModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AuditoriumService()

    def list(self, request):
        movies = self.service.get_auditorium_by_show_id
        serializer = MovieSerializer(movies, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        audi = self.service.get_auditorium_by_show_id(show_id=pk)
        print(audi)
        if not audi:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AuditoriumSerializer(audi, many=True)
        return Response(serializer.data)


class MovieViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = MovieService()

    def list(self, request):
        movies = self.service.get_all_movie()
        serializer = MovieSerializer(movies, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        movie = self.service.get_movie_by_id(pk)
        if not movie:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class SeatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer


class ShowViewSet(viewsets.ReadOnlyModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ShowService()

    def list(self, request):
        movies = self.service.show_repo.get_all_show()
        serializer = ShowSerializer(movies, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        show = self.service.show_repo.find_show_by_id(pk)
        if not show:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowSerializer(show)
        return Response(serializer.data)


class ShowSeatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShowSeats.objects.all()
    serializer_class = ShowSeatsSerializer


class TicketsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewSet(ModelViewSet):
    http_method_names = ('post', 'get',)
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            # serializers.save()
            return Response(
                data={'Success': True, 'message': "Booking Successful"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializers.errors,
            status=status.HTTP_400_BAD_REQUEST

        )


class BookTicketViewSet(ModelViewSet):
    http_method_names = ('post', 'get',)
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                data={'Success': True, 'message': "Booking Successful"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializers.errors,
            status=status.HTTP_400_BAD_REQUEST

        )

