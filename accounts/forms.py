from .models import Account
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms


class UserCreationForm(UserCreationForm):
   
 
    username = forms.CharField(max_length=60,widget = forms.TextInput (attrs={'placeholder':'Enter your username'}))
    password1 = forms.CharField(max_length=100,widget = forms.TextInput (attrs={'placeholder':'Enter a password you will remember'}))
    password2= forms.CharField(max_length=100,widget = forms.TextInput (attrs={'placeholder':'Enter the same password for confirmation'}))
    
    class Meta:
        model = Account
        fields = [
            'username',
            'password1',
            'password2',
             'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','password1', 'password2','email']:
          
           
            self.fields["email"].help_text= "Required incase you forget your password"

class UserEditForm(UserChangeForm):
   
   
    
    class Meta:
        model = Account
        fields = [
            'username',
            
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email']:
          
           
            self.fields[fieldname].help_text= None
          