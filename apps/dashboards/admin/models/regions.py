from django.db import models
from django.utils.text import slugify


class Region(models.Model):
    # Core info
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # Image
    image = models.ImageField(
        upload_to="regions/",
        blank=True,
        null=True
    )

    # Address
    zip_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)

    # Contact
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    # Location (human readable or map link)
    location = models.CharField(max_length=255, blank=True)

    # Status / metadata
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "regions"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
