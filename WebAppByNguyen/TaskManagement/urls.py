from django.urls import path
from . import views
urlpatterns =[
	path('', views.index, name = 'index'),
	path('createTask', views.createTask, name = 'createTask'),
	path('listTask', views.listTask, name = 'listTask'),
	path('getTask/<int:id>', views.getTask, name = 'getTask'),
	# path('detailTask/<str:task>/', views.getTask, name = 'getTask'),
]