from django.views import View
from ..models import Project, Board, Task, Column
from django.shortcuts import render, redirect
from ..forms import ProjectForm
from django.contrib import messages

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