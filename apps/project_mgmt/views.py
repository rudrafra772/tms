from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ProjectForm, CreateBoardForm, ColumnForm, AddTaskForm
from django.contrib import messages
from .models import Project, Board, Task, Column
from .choices import ColorChoices
from django.db import transaction
from django.http import JsonResponse
from django.db import models
from apps.auth.models import UserModel
from django.db.models import Prefetch
# Create your views here.


class KanbanBordView(View):
    def get(self, request):
        return render(request, 'project_mgmt/kanban.html')
    

class ProjectView(View):
    def get(self, request):
        projects_list = Project.objects.select_related('created_by').values('id', 'name', 'description', 'created_by__username', 'created_at')
        context = {
            'project_list': projects_list
        }
        return render(request, 'project_mgmt/projects.html', context)
    
class AddProject(View):
    def get(self, request):
        form = ProjectForm()
        context = {
            'header':"Create Project",
            'form': form
        }
        return render(request, 'project_mgmt/project_form.html', context)
    
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project created successfully.")
            return redirect('projects')
        else:
            message = form.errors.as_text()
            messages.error(request, f"Error in creating project. {message}")
        return redirect('add_project')
    

class EditProject(View):
    def get(self, request, id):
        project = Project.objects.get(id = id)
        form = ProjectForm(instance=project)
        context = {
            'header':"Edit Project",
            'form': form
        }
        return render(request, 'project_mgmt/project_form.html', context)
    
    def post(self, request, id):
        project = Project.objects.get(id = id)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully.")
            return redirect('projects')
        else:
            messages.error(request, "Error in updating project.")
        return redirect('edit_project')


class DeleteProject(View):
    def post(self,request, id):
        try:
            project = Project.objects.get(id = id)
            project.delete()
            messages.success(request, "Project has been deleted successfully.")
            return redirect('projects')
        except Exception as e:
            messages.error(request, f"{e}")


######################################################################################
#Kanban board (Main)
######################################################################################

class BoardView(View):
    def get(self, request):
        board_list = Board.objects.values('id', 'name', 'created_by__username','created_at').prefetch_related('created_by')
        context = {
            'board_list': board_list
        }
        return render(request, 'project_mgmt/board.html', context)

class AddBoardView(View):
    def get(self, request):
        form = CreateBoardForm()
        project_list = Project.objects.values('id', 'name')
        context = {
            'form': form,
            'project_list':project_list,
            'header':"Create Board"
        }
        return render(request, 'project_mgmt/board_form.html', context)

    def post(self, request):
        form = CreateBoardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Board created successfully.')
            return redirect('board')
        messages.error(request, 'Error in creating Board.')
        return redirect('add_board')
    
class EditBoardView(View):
    def get(self, request, id):
        board = Board.objects.get(id = id)
        project_list = Project.objects.values('id','name')
        form = CreateBoardForm(instance= board)
        context = {
            'form': form,
            'project_list':project_list,
            'header':"Edit Board"
        }
        return render(request, 'project_mgmt/board_form.html', context)
    
    def post(self, request, id):
        board = Board.objects.get(id = id)
        form = CreateBoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            messages.success(request, 'Board updated successfully.')
            return redirect('board')
        messages.error(request, 'Error in updating Board.')
        return redirect('add_board')

class DeleteBoardView(View):
    def post(self, request, id):
        board = Board.objects.get(id = id)
        board.delete()
        messages.success(request, 'Board deleted successfully.')
        return redirect('board')
    
######################################################################################
#Kanban board (Sub)
######################################################################################

class KanBanBoardView(View):
    def get(self, request, board_id):
        board = Board.objects.get(id = board_id)
        tasks_prefetch = Prefetch(
            'tasks',
            queryset=Task.objects.order_by('order')  # Adjust 'order' to the appropriate field for task ordering
        )
        board_columns = Column.objects.filter(board = board).prefetch_related(tasks_prefetch).order_by('order')
        users = UserModel.objects.values('id')
        context = {
            'board':board,
            'board_columns':board_columns,
            'users': users
        }
        return render(request, 'project_mgmt/kanban.html', context)
    
######################################################################################
#Kanban board  Columns
######################################################################################
class ColumnView(View):
    def get(self, request, board_id):
        column_list = Column.objects.filter(board_id = board_id).order_by('order')
        context = {
            'column_list':column_list,
            'board_id':board_id
        }
        return render(request, 'project_mgmt/column.html', context)
    
