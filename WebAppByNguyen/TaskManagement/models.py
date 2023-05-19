from django.db import models
from datetime import datetime

# Create your models here.

class TaskCreation(models.Model): 
	# tạo công việc
	nameTask = models.CharField(max_length = 255) # tên
	dataTask = models.TextField(max_length = 10000) #nội dung 
	startDate = models.DateTimeField(default = datetime.now, blank = True) # ngày tạo task, lấy mặc định
	endDate = models.DateTimeField() #ngày kết thúc task
	isImportant = models.BooleanField(default = False) # task có quan trong hay khong
	emailUSer = models.EmailField(max_length = 255, blank = True) # email người nhận task
	phoneUser = models.CharField(max_length = 255, blank = True)
	note = models.TextField(blank = True) # ghi chú
	status = models.BooleanField(default = False)

class TaskAssignMent(models.Model):
	 # phân công công việc
	nameUser = models.CharField(max_length = 255) #người nhận task
	emailUSer = models.EmailField(max_length = 255) # email người nhận task
	phoneUser = models.CharField(max_length = 255, blank = True)
	date = models.DateTimeField(default = datetime.now, blank = True) # lấy thời gian giao hiện tại, mặc định không thể sửa
	note = models.CharField(max_length = 255) # các điểm cần chú ý khi thực hiện task do người phân công nhắn

class TaskTracking(models.Model): 
	#xem tiến độ làm việc
	name = models.CharField(max_length = 255, default = None)
	status = models.BooleanField(default = False) #task đã hoàn thành hay chưa, mặc định chưa
	timeRest = models.DateTimeField() # thời gian còn lại của task

class TaskDone(models.Model): 
# các task đã hoàn thành
	name = models.CharField(max_length = 255) #tên task
	nameUser = models.CharField(max_length = 255) #người hoàn thành task
	date = models.DateTimeField(max_length = 255) #thời gian hoàn thành

class Reminder(models.Model): 
	#nhắc nhở
	name = models.CharField(max_length = 255) #tên nhắc nhở
	data = models.TextField(max_length = 255) #nội dung nhắc nhở
	date = models.DateTimeField(default = datetime.now, blank = True) #thời gian nhắc nhở

class RoomChat(models.Model): 
	#phòng để mọi người chat
	name = models.CharField(max_length = 255) # tên phòng 
	context = models.CharField(max_length = 10000) # nội dung phòng
	userCreate = models.CharField(max_length = 255) #người tạo phòng

class MessageChat(models.Model): 
	#nội dung chat
	data = models.TextField() # nội dung tin nhắn
	date = models.DateTimeField(default = datetime.now, blank = True) # ngày, giờ gởi
	userName = models.CharField(max_length = 255) # người gửi tin nhắn
	room = models.CharField(max_length = 255) # tên phòng

