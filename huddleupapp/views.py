from django.shortcuts import get_object_or_404, render
from .models import Contact
from django.shortcuts import get_list_or_404

# Create your views here.

def index(request):
    return render(request, 'huddleupapp/index.html')

def aboutus(request):
    return render(request, 'huddleupapp/aboutus.html')

def login(request):
    return render(request, 'huddleupapp/login.html')

def tutorial(request):
    return render(request, 'huddleupapp/tutorial.html')

def mycalendar(request):
    return render(request, 'huddleupapp/mycalendar.html')

def detail(request, user_id):
	contact_list = get_list_or_404(Contact, Username=user_id)
	context = {'contact_list': contact_list}
	return render(request, 'huddleupapp/detail.html', context)
