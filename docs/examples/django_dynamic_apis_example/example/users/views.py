from django.shortcuts import render
from users.models import Users, Profile

# Create your views here.


def users_list(request):
    current_users_list = Users.objects.all()
    return render(request, 'users_list.html', {'users_list': current_users_list})


def profile(request, user_id=None):
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

