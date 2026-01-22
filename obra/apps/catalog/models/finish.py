from django.db import models
from .base import TimeStampedModel


class Finish(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class FinishProduct(models.Model):
    finish = models.ForeignKey(
        "Finish",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("finish", "product")


class FinishVariant(models.Model):
    finish = models.ForeignKey(
        "Finish",
        on_delete=models.CASCADE
    )
    variant = models.ForeignKey(
        "catalog.Variant",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("finish", "variant")
