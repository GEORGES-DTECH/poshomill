from .models import Account
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms


class UserCreationForm(UserCreationForm):
   
    phone = forms.CharField(max_length=60,widget = forms.TextInput (attrs={'placeholder':'Valid phone for confirmation'}))
    username = forms.CharField(max_length=60,widget = forms.TextInput (attrs={'placeholder':'Enter your business name'}))
    password1 = forms.CharField(max_length=100,widget = forms.TextInput (attrs={'placeholder':'Enter a password you will remember'}))
    password2= forms.CharField(max_length=100,widget = forms.TextInput (attrs={'placeholder':'Enter the same password for confirmation'}))
    
    class Meta:
        model = Account
        fields = [
            'username',
            'phone',
            'select_country',
            'password1',
            'password2',
             'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','phone','select_country','password1', 'password2','email']:
          
           
            self.fields["email"].help_text= "email field is optional"

class UserEditForm(UserChangeForm):
   
   
    
    class Meta:
        model = Account
        fields = [
            'username',
            'phone',
            'select_country',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','phone','select_country','email']:
          
           
            self.fields[fieldname].help_text= None
          