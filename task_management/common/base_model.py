from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        abstract = True
