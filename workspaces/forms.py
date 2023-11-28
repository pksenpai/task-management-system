from django import forms
from .models import Workspace


class AddNewWorkspaceForm(forms.ModelForm):

    class Meta:
        model = Workspace
        fields = [
            'name',
            'description',
            'public',
            'category',
            'tag',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'name',
            'name': 'name',
            'placeholder': 'Name...',
            'required': '',
        })
        self.fields['description'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'description',
            'name': 'description',
            'placeholder': 'Workspace about...',
            'required': '',
        })
        self.fields['category'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'category',
            'name': 'category',
        })
        self.fields['tag'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['public'].widget.attrs.update({
            'class': 'block me-auto'
        })


# class LoginForm(AuthenticationForm):

#     class Meta:
#         model = User
#         fields = ['username', 'password',]
#         # fields = '__all__'
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({
#             'type': 'text',
#             'class': 'form-control',
#             'id': 'username',
#             'name': 'username',
#             'placeholder': 'Username',
#             'required': '',
#             'data-key': 'jafar',
#         })
        
#         self.fields['password'].widget.attrs.update({
#             'type': 'password',
#             'class': 'form-control',
#             'id': 'password',
#             'name': 'password',
#             'placeholder': 'Password',
#             'required': '',
#             'data-key': 'jafar',
#         })

