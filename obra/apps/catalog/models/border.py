from django.db import models
from .base import TimeStampedModel


class Border(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BorderProduct(models.Model):
    border = models.ForeignKey(
        "Border",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("border", "product")