from django.views import View
from ..models import Task, Column
from ..forms import AddTaskForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import models
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

class KanbanBordView(View):
    def get(self, request):
        return render(request, 'project_mgmt/kanban.html')
    
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

class EditTaskView(View):
    def post(self, request, id):
        task  = Task.objects.get(id = id)
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully.")
        else:
            error_messages = form.errors.as_text()
            messages.error(request, f"Error in adding task: {error_messages}")
        return redirect('kanban_board', task.column.board.id)


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

class DeleteTask(View):
    def post(self, request, id):
        task = Task.objects.get(id = id)
        board_id = task.column.board.id
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('kanban_board', board_id)

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)