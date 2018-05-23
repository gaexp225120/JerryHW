from django.shortcuts import render_to_response
from.models import Person
def index(request):
	person=Person.objects.all()
	return render_to_response('www/menu.html',locals())