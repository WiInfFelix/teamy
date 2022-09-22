from django.db import models
from teamy import settings

# Create your models here.
class Task(models.Model):
    def get_task_creator(self):
        return self.creator

    short_summary = models.TextField(max_length=256)
    description = models.TextField(max_length=32000)

    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_task_created",
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_tasks_assigned",
    )
