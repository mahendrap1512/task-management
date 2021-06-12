from django.db import models
from common.base_model import BaseModel
from project.models import Project


class Task(BaseModel):

    class TaskStatus(models.TextChoices):
        TODO = "TODO"
        WIP = "WIP"
        ONHOLD = "ONHOLD"
        DONE = "DONE"

    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=64, blank=True, null=True)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.TODO.value)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Task"
