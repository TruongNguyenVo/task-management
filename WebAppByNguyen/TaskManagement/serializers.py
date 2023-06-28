# file convert json API

from rest_framework import serializers
from .models import Account, TaskCreation
class AccountSerializer(serializers.ModelSerializer):
	"""
		các phần data được lấy và hiển thị trong API

	"""
	class Meta:
		model = Account
		fields = ["user", "type"] # "__all__"

class TaskCreationSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskCreation
		fields = ["nameTask", "dataTask", "username","endDate", "isImportant", "emailUSer","phoneUser", "note"]
