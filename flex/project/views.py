from .models import Project, Task, User, TaskRel
from .forms import UserForm, TaskRelation
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from requests import request
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.detail import DetailView


# Create your views here.

class Home(TemplateView):
    """
    Displaying active projects and tasks on home page
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
            context = super(Home, self).get_context_data(**kwargs)
            context.update({
                'tasks': Task.objects.filter(status=2),
                'projects': Project.objects.filter(status=2),
            })
            return context


class MyTaskList(TemplateView):
    """
    Displaying task list on task list page
    """
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
            context = super(MyTaskList, self).get_context_data(**kwargs)
            context.update({
                'tasks': Task.objects.all(),
                'tasksrel': TaskRel.objects.all(),
            })
            return context


class MyProjectList(ListView):
    """
    Displaying project list on project list page
    """
    template_name = 'project_list.html'
    model = Project

    def get_queryset(self):
        return Project.objects.all()


class HR(ListView):
    template_name = 'hr.html'
    model = User


def hr(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('hr_all')
        else:
            form = UserForm()
    # projects = Project.objects.all()
    return render(request, 'hr.html', {'form':form})
    # return render(request, 'hr.html', {'projects':projects})


def hr_all(request):
    users = User.objects.all()
    return render(request, 'hr_all.html', {'users': users})

# class HrList(ListView):
#     template_name ='hr_all.html'
#     model=User
#
#     def get_queryset(self):
#         return User.objects.all()

      
class ProjectDashboard(TemplateView):
    """
    Display project dashboard
    """
    template_name = 'project_dashboard.html'
    # model = Project

    def get_context_data(self, pk, **kwargs):
        context = super(ProjectDashboard, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(project_id=pk),
            'project': Project.objects.filter(pk=pk),
            'tasksrel': TaskRel.objects.all(),
        })
        return context


def new_relation(request, pk):
    form = TaskRelation()
    error_message = ''
    if request.method == 'POST':
        if pk != request.POST['predecessors']:
            task, created = TaskRel.objects.get_or_create(successor_id=pk, predecessors_id=request.POST['predecessors'])
            if not created:
                error_message = ('Такая связь уже существует',)
            else:
                return redirect('/mytasks')
        else:
            error_message = ('Нельзя связывать задачу с самой собой', )
    return render(request, 'create_rel.html', {'form': form, 'messages': error_message})


def upd_relation(request, pk):
    form = TaskRelation()
    rel = TaskRel.objects.get(pk=pk)
    error_message = ''
    if request.method == 'POST':
        if int(rel.successor_id) == int(request.POST['predecessors']):
            error_message = ('Нельзя связывать задачу с самой собой', )
        elif TaskRel.objects.filter(
                predecessors_id=request.POST['predecessors'], successor_id=rel.successor_id).exists():
            error_message = ('Такая связь уже существует', )
        else:
            rel.predecessors_id = request.POST['predecessors']
            rel.save()
            return redirect('/mytasks')
    form = TaskRelation(initial={'predecessors': rel.predecessors})
    return render(request, 'edit_rel.html', {'form': form, 'rel': pk, 'messages': error_message})


def del_relation(request, pk):
    form = None
    rel = TaskRel.objects.get(pk=pk)
    if request.method == 'POST':
        rel.delete()
        return redirect('/mytasks')
    else:
        return render(request, 'delete_rel.html', {'form': form, 'rel': rel})
