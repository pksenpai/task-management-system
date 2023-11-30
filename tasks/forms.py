from django import forms
from workspaces.models import Workspace
from .models import Task

class AddNewTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        # exclude = ['status']
        # fields = '__all__'
        fields = [
            'title',
            'description',
            'due_date',
            'hide',
            'color',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
        self.fields['title'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'title',
            'name': 'title',
            'placeholder': 'Title...',
            'required': '',
        })
        self.fields['description'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'description',
            'name': 'description',
            'placeholder': 'Description...',
            'required': '',
        })
        self.fields['due_date'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['due_date'].widget = forms.widgets.DateTimeInput( #test it
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd',
                'class': 'form-control w-50'
            }
        )
        self.fields['hide'].widget.attrs.update({
            'class': 'd-block me-auto'
        })
        self.fields['color'].widget.attrs.update({
            'class': 'd-block me-auto'
        })


class StatusCheckForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['status']
        
        