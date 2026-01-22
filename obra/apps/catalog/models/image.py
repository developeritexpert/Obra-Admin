from django.db import models
from .base import TimeStampedModel


class Image(TimeStampedModel):
    image_url = models.URLField()

    def __str__(self):
        return self.image_url


class ImageProduct(models.Model):
    image = models.ForeignKey(
        "Image",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )


class ImageVariant(models.Model):
    image = models.ForeignKey(
        "Image",
        on_delete=models.CASCADE
    )
    variant = models.ForeignKey(
        "catalog.Variant",
        on_delete=models.CASCADE
    )
