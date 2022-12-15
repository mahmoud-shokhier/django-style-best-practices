from django.core.exceptions import ValidationError

from django.db import models
from utils.models import BaseModel
from sm_group.apps.users.models import User


# Create your models here.
class CompanyType(models.IntegerChoices):
    POINTS = 1, "Points"
    DURATION = 2, "Duration"

 
class Company(BaseModel):
    name = models.CharField(unique=True, max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.IntegerField(choices=CompanyType.choices)
    value_points = models.IntegerField(null=True)
    value_duration = models.DurationField(null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_unique_value_matches_type",
                check=(
                    models.Q(
                        type=CompanyType.POINTS,
                        value_points__isnull=False,
                        value_duration__isnull=True,
                    )
                    | models.Q(
                        type=CompanyType.DURATION,
                        value_points__isnull=True,
                        value_duration__isnull=False,
                    )
                ),
            )
        ]

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("End date cannot be before start date")
