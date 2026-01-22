from django.db import models
from .base import TimeStampedModel


class ComplementaryProduct(TimeStampedModel):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    base_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
