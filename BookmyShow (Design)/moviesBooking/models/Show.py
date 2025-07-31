from utils.base_model import BaseModel
from django.db import models


class Show(BaseModel):
    show_time = models.DateTimeField(auto_now=False)
    show_end_time = models.DateTimeField(auto_now=False)

    movie = models.ForeignKey(
        'moviesBooking.Movie', on_delete=models.CASCADE,
        related_name='movie_show'
    )

    auditorium = models.ForeignKey(
        'moviesBooking.Auditorium', on_delete=models.CASCADE,
        related_name='auditorium',
    )

    class Meta:
        db_table = "show_table"
