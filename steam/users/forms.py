from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
 
class RegistrForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='This field is required')
  

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', )