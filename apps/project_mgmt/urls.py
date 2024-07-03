from django.urls import path
from .views import (
    KanbanBordView,
    ProjectView, 
    AddProject, 
    EditProject,
    DeleteProject,
)
urlpatterns = [
    path('kanban-board/', KanbanBordView.as_view(), name='kanban_board'),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("add-project/", AddProject.as_view(), name="add_project"),
    path("edit-project/<int:id>/", EditProject.as_view(), name="edit_project"),
    path('delete-project/<int:id>/', DeleteProject.as_view(), name="delete_project")
]
