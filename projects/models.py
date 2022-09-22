from django.db import models
from teamy import settings

# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2096)

    organisation = models.ForeignKey(
        "organisations.Organisation", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
