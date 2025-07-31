from utils.base_model import BaseModel
from django.db import models


class Theatre(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=255)

    address = models.TextField()

    city = models.ForeignKey('moviesBooking.City', null=True, blank=True, related_name='theatre_city', on_delete=models.SET_NULL)

    auditorium = models.ManyToManyField(
        'moviesBooking.Auditorium',
        related_name='theatre_auditorium',
        null=True, blank=True
    )

    class Meta:
        db_table = "theatre_table"
