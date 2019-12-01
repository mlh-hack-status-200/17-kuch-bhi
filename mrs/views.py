from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from .forms import MedForm,nameForm
from mrs.models import Med
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = nameForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			data = Med.objects.get(name=obj.name)
			return redirect('list.html', name=data.name)
	else:
		form = nameForm()
		return render(request, 'mrs/index.html', {'form':form})

def map(request):
	return render(request, 'mrs/map.html', {})

def domain(request):
	return render(request, 'mrs/three-column.html', {})

def contact(request):
	return render(request, 'mrs/contact.html', {})

def contact_submit(request):
	return render(request, 'mrs/contact_submit.html', {})

def form(request):
	if request.method == 'POST':
		form = MedForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('index.html')
	else:
		form = MedForm()
		return render(request, 'mrs/form.html', {'form':form})

def list(request,name):
	data = Med.objects.get(name=name)
	return render(request, 'mrs/list.html', {'data':data})










