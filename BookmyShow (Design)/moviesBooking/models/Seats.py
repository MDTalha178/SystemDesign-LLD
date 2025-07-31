from utils.base_model import BaseModel
from django.db import models


class Seats(BaseModel):
    class SeatType(models.TextChoices):
        NORMAL = "NORMAL"
        PERINEUM = "PERINEUM"
        VIP = "VIP"

    seat_number = models.CharField(null=False, blank=False, max_length=255)
    row = models.CharField(null=True, blank=True, max_length=255)
    column = models.CharField(null=True, blank=True, max_length=255)

    seat_type = models.CharField(
        choices=SeatType.choices,
        default=SeatType.NORMAL,
        max_length=255
    )

    auditorium = models.ForeignKey(
        'moviesBooking.Auditorium', null=True, blank=False,
        related_name="seats_auditorium",
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = "seats"
