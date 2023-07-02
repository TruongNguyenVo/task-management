from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TaskCreation, Account

from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from time import time
import json
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# file
from datetime import datetime, timedelta # time

#user register
from django.shortcuts import redirect 
from django.contrib.auth.models import User, auth
from django.contrib import messages


#my models
from .modelsByNguyen import *	
# Create your views here.
def test(request):
	user = request.user
	name = user.username
	context = {

	}
	
	# if user.is_authenticated:
	# 	temp = "Nguyen"
	# else:
	# 	temp = "Truong"

	# if request.method == "POST":
	# 	typeTask = request.POST.get('type')
	# else:
	# 	typeTask = "doing"

	# context = {
	# 		'temp' : [typeTask, temp,"1",TaskCreation.objects.all().filter(username = name)]
	# 	}

	# context.update(
	# 			# {'temp' : [getWeather()['status'],getWeather()['data']['Advice']] # [True, 'Mưa dông Thứ 7']
	# 			{
	# 			'temp' : [getWeather()['data']['Date']]
	# 			})

	# try:
	# 	if request.POST["status"] == "undone":
	# 		context.update({
	# 			'temp' : "un done",
	# 		})
	# except MultiValueDictKeyError:
	# 	pass

	
	# print()
	# path = TaskCreation.objects.all()[0].file.path

	# print()
	# # with open(TaskCreation.objects.all()[0].file.path, "r", encoding = "utf8") as f: # đọc file theo tiếng việt
	# # 	try:
	# # 		data_file = f.read()
	# # 	except Exception as e:
	# # 		data_file = e
	# file = ""
	# if request.method == "POST":
	# 	file = request.POST["myfile"]

	# task_save = TaskCreation(file = file, endDate = "2023-06-23 21:46:36.544131+00")
	# task_save.save()
	# context = {
	# 	'temp' : {'data' : file,
	# 			 'path' : path,
	# 			 'file' : TaskCreation.objects.all()[0].file,}
	# }



	# if request.POST['file'] == 'send':
	# 	pass
	

	# if request.method == "POST":
	# 	try:
	# 		file_save = request.FILES["fileTask"]
	# 		save = Document.objects.create(file = file_save)
	# 		save.save()
	# 		print()
	# 		print("DONEEEEEEEEEEEEEEEE")
	# 		print()
	# 	except 	MultiValueDictKeyError:
	# 		print()
	# 		print("NGHIIIIIIIIIIIIIIIIi")
	# 		print()



	template = loader.get_template("template.html")
	return HttpResponse(template.render(context, request))

def index(request):
	return render(request, 'index.html')
def createTask(request):
	user = request.user
	if request.method == 'POST' and user.is_authenticated:
		#get value in createtask.html
		nameTask = request.POST['nameTask']
		dataTask = request.POST['dataTask']
		# lấy file 
		try:
			file_save = request.FILES["fileTask"]
		# nếu không có file thì None
		except MultiValueDictKeyError:
			file_save = None

		# lấy ngày kết thúc nhiệm vụ
		try:
			endDate = request.POST['endDate']
		# nếu không có thì lấy ngày mặc định là sau 1 ngày
		except ValidationError:
			endDate = datetime.now()

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
								file = file_save,
								endDate = endDate,
								isImportant = isImportant,
								emailUSer = emailUSer,
								phoneUser = phoneUser,
								note = note,
								username = user.username)
		save_task.save()
		context = {
			'temp' : [nameTask,dataTask,endDate,isImportant,emailUSer,phoneUser,file_save,note]
		}
		#	['task 1', 'Detail task 1', '2023-05-18T23:09', 'on', 'lammai.0407@gmail.com', '0944058941', 'can than']
		delay(0.3)
		return redirect('listTask')
	else:
		context = {
			'login' : "Login to create task"

		}
		return render(request, 'createtask.html', context)

def listTask(request): #trang hiển thị các nhiệm vụ
	
	user = request.user
	typeTask = 'doing'
	if request.method == "POST":
		typeTask = request.POST.get('type')
	task_status = [] # gồm 3 tham số: name, status, timeRests
	task_list = TaskCreation.objects.all().filter(username = user.username)
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
		'typeTask' : typeTask,

	}
	return HttpResponse(template.render(context, request)) 
