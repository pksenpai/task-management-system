from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']
        # fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
            'placeholder': 'Username',
            'required': '',
        })
        self.fields['password1'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'id': 'password1',
            'name': 'password1',
            'placeholder': 'set-password',
            'required': '',
        })
        self.fields['password2'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'id': 'password2',
            'name': 'password2',
            'placeholder': 'check-password',
            'required': '',
        })
        self.fields['first_name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'first_name',
            'name': 'first_name',
        })
        self.fields['last_name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'last_name',
            'name': 'last_name',
        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'id': 'email',
            'name': 'email',
            'placeholder': 'you@example.com',
            'required': '',
        })
        
        """\________________________Input-Attrs________________________/"""

        # username --> type="text" class="form-control" id="username" placeholder="Username" name="username" required
        # password1 --> type="password" class="form-control" id="password1" placeholder="set-password" name="password1" required=""
        # password2 --> type="password" class="form-control" id="password2" placeholder="check-password" name="password2" required=""
        
        # first_name --> type="text" class="form-control" id="firstName" name="firstname"
        # last_name --> type="text" class="form-control" id="lastName" name="lastname" placeholder="" value="" required=""
        # email --> type="email" class="form-control" id="email" name="email" placeholder="you@example.com"
    
class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password',]
        # fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
            'placeholder': 'Username',
            'required': '',
            'data-key': 'jafar',
        })
        
        self.fields['password'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'id': 'password',
            'name': 'password',
            'placeholder': 'Password',
            'required': '',
            'data-key': 'jafar',
        })
        
        # self.fields["password"].widget.attrs['class'] = 'form-control'
        
        # self.fields['email'].widget.attrs.update({
        #     'type': 'email',
        #     'class': 'form-control',
        #     'id': 'email',
        #     'name': 'email',
        #     'placeholder': 'you@example.com',
        #     'required': ''
        # })
        
        """\________________________Input-Attrs________________________/"""

        # username --> type="text" class="form-control" id="username" placeholder="Username" name="username" required
        # password1 --> type="password" class="form-control" id="password" placeholder="Password" name="password" required=""
        # email --> type="email" class="form-control" id="email" name="email" placeholder="you@example.com"
    