from django.db import models
from .project import Project
from apps.auth.models import UserModel
from utils.models import BaseModel
from apps.project_mgmt.choices import ColorChoices
from tinymce.models import HTMLField

class Board(BaseModel, models.Model):
    project = models.ForeignKey(Project, related_name='boards', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Column(BaseModel, models.Model):
    board = models.ForeignKey(Board, related_name='columns', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    color = models.CharField(choices=ColorChoices.choices, max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Task(BaseModel, models.Model):
    column = models.ForeignKey(Column, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = HTMLField(blank=True, null=True)
    order = models.PositiveIntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title