def getTask(request, id):
	# người dùng hiện tại
	user =request.user
	try:
		task = TaskCreation.objects.get(id = id, username = user.username)
	# nếu không có nhiệm vụ dó
	except ObjectDoesNotExist:
		return redirect("listTask")
	template = loader.get_template("detailtask.html")
	message = ""
	try:
	# nếu user click done task thì cập nhật finishDate và status
		if request.POST["task"] == "Done":
			delay(0.3)
			task.finishDate = datetime.now()
			task.status = True
			task.save()
			message = "task is successful !"
			return redirect("listTaskDone")
	# xóa task
		if request.POST["task"] == "Delete":
			delay(0.3)
			task.delete()
			message = "Deleted task !"
			return redirect("listTask")
	except MultiValueDictKeyError as e:
			message = e
	
	context = {
		'nameTask' : task.nameTask,
		'dataTask' : task.dataTask,
		'file' : task.file,
		'startDate' : task.startDate,
		'endDate' : task.endDate,
		'isImportant' : task.isImportant,
		'note' : task.note,
		'id' : task.id,
		'temp' : "Hdasdas",
	}

	return HttpResponse(template.render(context, request)) 
def listTaskDone(request): #hàm trả về các task đã done hoặc hết hạn
	

	user = request.user
	task_list = TaskCreation.objects.all().filter(username = user.username)
	task_status = []
	temp = ""
	
	# undone
	nameTask = request.POST.get('nameTask')
	if nameTask is not None:
		# tách số id (request trả về chuỗi)
		idTask = nameTask[len(nameTask) - 3 : - 1]
		task_change = TaskCreation.objects.get(id = idTask)
		# thay đổi về chưa hoàn thành
		task_change.status = False
		task_change.save()

	for task in task_list:
		if task.status == True:
			tempTask = []
			tempTask = {
					'name' : task.nameTask, 
					'data' : task.dataTask, 
					'finish' :task.finishDate, 
					'id' : task.id}
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
		'file' : task.file,
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



# hàm download file
def download(request):
	# đường dẫn của file

	path = TaskCreation.objects.filter(file = request.GET['download'])[0].file.path # lọc đường dẫn theo tên file, tên người 
	
	try:
		file_path = os.path.join(settings.MEDIA_ROOT, path)
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
		raise Http404
	except MultiValueDictKeyError:
		pass


	# with open(path.path, "r", encoding = "utf8") as f: # đọc file theo tiếng việt
	# 	try:
	# 		data_file = f.read()
	# 	except Exception as e:
	# 		data_file = e


	temp = request.GET['download']
	context = {
		# "temp" : TaskCreation.objects.filter(file = request.GET['download'])[0].file.path
		"temp" : [temp,file_path]
	}
	template = loader.get_template("template.html")
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
			if Account.objects.filter(username = user).exists():
				message = "User already used!"
				# return redirect('register')

			# nếu hai password giống nhau và user chưa tồn tại thì tạo tài khoản
			else:
				# table ngoài
				new_user = Account(
									username = user,
									password = password,
									api_token = randomToken(user))
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
		# authentic = Account.objects.filter(user = username, pw = password).exists()

		# nếu xác thực thành công
		user = auth.authenticate(username = username, password = password)
		# user_filter = Account.objects.all().filter(user = "vonguyen1").exists() # True-False

		if user is not None:
			auth.login(request,user)
			return redirect('/')
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















# A P I 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AccountSerializer, TaskCreationAPISerializer

	# if request.method == 'GET':
	# 	pass
	# elif request.method == 'POST':
	# 	pass

	# elif request.method == "DELETE":
	# 	pass
	# elif request.method == "PUT":
	# 	pass

	# GET - view
	# POST - create
	# DELETE - delete
	# PUT - update

