from django.db import models

from utils.base_model import BaseModel


# Create your models here.
class City(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=255)

    theatre = models.ManyToManyField(
        'moviesBooking.Theatre',
        null=True, blank=True,
        related_name='city_theatre',

    )

    class Meta:
        db_table = "city_table"
