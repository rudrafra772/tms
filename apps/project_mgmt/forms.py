from django import forms
from .models import Project, Board, Column, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']




class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'project']

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ['name', 'color']

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'user']