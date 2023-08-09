from django import forms  
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'startDate', 'endDate', 'assignee', 'project', 'description', 'priority', 'attach_file']

