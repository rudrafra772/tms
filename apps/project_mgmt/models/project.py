from django.db import models
from utils.models import CreatedUpdatedAt
from apps.auth.models import UserModel


# Create your models here.

class Project(CreatedUpdatedAt, models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name