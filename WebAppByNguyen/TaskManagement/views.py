from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TaskCreation, TaskTracking, TaskDone
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from time import time
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

		try:
			if request.POST['isImportant'] == 'on': 
			# if task is important -> on
				isImportant = True
		except MultiValueDictKeyError:
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
		delay(0.3)
		return redirect('listTask')
	else:
		context = {
			# 'temp' : "else"
		}
		delay(0.3)
		return render(request, 'createtask.html', context)

def listTask(request): #trang hiển thị các nhiệm vụ
	
	task_status = [] # gồm 3 tham số: name, status, timeRests
	task_list = TaskCreation.objects.all()
	time_now = datetime.now()
	for task in task_list:
		temp_task =[]
		
		#hiện thị còn bao nhiêu thời gian
		timeRest = munis(datetime.now(),task.endDate)

		# một task bao gồm: name, status và thời gian còn lại
		temp_task = [task.nameTask, task.status, days_hours_minutes(timeRest), task.id]
		task_status.append(temp_task)
		temp = timeRest
	template = loader.get_template('listtask.html')
	
	context = { 
		'task_status': task_status,
		# 'temp' : connectDB() 
	}
	return HttpResponse(template.render(context, request)) 
def getTask(request, id):

	task = TaskCreation.objects.get(id = id)
	template = loader.get_template("detailtask.html")


	message = ""

	try:
	# nếu user click done task thì cập nhật endDate và status
		if request.POST["taskDone"] == "Done":
			task.endDate = datetime.now()
			task.status = True
			task.save()
			message = "task is successful !"
	except MultiValueDictKeyError:
			message = ""
	
	context = {
		'nameTask' : task.nameTask,
		'dataTask' : task.dataTask,
		'startDate' : task.startDate,
		'endDate' : task.endDate,
		'isImportant' : task.isImportant,
		'note' : task.note,
		'id' : task.id,
		'temp' : message,
	}


	return HttpResponse(template.render(context, request)) 
def listTaskDone(request): #hàm trả về các task đã done hoặc hết hạn
	task_list = TaskCreation.objects.all()
	task_status = []
	temp = ""
	for task in task_list:
		if task.status == True:
			tempTask = []
			timeEnd = task.endDate
			tempTask = [task.nameTask, task.dataTask, timeEnd]
			task_status.append(tempTask)
			# temp = task.endDate
	
	context = {
		'task_status' :task_status,
		'temp' : temp,
	}
	template = loader.get_template('taskdone.html')
	return HttpResponse(template.render(context, request)) 

def editTask(request, id):


	task = TaskCreation.objects.get(id = id)
	template = loader.get_template("edit.html")


	message = ""

	try:
	# nếu user click done task thì cập nhật endDate và status
		if request.POST["taskDone"] == "Done":
			task.endDate = datetime.now()
			task.status = True
			task.save()
			message = "task is successful !"
	except MultiValueDictKeyError:
			message = ""
	
	context = {
		'nameTask' : task.nameTask,
		'dataTask' : task.dataTask,
		'endDate' : task.endDate,
		'isImportant' : task.isImportant,
		'phoneUser': task.phoneUser,
		'emailUser' : task.emailUSer,
		'note' : task.note,
		'temp' : task.endDate,
	}

	if request.method == 'POST':
		#get value in createtask.html
		nameTask = request.POST['nameTask']
		dataTask = request.POST['dataTask']

		endDate = request.POST['endDate']
		if endDate == "":
			endDate = task.endDate
		try:
			if request.POST['isImportant'] == 'on': 
			# if task is important -> on
				isImportant = True
		except MultiValueDictKeyError:
			isImportant = False
		emailUSer = request.POST['emailUSer']
		phoneUser = request.POST['phoneUser']

		note = request.POST['note']
		edit_task = TaskCreation.objects.filter(id=id).update(
				nameTask = nameTask,
				dataTask = dataTask,
				endDate = endDate,
				isImportant = isImportant,
				emailUSer = emailUSer,
				phoneUser = phoneUser,
				)

		context = {
			# 'temp' : [nameTask,dataTask,endDate,isImportant,emailUSer,phoneUser,note]
			'temp' : "updated"
		}
		#	['task 1', 'Detail task 1', '2023-05-18T23:09', 'on', 'lammai.0407@gmail.com', '0944058941', 'can than']
		return redirect('listTask')

	return HttpResponse(template.render(context, request))

