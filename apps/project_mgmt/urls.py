from django.urls import path
from .views.kanban import (
    KanbanBordView, KanbanAddTask, UpdateTask, DeleteTask, upload_file
)
from .views.project import (
    ProjectView, AddProject, EditProject, DeleteProject
)
from .views.board import (
    BoardView, AddBoardView, EditBoardView, DeleteBoardView, KanBanBoardView, ColumnView, AddColumnView,
    UpdateColumnOrder, EditColumn, DeleteColumn
)
from .views.callender import (
    CalenderView, ChangeCalenderMonth
)

urlpatterns = [
    ######################################################################################
    #Project Urls
    ######################################################################################
    path("projects/", ProjectView.as_view(), name="projects"),
    path("add-project/", AddProject.as_view(), name="add_project"),
    path("edit-project/<int:id>/", EditProject.as_view(), name="edit_project"),
    path('delete-project/<int:id>/', DeleteProject.as_view(), name="delete_project"),

    ######################################################################################
    #Board Urls
    ######################################################################################
    path('board/', BoardView.as_view(), name="board"),
    path('boards/add/', AddBoardView.as_view(), name='add_board'),
    path('edit-board/<int:id>/', EditBoardView.as_view(), name='edit_board'),
    path('delete-board/<int:id>/', DeleteBoardView.as_view(), name="delete_board"),
    path('kanban-board/<int:board_id>/', KanBanBoardView.as_view(), name='kanban_board'),
    path('column/<int:board_id>/', ColumnView.as_view(), name="column"),
    path('add-column/<int:board_id>/', AddColumnView.as_view(), name="add_column"),
    path('update-column-order/', UpdateColumnOrder.as_view(), name="update_column_order"),
    path('edit-column/<int:board_id>/<int:id>/', EditColumn.as_view(), name="edit_column"),
    path('delete-column/<int:board_id>/<int:id>/', DeleteColumn.as_view(), name="delete_column"),

    ######################################################################################
    #Kanban Urls
    ######################################################################################
    path('kanban-board/', KanbanBordView.as_view(), name='kanban_board'),
    path('kanban-add-task/<int:column_id>', KanbanAddTask.as_view(), name="kanban_add_task"),
    path('update-task/', UpdateTask.as_view(), name='update_task'),
    path('delete-task/<int:id>/', DeleteTask.as_view(), name="delete_task"),
    path('upload/', upload_file, name='upload_file'),
    
    ######################################################################################
    #calender Urls
    ######################################################################################
    path('calender/', CalenderView.as_view(), name="calender"),
    path('calender/<str:date>/<str:next>/<str:prev>/', ChangeCalenderMonth.as_view(), name="change_month")
    

]
