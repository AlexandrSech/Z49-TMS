from django.shortcuts import render, redirect
from .forms import RegistrForm
 
def register(request):
	if request.method == "POST":
		form = RegistrForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegistrForm()
	return render(request, 'users/register.html', {'form': form})