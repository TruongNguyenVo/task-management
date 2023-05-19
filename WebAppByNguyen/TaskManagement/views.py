from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TaskCreation, TaskTracking, TaskDone
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect 
#my models
from .modelsByNguyen import *	
# Create your views here.
def index(request):
	return render(request, 'index.html')
def createTask(request):
	if request.method == 'POST':
		#get value in createtask.html
		nameTask = request.POST['nameTask']
		dataTask = request.POST['dataTask']
		endDate = request.POST['endDate']
		if request.POST['isImportant'] == 'on': # if task is important -> on
			isImportant = True
		else:
			isImportant = False
		emailUSer = request.POST['emailUSer']
		phoneUser = request.POST['phoneUser']
		note = request.POST['note']
		save_task = TaskCreation(
								nameTask = nameTask, 
								dataTask= dataTask, 
								endDate = endDate,
								isImportant = isImportant,
								emailUSer = emailUSer,
								phoneUser = phoneUser,
								note = note)
		save_task.save()
		context = {
			'temp' : [nameTask,dataTask,endDate,isImportant,emailUSer,phoneUser,note]
		}
		#	['task 1', 'Detail task 1', '2023-05-18T23:09', 'on', 'lammai.0407@gmail.com', '0944058941', 'can than']
		return render(request, 'createtask.html', context)
	else:
		context = {
			'temp' : "else"
		}
		return render(request, 'createtask.html', context)

def listTask(request): #trang hiển thị các nhiệm vụ
	
	task_status = [] # gồm 3 tham số: name, status, timeRests
	task_list = TaskCreation.objects.all()
	time_now = datetime.now()
	for task in task_list:
		temp_task =[]
		
		#hiện thị còn bao nhiêu thời gian
		timeRest = task.endDate.replace(tzinfo=None) - datetime.now()

		# một task bao gồm: name, status và thời gian còn lại
		temp_task = [task.nameTask, task.status, days_hours_minutes(timeRest), task.id]
		task_status.append(temp_task)

	template = loader.get_template('listtask.html')
	
	context = { 
		'task_status': task_status
	}
	return HttpResponse(template.render(context, request)) 
def getTask(request, id):

	task = TaskCreation.objects.get(id = id)
	template = loader.get_template("detailtask.html")
	context = {
		'nameTask' : task.nameTask,
		'dataTask' : task.dataTask,
		'startDate' : task.startDate,
		'endDate' : task.endDate,
		'isImportant' : task.isImportant,
		'note' : task.note,


	}
	return HttpResponse(template.render(context, request)) 

