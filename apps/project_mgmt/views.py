from django.shortcuts import render, redirect
from django.views import View
from .forms import ProjectForm
from django.contrib import messages
from .models import Project

# Create your views here.


class KanbanBordView(View):
    def get(self, request):
        return render(request, 'project_mgmt/kanban.html')
    

class ProjectView(View):
    def get(self, request):
        projects_list = Project.objects.all()
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
        print(form, '****')
        if form.is_valid():
            project = form.save(commit=False)
            project.user = self.request.user
            project.save()
            messages.success(request, "Project created successfully")
            return redirect('projects')
        else:
            messages.error(request, "Error in creating project")
        return redirect('add_project')