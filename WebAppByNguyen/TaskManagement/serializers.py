# file convert json API

from rest_framework import serializers
from .models import Account, TaskCreationAPI
class AccountSerializer(serializers.ModelSerializer):
	"""
		các phần data được lấy và hiển thị trong API

	"""
	class Meta:
		model = Account
		fields = ["username", "password"] # "__all__"

class TaskCreationAPISerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskCreationAPI
		fields = '__all__'

