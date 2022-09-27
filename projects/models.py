from django.db import models

from teamy import settings


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2096)
    creator = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, related_name="creator")
    initiator = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, related_name="initiator")

    organisation = models.ForeignKey(
        "organisations.Organisation", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
