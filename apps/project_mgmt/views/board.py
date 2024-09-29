from django.views import View
from ..models import Project, Board, Task, Column
from django.shortcuts import render, redirect
from django.urls import reverse
from ..forms import CreateBoardForm, ColumnForm
from django.contrib import messages
from apps.auth.models import UserModel
from django.db.models import Prefetch
from ..choices import ColorChoices
from django.db import models
from django.db import transaction
from django.http import JsonResponse

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
        users = UserModel.objects.values('id', 'username')
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
    