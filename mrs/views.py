from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from .forms import Medform
from mrs.models import Med
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
	return render(request, 'mrs/home.html', {})

def map(request):
	return render(request, 'mrs/map.html', {})










