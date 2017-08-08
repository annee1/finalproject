from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=200)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	def __str__(self):
		return self.username
	def get_firstname(self):
		return self.firstname
	def get_lastname(self):
		return self.lastname 




class Friend(models.Model):
	friend = models.ForeignKey(User, on_delete=models.CASCADE)
	friendusername = models.CharField(max_length=200)
	friendfirstname = models.CharField(max_length=100)
	friendlastname = models.CharField(max_length=100)
	def __str__(self):
		return self.friendusername
