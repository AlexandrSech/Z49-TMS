from django.shortcuts import render, redirect
from authentication.forms import LoginForm, MessageForm
from authentication.models import MyUser, Messages
from django.http import JsonResponse
from .serializers import MessagesSerializer


def index(request, user_id=None):
    # request.GET.get('user_id', None)
    if request.method == 'GET':
        # print(user_id)
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
                    request.session['last_load_message_id'] = -1
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
            chl = {'login': data.get('user_name', ''), 'password': data.get('password', '')}
            print(chl)
            if chl['login'] and chl['password']:
                new_user = MyUser(**chl)
                print(new_user.save())
                print(new_user.id, new_user.login)
                if new_user:
                    return redirect('index')

        return render(request, 'authentication/registration.html')


def get_messages(request):
    messages = Messages.objects.all()
    serializer = MessagesSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)


def message(request):
    if request.method == 'GET':
        print('last_load_message_id: ', request.session.get('last_load_message_id', -1))

        m_list = Messages.objects.filter(id__gt=request.session.get('last_load_message_id', -1))

        for i in m_list:
            print(i.user_name, i.text)



        print("m_list", m_list)
        if len(m_list):
            request.session['last_load_message_id'] = m_list[len(m_list) - 1].id
        print('last_load_message_id: ', request.session.get('last_load_message_id', -1))
        return render(request, 'authentication/main.html',
                      {'user_name': str(request.session.get('user_name', 'no user')), 'm_list': m_list, 'first_user_name': m_list[0].user_name})
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



