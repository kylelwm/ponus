from django.shortcuts import render
from django.shortcuts import render_to_response
from modules.models import *
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.db.models.query import EmptyQuerySet

# Create your views here.

def index(request):
    return render(request, 'modules/index.html')

def modulelist(request):
	latest_module_list = Module.objects.all()
	context = {'latest_module_list': latest_module_list}
	return render(request, 'modules/modulelist.html', context)
	
def testsearch(request):
	latest_module_list = Module.objects.all()
	context = {'latest_module_list': latest_module_list}
	return render(request, 'modules/testsearch.html', context)
	
def sorttable(request):
	latest_module_list = Module.objects.all()
	context = {'latest_module_list': latest_module_list}
	return render(request, 'modules/sorttable.html', context)
	
def addmodule(request):
	context = RequestContext(request)
	palette_modules = UserModule.objects.filter(user=request.user)
	semesterusermodulelink = Semester_UserModule_Link.objects.filter(user=request.user)
	#CREATE SEMESTER IF IT DOESN'T EXIST STILL
	if isinstance(Semester.objects.filter(user=request.user), EmptyQuerySet):
		Semester.objects.create(semester_name='Semester 1', user=request.user)
		Semester.objects.create(semester_name='Semester 2', user=request.user)
		Semester.objects.create(semester_name='Semester 3', user=request.user)
		Semester.objects.create(semester_name='Semester 4', user=request.user)
		Semester.objects.create(semester_name='Semester 5', user=request.user)
		Semester.objects.create(semester_name='Semester 6', user=request.user)

	if request.method == 'POST':
		form = Module_Form(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			
			# Uncomment this part later
			if request.user.is_authenticated():
				obj.user = request.user
			else:
				obj.user = User.objects.get(username__exact='Ming')
			form.save()

			return render_to_response('addmodule.html', {'form': form}, context)
	else:
		form = Module_Form()
	return render_to_response('addmodule.html', {'form': form}, context)