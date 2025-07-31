from rest_framework import serializers

from moviesBooking.Service.RedisBookingService import RedisBookingService
from moviesBooking.models import (
    Auditorium, City, Movie, Seats, Show,
    ShowSeats, Theatre, Tickets, User
)


class ShowNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ['id', 'show_time', 'show_end_time']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    show = serializers.SerializerMethodField()

    @staticmethod
    def get_show(obj):
        shows = obj.movie_show.all()
        return ShowNestedSerializer(shows, many=True).data

    class Meta:
        model = Movie
        fields = '__all__'


class NestedMovie(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movie_name', 'movie_poster',)


class ShowSerializer(serializers.ModelSerializer):
    movie = NestedMovie()

    class Meta:
        model = Show
        fields = '__all__'


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'


class ShowSeatsSerializer(serializers.ModelSerializer):
    seats = SeatsSerializer()

    class Meta:
        model = ShowSeats
        fields = '__all__'


class AuditoriumSerializer(serializers.ModelSerializer):
    seats = serializers.SerializerMethodField()

    class Meta:
        model = Auditorium
        fields = ['id', 'name', 'capacity', 'seats']

    def get_seats(self, obj):
        # Get all shows associated with the auditorium
        shows = obj.show.all()

        # Get all ShowSeats entries related to those shows
        show_seats_qs = ShowSeats.objects.filter(show__in=shows).select_related('seats', 'show')

        # Serialize those ShowSeats
        return ShowSeatsSerializer(show_seats_qs, many=True).data


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    show_id = serializers.CharField(required=True)
    seat_id = serializers.ListSerializer(
        child=serializers.CharField(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.booking_service = RedisBookingService()

    def validate(self, attrs):
        self.booking_service.block_seat(attrs.get('show_id'), attrs.get('seat_id'), attrs.get('user_id'))
        return attrs

    def create(self, validated_data):
        try:
            tickets = self.booking_service.book_ticket(
                validated_data.get('user_id'), validated_data.get('show_id'), validated_data.get('seat_id')
            )
            return tickets
        except Exception as e:
            serializers.ValidationError("Some thing went wrong")

    class Meta:
        model = ShowSeats
        fields = ('user_id', 'show_id', 'seat_id',)
