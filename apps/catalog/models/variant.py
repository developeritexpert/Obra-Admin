from django.db import models
from .base import TimeStampedModel, UnitTypeChoices


class Variant(TimeStampedModel):
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="variants"
    )

    sku = models.CharField(max_length=100, unique=True)
    variant_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    base_price = models.DecimalField(max_digits=12, decimal_places=2)

    thickness = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    width = models.DecimalField(max_digits=8, decimal_places=2)
    height = models.DecimalField(max_digits=8, decimal_places=2)
    length = models.DecimalField(max_digits=8, decimal_places=2)

    unit_type = models.CharField(max_length=10, choices=UnitTypeChoices.choices)
    in_stock = models.BooleanField(default=True)

    colors = models.JSONField(default=list)

    def __str__(self):
        return f"{self.product.title} - {self.variant_name}"
