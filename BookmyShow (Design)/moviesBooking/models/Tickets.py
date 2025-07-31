from utils.base_model import BaseModel
from django.db import models


class Tickets(BaseModel):
    class TicketStatus(models.TextChoices):
        BOOKED = "BOOKED"
        PENDING = "PENDING"
        FAILED = "FAILED"

    user = models.ForeignKey(
        'moviesBooking.User', null=False, blank=False,
        related_name='tickets_user',
        on_delete=models.CASCADE
    )

    show = models.ForeignKey(
        'moviesBooking.Show', null=False, blank=False,
        related_name='tickets_user',
        on_delete=models.CASCADE
    )

    show_seats = models.ManyToManyField(
        'moviesBooking.ShowSeats',
        null=True, blank=True,
        related_name='city_theatre',

    )

    ticket_status = models.CharField(
        choices=TicketStatus.choices,
        null=True, blank=True,
        max_length=255
    )

    class Meta:
        db_table = "tickets_table"


