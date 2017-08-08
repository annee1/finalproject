from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	Username = models.ForeignKey(User, on_delete=models.CASCADE)
	contact_firstname = models.CharField(max_length=200)
	contact_lastname = models.CharField(max_length=100)
	contact_username = models.CharField(max_length=100)
	def __str__(self):
		return self.contact_firstname
		 

