from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task, STATUS, User, TASK_TYPE


class TaskForm(forms.ModelForm):
    """
    Create new task object
    """
    wbs_code = forms.CharField(
        label='WBS код',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    task_type = forms.ChoiceField(
        choices=TASK_TYPE,
        label='Тип',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    description = forms.CharField(
        label='Описание',
        required=False, widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3}
        )
    )
    start_date = forms.DateField(
        label='Дата начала',
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        ), required=False
    )
    duration = forms.DurationField(
        label='Продолжительность',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ), required=False
    )
    end_date = forms.DateField(
        label='Дата завершения',
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        ), required=False
    )
    responsible = forms.CharField(
        label='Исполнитель',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    status = forms.ChoiceField(
        choices=STATUS,
        label='Статус',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    project = forms.ModelChoiceField(
        label='Проект',
        queryset=Project.objects.all(), required=False, widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Task
        fields = [
            'wbs_code',
            'task_type',
            'name',
            'description',
            'start_date',
            'duration',
            'end_date',
            'responsible',
            'status',
            'project',
        ]


class TaskCreate(CreateView):
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = '/mytasks/'


class TaskUpdate(UpdateView):
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = '/mytasks/'
    queryset = Task.objects.all()


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/mytasks/'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'job',
            'phone',
            'email',
            'project_role',
            'occupation',
            'other',
            'project'
        ]


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'hr.html'
    success_url = '/'


class TaskRelation(forms.ModelForm):
    """
    Create new task object
    """
    predecessors = forms.ModelChoiceField(
        queryset=Task.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label='Предыдущая задача')

    class Meta:
        model = Task
        fields = [
            'predecessors',
        ]

