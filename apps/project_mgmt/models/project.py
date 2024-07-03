from django.db import models
from utils.models import BaseModel
from apps.auth.models import UserModel


# Create your models here.

class Project(BaseModel, models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    