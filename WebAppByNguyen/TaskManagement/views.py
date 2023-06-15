from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TaskCreation, Account
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from time import time

#user register
from django.shortcuts import redirect 
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
		return render(request, 'createtask.html', context)

def listTask(request): #trang hiển thị các nhiệm vụ
	typeTask = 'doing'
	if request.method == "POST":
		typeTask = request.POST.get('type')
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
		'typeTask' : typeTask
	}
	return HttpResponse(template.render(context, request)) 
def getTask(request, id):

	task = TaskCreation.objects.get(id = id)
	template = loader.get_template("detailtask.html")


	message = ""

	try:
	# nếu user click done task thì cập nhật finishDate và status
		if request.POST["taskDone"] == "Done":
			delay(0.3)
			task.finishDate = datetime.now()
			task.status = True
			task.save()
			message = "task is successful !"
			return redirect("listTaskDone")
		# if request.POST["taskDont"] == "Dont":
		# 	delay(0.3)
		# 	task.status = False
		# 	task.save()
		# 	return redirect("listTaskDone")
	except MultiValueDictKeyError as e:
			message = e
	
	context = {
		'nameTask' : task.nameTask,
		'dataTask' : task.dataTask,
		'startDate' : task.startDate,
		'endDate' : task.endDate,
		'isImportant' : task.isImportant,
		'note' : task.note,
		'id' : task.id,
		'temp' : "Hdasdas",
	}

	return HttpResponse(template.render(context, request)) 
def listTaskDone(request): #hàm trả về các task đã done hoặc hết hạn
	task_list = TaskCreation.objects.all()
	task_status = []
	temp = ""
	for task in task_list:
		if task.status == True:
			tempTask = []
			tempTask = [task.nameTask, task.dataTask, task.finishDate]
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
def test(request):
	user = request.user
	if request.method == "POST":
		typeTask = request.POST.get('type')
	else:
		typeTask = "doing"
	template = loader.get_template("template.html")
	context = {
			'temp' : [typeTask]
		}
	return HttpResponse(template.render(context, request))


def register(request):
	template = loader.get_template("register.html")
	message = ""
	
	if request.method == "POST":
		# lấy user, password và password2 ở trang register
		user = request.POST['user']
		password = request.POST['pass']
		password2 = request.POST['pass2']


		# nếu hai pass và pass2 giống nhau
		if password == password2:
			# nếu user đã có
			if Account.objects.filter(user = user).exists():
				message = "User already used!"
				# return redirect('register')

			# nếu hai password giống nhau và user chưa tồn tại thì tạo tài khoản
			else:
				# database ngoài
				new_user = Account(
									user = user,
									pw = password)
				new_user.save()

				# database của django
				save_user = User.objects.create_user(username = user, email= "", password = password)
				save_user.save()
				message = "Register already successful!"
				return HttpResponse(loader.get_template("login.html").render({'user':user,'password' : password}, request))			

		# nếu hai pass và pass2 khác nhau
		else:
			message = "password is not same!"
			# return render(request,"register.html")
	
	# nếu người dùng chưa điền hết thông tin
	else:
		messages = "Fill all form!"
		# return render(request,"register.html")
	context = {
		'message' : message,
		}
	

	return HttpResponse(template.render(context, request))



def login(request):
	template = loader.get_template("login.html")
	user = request.user.username
	messages = ""
	if request.method == 'POST':
		#lấy user và password ở trang login
		username = request.POST['user']
		password = request.POST['pass']

		# xác thực lần 1
		authentic = Account.objects.filter(user = username, pw = password).exists()

		# nếu xác thực thành công
		if authentic == True:
			# xác thực lần 2
			user = auth.authenticate(username = username, password = password)
			if user is not None:
				auth.login(request,user)
				return redirect('/')
			else:
				messages = f'User or Password is incorrect! {username} {password} {user} else in'
		else:
			messages = f'User or Password is incorrect! {username} {password} {user} else out'
	# else:
	# 	return render(request, 'login.html',{'user': "", 'password' : "",})
	
	context = {
		'message' : [messages],
		'user': "", 
		'password' : "",
	}
	return HttpResponse(template.render(context, request))

def logout(request):
	auth.logout(request)
	context = {
		'user' : "",
		'password' : "",
	}
	return render(request, 'index.html', context)