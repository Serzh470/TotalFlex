from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import Project, Task, STATUS, User, TASK_TYPE, ROLE
from django.forms.widgets import TextInput
import datetime


class DurationInput(TextInput):
    """
    Custom widget for duration field, show duration in days '%dд' format in form
    """
    def format_value(self, value):
        if isinstance(value, datetime.timedelta):
            return '{}д'.format(value.days)
        else:
            return 'д'


class DurationDayFiled(forms.CharField):
    """
    Custom input field for input in days. Saves number in form in days in timedelta (with or without 'д').
    """
    def to_python(self, value):

        if 'д' in value:
            value = int(value.replace('д', ''))
            value = datetime.timedelta(days=value)
        else:
            days_number = int(value)
            value = datetime.timedelta(days=days_number)
        return super().to_python(value)


class TaskForm(forms.ModelForm):
    """
    Create new task object for with many settings for each field
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
        required=False, 
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3}
        )
    )
    start_date = forms.DateField(
        label='Дата начала',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        )
    )    
    duration = DurationDayFiled(
        required=False,
        label='Продолжительность',
        widget=DurationInput(
            attrs={'class': 'form-control'}
        )
    )
    end_date = forms.DateField(
        label='Дата завершения',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'datepicker form-control'}
        )
    )
    responsible = forms.ModelChoiceField(
        label='Исполнитель',
        queryset=User.objects.all(),
        required=False,
        widget=forms.Select(
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
    percent_complete = forms.IntegerField(
        label='% выполнения',
        required=False,
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'type': 'number'}
        )
    )
    project = forms.ModelChoiceField(
        label='Проект',
        queryset=Project.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    optimistic_price = forms.FloatField(
        label='Оптимистичная стоимость',
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'type': 'number'}
        )
    )
    realistic_price = forms.FloatField(
        label='Реалистичная стоимость',
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'type': 'number'}
        )
    )
    pessimistic_price = forms.FloatField(
        label='Пессимистичная стоимость',
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'type': 'number'}
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
            'percent_complete',
            'project',
            'optimistic_price',
            'realistic_price',
            'pessimistic_price'
        ]


class UserForm(forms.ModelForm):
    """
    Form for creating and editing users info.
    """
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    job = forms.CharField(
        label='Должность',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.CharField(
        label='E-mail',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    project_role = forms.ChoiceField(
        label='Роль в проекте',
        choices=ROLE,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    occupation = forms.CharField(
        label='% занятости',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    other = forms.CharField(
        label='Комментарии',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'job',
            'phone',
            'email',
            'project_role',
            'occupation',
            'other'
        ]


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =[
            'wbs_code',
            'name',
            'description',
            'responsible',
            'status',
            'optimistic_price',
            'pessimistic_price',
            'realistic_price',
        ]


class BudgetCalculate(CreateView):
    form_class = BudgetForm
    template_name = 'business_plan.html'
    success_url = ''


class TaskRelation(forms.ModelForm):
    """
    Display form for defining relation between tasks
    """
    predecessors = forms.ModelChoiceField(
        queryset=Task.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}), label='Предыдущая задача')

    class Meta:
        model = Task
        fields = [
            'predecessors',
        ]

