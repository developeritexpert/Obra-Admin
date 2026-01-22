from django.db import models
from .base import TimeStampedModel, StatusChoices, UnitTypeChoices


class Product(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    box_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    no_of_pieces_per_box = models.PositiveIntegerField(null=True, blank=True)

    thickness = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    width = models.DecimalField(max_digits=8, decimal_places=2)
    height = models.DecimalField(max_digits=8, decimal_places=2)
    length = models.DecimalField(max_digits=8, decimal_places=2)

    unit_type = models.CharField(max_length=10, choices=UnitTypeChoices.choices)
    in_stock = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices)

    diagram_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