@api_view(['GET'])
def getData(request, api_token):
#	# data -> dictionary (json)
	# print(Account.objects.get(api_token = api_token))

	try:
		user = Account.objects.get(api_token = api_token)
		data_user = {
			'account' : user.username,
			'type' :user.type,
		}

		get_task = TaskCreation.objects.filter(username = user.username)
		list_task = []
		for task in get_task:
			data_task = {
				'name' : task.nameTask,
				'data' :task.dataTask,
				'detail' : task.note,
				'day create' : task.startDate.strftime("%m/%d/%Y, %H:%M:%S"),
				'day end' : task.endDate.strftime("%m/%d/%Y, %H:%M:%S"),
				'status' : task.status

			}
			list_task.append(data_task)
		data = {
			'user' : data_user,
			'task' : list_task,
			'time' : datetime.now()

		}
	except Exception as e: 
		data = {
		"status" : e,
		}
	
	return Response(data)

@api_view(['POST'])
def postInfor(request):

	# đăng nhập bằng API lấy type người dung
	if request.method == "POST":
		serializer = AccountSerializer(data = request.data)
		# xác thực api
		if serializer.is_valid():
			data_response = serializer.data
			username = data_response['username']
			password = data_response['password']
			user = Account.objects.filter(username = username, password = password).exists()
			if user == True:
				account = Account.objects.get(username = username, password = password)
				data = {
				'status' : 'Đăng nhập thành công',
				'username' : account.username,
				'type' : account.type,
				'token' : account.api_token,}
			else:
				data = {
					'status' : 'Không tìm thấy tài khoản',
					'user' : None,
				}
			return Response({
				"data" : data,
				"time" : datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			})
		else:
			data = {
				"data" : "Data thiếu hoặc chưa được xác thực",
				"time" :datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			}
			return Response(data)

# API dùng để tạo nhiệm vụ
@api_view(['POST'])
def postTask(request, api_token):
	serializer =  TaskCreationAPISerializer(data = request.data)
	# lấy username trong Account theo api_token
	try:
		username = Account.objects.get(api_token = api_token).username
	# nếu không tìm thấy tài khoản
	except:
		return Response({
				"status" : False,
				"data" : "Không tìm thấy tài khoản! ( Find not account! )"
			})
	# gán giá trị nếu trong có giá trị truyền vào
	if serializer.is_valid():
		response_data = serializer.data
		# lấy dữ liệu từ user
		try:
			name_task = response_data['nameTask']
		except KeyError:
			name_task = None
		try:
			data_task = response_data['dataTask']
		except KeyError:
			data_task = None
		try:
			end_date = response_data['endDate']
		except KeyError:
			end_date = None
		try:
			isImportant = response_data['isImportant']
		except KeyError:
			isImportant = None
		try:
			email_user = response_data['emailUSer']
		except KeyError:
			email_user = None
		try:
			phone_user = response_data['phoneUser']
		except KeyError:
			phone_user = None
		try:
			note = response_data['note']
		except KeyError:
			note = None

		"""
		ĐOẠN CODE TẠO NHIỆM VỤ
		"""
		data = {
			'status' :True,
			'data' : "Tạo nhiệm vụ thành công ( Create task successful!)",
		}
	else:
		data = {
			'status' :False,
			'data' : "Data truyền vào không đúng định dạng! ( The data is not in the correct form! )",

		}

	return Response({
			'data' :data,
			'time' :datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
		})
@api_view(["DELETE"])
def deleteData(request, name_task, api_token):

	data = {
		"status" : False,
		"name" : name_task,
		"time" : datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	}
	# lấy tên người dùng dựa vào api_token
	try:
		username = Account.objects.get(api_token = api_token).username
		# nếu tài khoản tồn tại
		try:
			task = TaskCreation.objects.get(username = username, nameTask = name_task)
			data.update({
					"status" :True,
					"user" : username,
					"data" : "Xóa " + task.nameTask + " thành công!" + "( Delete " + task.nameTask +" successful!)"
				})
			"""
			ĐOẠN CODE XÓA NHIỆM VỤ
			task.delete()			
			"""
			return Response(data)
		# nếu không có nhiệm vụ 
		except Exception :
			data.update({
				"user" : username,
				"data" : "Không tìm thấy nhiệm vụ! (Find not task!)"
				})
			return Response(data)

	# nếu không có tài khoản dự vào username
	except :
		data.update({
			"data" : "Không tìm thấy tài khoản!" + " (Find not account!)"
			
		})
		return Response(data)
	# lấy task theo name_task và api_token người dùng


	
	


@api_view(['PUT'])
def putData(request, id):
	pass