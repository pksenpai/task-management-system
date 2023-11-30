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
            'color',
            'hide',
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
        self.fields['color'].widget.attrs.update({
            'class': 'd-block me-auto'
        })
        self.fields['hide'].widget.attrs.update({
            'class': 'd-block me-auto'
        })

class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'color',
            'edit_task_permission',
            'functor_task_permission',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
              
        initial_due_date = None
        if 'instance' in kwargs and kwargs['instance']:
            initial_due_date = kwargs['instance'].due_date
          
        self.fields['title'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control disable',
            'id': 'title',
            'name': 'title',
            'placeholder': 'Title...',
        })
        self.fields['description'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'description',
            'name': 'description',
            'placeholder': 'Description...',
        })
        self.fields['color'].widget.attrs.update({
            'class': 'd-block me-auto'
        })
        self.fields['edit_task_permission'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control text-danger',
            'id': 'edit_task_permission',
            'name': 'edit_task_permission',
        })
        self.fields['functor_task_permission'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control text-primary',
            'id': 'functor_task_permission',
            'name': 'functor_task_permission',
        })

        
class StatusCheckForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['status']
        
        