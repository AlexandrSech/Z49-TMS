from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django import forms

"""

    1. Дана форма с тремя текстовыми полями. 
    Вернуть пользователю максимальное по длине значение поля. 
    Пример: введены abc, abcdef, ab - пользователю вернется abcdef. 
    Для задания требуется создать новый репозиторий.
    2. Дана форма с одним полем - дата. 
    Если дата первое января - вывести сообщение: “С новым {номер года} годом”. 
    В ином случае, вывести дату в формате: год-месяц-день. 
    Выполнить задание в репозитории из первого задания"""
class BaseForm(forms.Form):
    input_1 = forms.CharField()
    input_2 = forms.CharField()
    input_3 = forms.CharField()


class DataForm(forms.Form):
    current_data = forms.DateField()


def base(request):
    return render(request, 'base.html')


def task_19_1(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        form = BaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            max_i = ""
            for i in data.values():
                if len(max_i) < len(i):
                    max_i = i
            return render(request, 'index2.html', {'max_i': max_i})
        else:
            return render(request, 'index.html')


def task_19_2(request):
    if request.method == "GET":

        return render(request, 'task_19_2.html')

    elif request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data
            print(date)

            print(date.get('current_data'))
            d = date.get('current_data').day
            m = date.get('current_data').month
            y = date.get('current_data').year
            print('{}:{}:{}'.format(d, m, y))

            return render(request, 'task_19_2_2.html', {'d': d, 'm': m, 'y': y})

        return render(request, 'task_19_2.html')

    # Create your views here.
