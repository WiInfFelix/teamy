from django.db import models
from teamy import settings

# Create your models here.
class Organisation(models.Model):
    name = models.CharField("Name", max_length=256)
    description = models.TextField("Description", max_length=1028)
    country = models.CharField("Country", max_length=128)
    city = models.CharField("City", max_length=128)
    founder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name
