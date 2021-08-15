from django.shortcuts import render, redirect
from users.models import Users, Profile
from django.contrib.auth import authenticate, login
import json
from django.http import HttpResponse

# Create your views here.


def get_token(request):
    return HttpResponse(json.dumps({'token': 'asddlkvchbawjdcbwelBCJALWECINAW'}))


def get_list(request):
    my_list = [i for i in range(0, 1000, 4)]
    return HttpResponse(json.dumps({'rows': my_list, 'text': 'цой жив'}))


def my_login(request):
    user = authenticate(username='john', password='root')
    if user is not None:
        login(request, user)
        return redirect('users_list')
    return redirect('login')


def users_list(request):
    # user = request.session.get('user', '')
    print(request.user.is_authenticated)
    print(request.user)
    print(request.user.groups)
    groups = ['admin', ]
    if request.user.is_authenticated:
        if request.user.groups in groups:
            current_profile = Profile.objects.filter(user_id=1)
            return render(request, 'profile.html', {'profile': current_profile})
    current_users_list = Users.objects.all()
    return render(request, 'users_list.html', {'users_list': current_users_list})


def profile(request, user_id=None):
    current_profile = Profile.objects.filter(user_id=1)
    return render(request, 'profile.html', {'profile': current_profile})
    print(user_id)
    current_profile = Profile.objects.filter(user_id=user_id)

    return render(request, 'profile.html', {'profile': current_profile})



    # print(user_id)

    '''user_name_template = {'login': 'User{}', 'password': '123',
                          'user_id': '', 'first_name': 'F_name{}', 'last_name': 'L_name{}',
                          'email': 'some_email_of_user{}@example.com',
                          'age': '{}'}

    profile_template = {'user_id': '', 'first_name': 'F_name{}', 'last_name': 'L_name{}',
                          'email': 'some_email_of_user{}@example.com',
                          'age': '{}'}
    for i in range(1, 11):
        new_user = Users(login=user_name_template['login'].format(i), password=user_name_template['password'])
        new_user.save()

        profile_for_new_user = Profile(
            user_id=i,
            first_name=profile_template['first_name'].format(i),
            last_name=profile_template['last_name'].format(i),
            email=profile_template['email'].format(i),
            age=profile_template['age'].format(i)
        )

        profile_for_new_user.save()'''

