from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at_utc = models.DateTimeField(editable=False, blank=False, null=False)
    modified_at_utc = models.DateTimeField(blank=False, null=False)
    is_deleted = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        abstract = True
