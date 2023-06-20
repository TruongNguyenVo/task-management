from django.contrib import admin
from .models import *
# Register your models here.
#thêm các model trong file models.py
admin.site.register(TaskCreation)
# admin.site.register(TaskAssignMent)
# admin.site.register(TaskTracking)
# admin.site.register(TaskDone)
# admin.site.register(Reminder)
# admin.site.register(RoomChat)
# admin.site.register(MessageChat)
admin.site.register(Account)

