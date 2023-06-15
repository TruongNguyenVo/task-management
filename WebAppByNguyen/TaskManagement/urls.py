from django.urls import path
from . import views
urlpatterns =[
	path('', views.index, name = 'index'),
	path('createTask', views.createTask, name = 'createTask'),
	path('listTask', views.listTask, name = 'listTask'),
	path('getTask/<int:id>', views.getTask, name = 'getTask'),
	path('editTask/<int:id>', views.editTask, name = 'editTask'),
	path('listTaskDone', views.listTaskDone, name = 'listTaskDone'),
	path('test', views.test, name = 'test'),
	path('register', views.register, name= 'register'),
	path('login', views.login, name= 'login'),
	path('logout', views.logout, name= 'logout'),
	# path('detailTask/<str:task>/', views.getTask, name = 'getTask'),
]