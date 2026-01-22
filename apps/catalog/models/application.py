from django.db import models
from .base import TimeStampedModel


class Application(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ApplicationProduct(models.Model):
    application = models.ForeignKey(
        "Application",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("application", "product")