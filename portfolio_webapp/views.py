from django.shortcuts import render
from projects.models import projects

def home(request):
	project = projects.objects
	return render(request,'index.html',{'projects':project})


