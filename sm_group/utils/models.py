from django.db import models
from django.utils import timezone
import uuid

class BaseModel(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
