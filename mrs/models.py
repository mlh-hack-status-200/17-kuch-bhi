from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Med(models.Model):
	def get_default_my_time():
  		return timezone.localtime(timezone.now())	
	
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	phone = models.CharField(max_length=12)
	user_name = models.CharField(max_length=300)
	date = models.DateTimeField(default = get_default_my_time)
	address = models.CharField(max_length = 1000, default = 'Ghaziabad - Meerut Highway, NH-58, Ghaziabad, Uttar Pradesh 201206, India')
	

