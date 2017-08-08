from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import User, Friend

# Create your views here.

def index(request):
    return render(request, 'huddleupapp/index.html')

def aboutus(request):
    return render(request, 'huddleupapp/aboutus.html')

def login(request):
    return render(request, 'huddleupapp/login.html')

def user_detail(request, user_id):
	username = get_object_or_404(User, pk=user_id)
	return render(request, 'huddleupapp/user_detail.html', {'username': username})
