from utils.base_model import BaseModel
from django.db import models


class Auditorium(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=255)

    capacity = models.IntegerField(null=False, blank=False)

    theatre = models.ForeignKey(
        'moviesBooking.Theatre',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='auditorium_theatre'
    )
    seats = models.ManyToManyField(
        'moviesBooking.Seats', null=True, blank=True,
        related_name='auditorium_seats'
    )

    show = models.ManyToManyField(
        'moviesBooking.Show', null=True, blank=True,
        related_name='auditorium_show'
    )

    class Meta:
        db_table = "auditorium_table"
