from django.urls import path
from .views import (
    KanbanBordView, ProjectView, AddProject, EditProject,
    DeleteProject, BoardView, AddBoardView, EditBoardView,
    DeleteBoardView, KanBanBoardView, AddColumnView, ColumnView,
    UpdateColumnOrder, EditColumn, DeleteColumn, KanbanAddTask, UpdateTask, DeleteTask, upload_file, CalenderView, ChangeCalenderMonth
)
urlpatterns = [
    path('kanban-board/', KanbanBordView.as_view(), name='kanban_board'),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("add-project/", AddProject.as_view(), name="add_project"),
    path("edit-project/<int:id>/", EditProject.as_view(), name="edit_project"),
    path('delete-project/<int:id>/', DeleteProject.as_view(), name="delete_project"),
    path('board/', BoardView.as_view(), name="board"),
    path('boards/add/', AddBoardView.as_view(), name='add_board'),
    path('edit-board/<int:id>/', EditBoardView.as_view(), name='edit_board'),
    path('delete-board/<int:id>/', DeleteBoardView.as_view(), name="delete_board"),
    path('kanban-board/<int:board_id>/', KanBanBoardView.as_view(), name='kanban_board'),
    path('column/<int:board_id>/', ColumnView.as_view(), name="column"),
    path('update-column-order/', UpdateColumnOrder.as_view(), name="update_column_order"),
    path('add-column/<int:board_id>/', AddColumnView.as_view(), name="add_column"),
    path('edit-column/<int:board_id>/<int:id>/', EditColumn.as_view(), name="edit_column"),
    path('delete-column/<int:board_id>/<int:id>/', DeleteColumn.as_view(), name="delete_column"),
    path('kanban-add-task/<int:column_id>', KanbanAddTask.as_view(), name="kanban_add_task"),
    path('update-task/', UpdateTask.as_view(), name='update_task'),
    path('delete-task/<int:id>/', DeleteTask.as_view(), name="delete_task"),
    path('upload/', upload_file, name='upload_file'),
    path('calender/', CalenderView.as_view(), name="calender"),
    path('calender/<str:date>/', ChangeCalenderMonth.as_view(), name="change_month")
]
