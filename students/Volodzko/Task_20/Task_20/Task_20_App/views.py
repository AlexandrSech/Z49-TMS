from django.shortcuts import render
from django import forms


class Order(forms.Form):
    first_name = forms.CharField()
    where_from = forms.CharField()
    where = forms.CharField()
    count_people = forms.IntegerField()
    data_fly = forms.DateField()


def base(request):
    return render(request, "base.html")


def order(request):
    if request.method == "GET":
        return render(request, 'order_auto.html')
    elif request.method == "POST":
        form = Order(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            count_people = data.get('count_people')
            if count_people == 1:
                price = 100
            else:
                price = 100 * 2 * count_people
            return render(request, "index.html", {"price": price})
        else:
            return render(request, 'order_auto.html')
    else:
        return render(request, 'base.html')

# Create your views here.
