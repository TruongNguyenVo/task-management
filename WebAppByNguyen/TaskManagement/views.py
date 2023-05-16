from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, 'index.html')
def createTask(request):
	return render(request, 'createtask.html')
def listTask(request):
	return render(request, 'listtask.html')
def getTask(request):
	return render(request, 'detailtask.html')