from django.shortcuts import render, redirect
from authentication.forms import LoginForm, MessageForm
from authentication.models import MyUser, Messages
from django.http import JsonResponse
from .serializers import MessagesSerializer


def index(request):
    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.__dict__)
            data = form.cleaned_data
            print(data)
            user = MyUser.objects.filter(login=data.get('user_name')).first()
            print(user)
            if user:
                if user.password == data.get('password'):
                    request.session['user_name'] = user.login
                    return redirect('message')

        return render(request, 'authentication/login.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'authentication/registration.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.__dict__)
            data = form.cleaned_data
            print(data)
            # l_id = Users.objects.filter('-id').first().id
            new_user = MyUser.objects.create(# id=5,
                                             login=data.get('user_name'),
                                             password=data.get('password'))
            # new_user.save()
            print(new_user)
            if new_user:
                return render(request, 'authentication/index.html')

        return render(request, 'authentication/registration.html')


def get_messages(request):
    messages = Messages.objects.all()
    serializer = MessagesSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)


def message(request):
    if request.method == 'GET':
        m_list = Messages.objects.all()
        print("m_list", m_list)
        return render(request, 'authentication/main.html',
                      {'user_name': str(request.session.get('user_name', 'no user')), 'm_list': m_list})
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print(form.__dict__)
            data = form.cleaned_data
            print(data)

            new_mess = Messages.objects.create(user_name=data.get('user_name'),
                                               text=data.get('m_text'))
            print(new_mess)
        return redirect('message')



