from django.shortcuts import render
from django import forms
from Task_21_App.models import Users
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    age = forms.IntegerField()
    profession = forms.CharField(max_length=255)


def base(request):
    return render(request, 'base.html')


def main(request):
    if request.method == "GET":
        list_users = Users.objects.all()
        return render(request, 'main.html', {'list_users': list_users})


def detail(request, user_id):
    if request.method == "GET":
        user = Users.objects.filter(id=user_id).all()
        print(user)
        return render(request, 'detail.html', {'user': user})
    if request.method == 'POST':
        if request.POST['Имя']:
            print(request.POST['Имя'])
            user_up = Users.objects.filter(id=user_id).update(first_name=request.POST['Имя'])
            return redirect('main')
        elif request.POST['Id']:
            print(request.POST['Id'])
            user_up = Users.objects.filter(id=user_id).update(id=request.POST['Id'])
            return redirect('main')
        elif request.POST['Фамилия']:
            print(request.POST['Фамилия'])
            user_up = Users.objects.filter(id=user_id).update(last_name=request.POST['Фамилия'])
            return redirect('main')
        elif request.POST['Возраст']:
            print(request.POST['Возраст'])
            user_up = Users.objects.filter(id=user_id).update(age=request.POST['Возраст'])
            return redirect('main')
        elif request.POST['Профессия']:
            print(request.POST['Профессия'])
            user_up = Users.objects.filter(id=user_id).update(profession=request.POST['Профессия'])
            return redirect('main')


def delete(request):
    if request.method == 'GET':
        u_id = request.GET.get('id')
        delete_user = Users.objects.filter(id=u_id).delete()

        return redirect('main')
