from django.urls import path 
from . import views

urlpatterns = [
	path('index.html', views.home, name='home'),
	path('map/', views.map, name='map'),
	path('three-column.html', views.domain, name='domain'),
	path('contact.html', views.contact, name='contact'),
	path('contact_submit.html', views.contact_submit, name='contact_submit'),
	path('form', views.form, name='form'),
	path('list.html', views.list, name='list'),
]
