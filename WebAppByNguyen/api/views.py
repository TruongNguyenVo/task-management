from rest_framework.response import Response
from rest_framework.decorators import api_view

# GET - view
# POST - create
# DELETE - delete
# PUT - update

@api_view(['GET'])
def getData(request):
	# data -> dictionary (json)
	person = {
		'position' : 'admin',
		'name' : 'Nguyen',
		'gender' : 'Male',
		'age' : 19,
	}
	return Response(person)