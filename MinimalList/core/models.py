from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    class Meta:
        verbose_name_plural = "Tasks"

    task_name = models.TextField(max_length=100)
    def __str__(self):
        return self.task_name

    