class AddColumnView(View):
    def get(self, request, board_id):
        form = ColumnForm()
        color_choices = ColorChoices.choices
        context = {
            'board_id':board_id,
            'form':form,
            'header':"Create Column",
            'color_choices':color_choices
        }
        return render(request, 'project_mgmt/column_form.html', context)
    
    def post(self, request, board_id):
        form = ColumnForm(request.POST)
        board = Board.objects.get(id = board_id)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.board = board
            form_data.order = 0
            form_data.save()
            Column.objects.filter(order__gte=0).exclude(id=form_data.id).update(order=models.F('order') + 1)
            messages.success(request, 'Column Created successfully')
            return redirect('column', board_id)
        messages.error(request, 'Error in creating column')
        return redirect('add_column', board_id)
    
class UpdateColumnOrder(View):
    @transaction.atomic
    def post(self, request):
        column_ids = request.POST.getlist('column_ids[]')
        board_id = request.POST.get('board_id')
        for index , column_id in enumerate(column_ids):
            column = Column.objects.get(pk=column_id)
            column.order = index
            column.save()
        return JsonResponse({'success': True, 'redirect_url': reverse('column',  kwargs={'board_id': board_id})})
    
class EditColumn(View):
    def get(self, request, board_id, id):
        column = Column.objects.get(id = id)
        form  = ColumnForm(instance=column)
        color_choices = ColorChoices.choices
        context = {
            'board_id':board_id,
            'form':form,
            'header':"Edit Column",
            'color_choices':color_choices
        }
        return render(request, 'project_mgmt/column_form.html', context)
    
    def post(self, request, board_id, id):
        column = Column.objects.get(id = id)
        form = ColumnForm(request.POST, instance= column)
        if form.is_valid():
            form.save()
            messages.success(request, 'Column updated successfully.')
            return redirect('column', board_id)
        messages.error(request, 'Error in updating column.')
        return redirect('edit_column', board_id, id)
    
class DeleteColumn(View):
    def post(self, request, board_id, id):
        column = Column.objects.get(id = id)
        column.delete()
        messages.success(request, "Column deleted successfully.")
        return redirect('column', board_id)
    

######################################################################################
#Kanban board (Drapable) 
######################################################################################

class KanbanAddTask(View):
    def post(self, request, column_id):
        column = Column.objects.get(id = column_id)
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.column = column
            task.order = 0
            task.save()
            Task.objects.filter(order__gte=0, column = column).exclude(id=task.id).update(order=models.F('order') + 1)
            messages.success(request, "Task Added Successfully.")
        else:
            error_messages = form.errors.as_text()
            messages.error(request, f"Error in adding task: {error_messages}")
        return redirect('kanban_board', column.board.id)
    from django.db.models import F

class UpdateTask(View):
    def post(self, request):
        task_id = request.POST.get('task_id')
        new_column_id = request.POST.get('new_column_id')
        new_order = int(request.POST.get('new_order'))

        try:
            task = Task.objects.get(id=task_id)
            new_column = Column.objects.get(id=new_column_id)
            old_order = task.order
            old_column = task.column

            # Moving within the same column
            if old_column == new_column:
                if old_order > new_order:
                    # Moving up: shift tasks between new_order and old_order down
                    Task.objects.filter(
                        column=new_column,
                        order__gte=new_order,
                        order__lt=old_order
                    ).update(order=models.F('order') + 1)
                elif old_order < new_order:
                    # Moving down: shift tasks between old_order and new_order up
                    Task.objects.filter(
                        column=new_column,
                        order__gt=old_order,
                        order__lte=new_order
                    ).update(order=models.F('order') - 1)

            # Moving to a different column
            else:
                # Adjust the order in the old column
                Task.objects.filter(
                    column=old_column,
                    order__gt=old_order
                ).update(order=models.F('order') - 1)

                # Shift tasks in the new column
                Task.objects.filter(
                    column=new_column,
                    order__gte=new_order
                ).update(order=models.F('order') + 1)

            # Update the task's column and order
            task.column = new_column
            task.order = new_order
            task.save()

        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)
        except Column.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Column not found'}, status=404)

        return JsonResponse({'success': True})

