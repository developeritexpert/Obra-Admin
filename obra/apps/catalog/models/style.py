from django.db import models
from .base import TimeStampedModel


class Style(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class StyleProduct(models.Model):
    style = models.ForeignKey(
        "Style",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("style", "product")


class StyleVariant(models.Model):
    style = models.ForeignKey(
        "Style",
        on_delete=models.CASCADE
    )
    variant = models.ForeignKey(
        "catalog.Variant",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("style", "variant")
