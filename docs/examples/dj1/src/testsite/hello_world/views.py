from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .templates import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Users


class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField()


def index(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.__dict__)
            data = form.cleaned_data
            print(data)
            user = Users.objects.filter(login=data.get('user_name')).first()
            print(user)
            if user:
                if user.password == data.get('password'):
                    rp = render_to_string('main.html', {'user_name': user.login})
                    return render(request, 'main.html', {'user_name': user.login})

        return render(request, 'login.html')


def base(request):
    rp = render_to_string('base.html', {'co': 'some text'})
    return render(request, rp)


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.__dict__)
            data = form.cleaned_data
            print(data)
            # l_id = Users.objects.filter('-id').first().id
            new_user = Users.objects.create(id=3,
                                            login='qwe', # data.get('user_name'),
                                            password='asd', # data.get('password'))
            # new_user.save()
            print(new_user)
            if new_user:
                return render(request, 'index.html')

        return render(request, 'registration.html')

