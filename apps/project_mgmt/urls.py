from django.urls import path
from .views import (
    KanbanBordView,
    ProjectView, 
    AddProject
)
urlpatterns = [
    path('kanban-board/', KanbanBordView.as_view(), name='kanban_board'),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("add-project/", AddProject.as_view(), name="add_project")
]
