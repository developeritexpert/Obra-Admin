from django.db import models
from .base import TimeStampedModel


class Material(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MaterialProduct(models.Model):
    material = models.ForeignKey(
        "Material",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("material", "product")