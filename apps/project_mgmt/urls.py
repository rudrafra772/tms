from django.urls import path
from .views import KanbanBordView
urlpatterns = [
    path('kanban-board/', KanbanBordView.as_view(), name='kanban_board')
]
