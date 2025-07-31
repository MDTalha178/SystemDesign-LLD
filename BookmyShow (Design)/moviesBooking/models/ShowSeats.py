from utils.base_model import BaseModel
from django.db import models


class ShowSeats(BaseModel):
    class SeatType(models.TextChoices):
        BLOCKED = "BLOCKED"
        LOCK = "LOCK"
        BOOKED = "BOOKED"
        AVAILABLE = "AVAILABLE"

    show = models.ForeignKey(
        'moviesBooking.Show',
        null=True, blank=True,
        related_name='show_seats',
        on_delete=models.CASCADE,
    )

    seats = models.ForeignKey(
        'moviesBooking.Seats',
        null=True, blank=True,
        related_name='show_seats_seats',
        on_delete=models.CASCADE,
    )

    seat_status = models.CharField(
        choices=SeatType.choices,
        null=True, blank=True,
        max_length=255
    )

    class Meta:
        db_table = "show_seats_table"
