from django.db import models
from django.contrib.auth.models import User
from common.base_model import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="projects")
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=True, default=None)

    class Meta:
        db_table = "Project"
        indexes = [
            models.Index(fields=["created_at_utc"]),
            models.Index(fields=["name"])
        ]
