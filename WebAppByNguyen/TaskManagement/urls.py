from django.urls import path
from . import views
urlpatterns =[
	path('', views.index, name = 'index'),
	path('home', views.index, name = 'home'),
	path('createTask', views.createTask, name = 'createTask'),
	path('listTask', views.listTask, name = 'listTask'),
	path('getTask', views.getTask, name = 'getTask'),
	# path('detailTask/<str:task>/', views.getTask, name = 'getTask'),
]