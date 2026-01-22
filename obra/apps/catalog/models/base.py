from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusChoices(models.TextChoices):
    ACTIVE = "active", "Active"
    DRAFT = "draft", "Draft"


class UnitTypeChoices(models.TextChoices):
    CM = "cm", "Centimeter"
    METER = "meter", "Meter"
