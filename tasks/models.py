from django.db import models

from teamy import settings


# Create your models here.
class Task(models.Model):
    def get_task_creator(self):
        return self.creator

    short_summary = models.TextField(max_length=256)
    description = models.TextField(max_length=32000)

    class TaskStatus(models.TextChoices):
        OPEN = "open"
        IN_PROGRESS = "in_progress"
        TEST = "test"
        REVIEW = "review"
        CLOSED = "closed"
        ABORTED = "aborted"

    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_task_creator",
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_tasks_assignee",
    )


class Comment(models.Model):

    title = models.CharField(max_length=256)
    text = models.TextField(max_length=32000)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_author",
    )

    task = models.ForeignKey(
        "tasks.Task", on_delete=models.CASCADE, related_name="task_comments"
    )


class Comment(models.Model):
    comment_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey("tasks.Task", on_delete=models.CASCADE)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.DO_NOTHING)
