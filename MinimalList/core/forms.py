from django import forms
# No futuro importarei as labels/projects/categorias das models
from django.utils.translation import gettext_lazy as _
from .models import Tasks


class NewTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = {'task_name'}
        labels = {
            'task_name': _('Nome da tarefa'),
        }
