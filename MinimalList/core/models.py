from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.taskAdd

    taskAdd = models.TextField(max_length=100)


class Projects(models.Model):
    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.projectAdd

    projectAdd = models.CharField(max_length=30)
