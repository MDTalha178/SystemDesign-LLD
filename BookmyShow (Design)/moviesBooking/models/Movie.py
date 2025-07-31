from utils.base_model import BaseModel
from django.db import models


class Movie(BaseModel):
    movie_name = models.CharField(null=True, blank=True, max_length=255)
    movie_poster = models.CharField(null=True, blank=True, max_length=255)

    show = models.ManyToManyField(
        'moviesBooking.Show', null=True, blank=True,
        related_name='auditorium_seats'
    )

    class Meta:
        db_table = "movie_table"
