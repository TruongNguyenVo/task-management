from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns =[
	# url hiển thị, hàm def trong views, tên trong views
	path('', views.index, name = 'index'),
	path('create', views.createTask, name = 'createTask'),
	path('list-task', views.listTask, name = 'listTask'),
	path('get-task/<int:id>', views.getTask, name = 'getTask'),
	path('edit-task/<int:id>', views.editTask, name = 'editTask'),
	path('list-task-done', views.listTaskDone, name = 'listTaskDone'),
	path('test', views.test, name = 'test'),
	path('register', views.register, name= 'register'),
	path('login', views.login, name= 'login'),
	path('logout', views.logout, name= 'logout'),
	path('get-task/download', views.download, name = 'download'),
	path('download', views.download, name = 'download'),
	# path('detailTask/<str:task>/', views.getTask, name = 'getTask'),


	# API
	path('api.get/user&api_token=<str:api_token>', views.getData, name = 'getData'),
	path('api.post/type/user', views.postInfor, name = 'postInfor'), # api dùng tài khoản, mật khẩu để lấy token user
	path('api.post/type/create&api_token=<str:api_token>', views.postTask, name = 'postTask'), # api dùng để tạo task
	path('api.delete/type/task=<str:name_task>&api_token=<str:api_token>', views.deleteData, name = 'deleteData'),
	path('api.putData/<int:id>', views.putData, name = 'putData'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)