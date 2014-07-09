from django.shortcuts import render
from django.shortcuts import render_to_response
from modules.models import *
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.db.models.query import EmptyQuerySet
from django.http import HttpResponse

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
	#Try to retrieve usermodules base on request.user, but user is not authenticated yet
	try: 
		usermodules = UserModule.objects.filter(user=request.user)
	except:
		usermodules = UserModule.objects.none()

	if request.method == 'POST':
		form = Module_Form(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			
			# Uncomment this part later
			if request.user.is_authenticated():
				obj.user = request.user
			else:
				obj.user = User.objects.get(username__exact='default')

			try:
				usermodule = UserModule.objects.get(module = obj.module, user=obj.user)

			except:
				form.save()

			return render_to_response('addmodule.html', {'form': form, 'usermodules':usermodules}, context)
	else:
		form = Module_Form()
	return render_to_response('addmodule.html', {'form': form, 'usermodules':usermodules}, context)

def update(request):
	context = RequestContext(request)
	if request.method == 'GET':
		fromwhere = request.GET.get('fromwhere')
		towhere = request.GET.get('towhere')
		targetmodule = Module.objects.get(module_code = request.GET.get('module'))
		usermodule = UserModule.objects.get(module = targetmodule, user = request.user)
		usermodule.link = towhere
		usermodule.save()

		return render(request, 'modules/addmodule.html', context)

def newsearch(request):
	moduleslist = Module.objects.all()
	context = {'moduleslist': moduleslist}
	return render(request, 'modules/newsearch.html', context)

def home(request):
	context = RequestContext(request)
	moduleslist = Module.objects.all()
	#Try to retrieve usermodules base on request.user, but user is not authenticated yet
	try: 
		usermodules = UserModule.objects.filter(user=request.user)
	except:
		usermodules = UserModule.objects.none()

	return render_to_response('home.html', {'usermodules':usermodules, 'moduleslist': moduleslist}, context)

def newmodule(request):
	context = RequestContext(request)

	moduleslist = Module.objects.all()
	#Try to retrieve usermodules base on request.user, but user is not authenticated yet
	try: 
		usermodules = UserModule.objects.filter(user=request.user)
	except:
		usermodules = UserModule.objects.none()

	if request.method == 'GET':
		creator = request.user
		selectedToAdd = request.GET.get('chosen')
		selectedModule = Module.objects.get(module_code=selectedToAdd)
		try:
			usermodule = UserModule.objects.get(module=selectedModule, user=creator)
		except:
			usermodule = UserModule(module=selectedModule, user=creator, link="pal")
			usermodule.save()

		return render_to_response('home.html', {'usermodules':usermodules, 'moduleslist': moduleslist}, context)
	else:
		return render_to_response('home.html', {'usermodules':usermodules, 'moduleslist': moduleslist}, context)

def deletemodule(request):
	context = RequestContext(request)

	moduleslist = Module.objects.all()
	#Try to retrieve usermodules base on request.user, but user is not authenticated yet
	try: 
		usermodules = UserModule.objects.filter(user=request.user)
	except:
		usermodules = UserModule.objects.none()

	if request.method == 'GET':
		destroyer = request.user
		selectedToDel = request.GET.get('chosen')
		selectedModule = Module.objects.get(module_code=selectedToDel)
		usermodule = UserModule.objects.get(module=selectedModule, user=destroyer)
		usermodule.delete()

		return render_to_response('home.html', {'usermodules':usermodules, 'moduleslist': moduleslist}, context)
	else:
		return render_to_response('home.html', {'usermodules':usermodules, 'moduleslist': moduleslist}, context)

def palette(request):

	context = RequestContext(request)

	try: 
		usermodules = UserModule.objects.filter(user=request.user)
	except:
		usermodules = UserModule.objects.none()

	return render_to_response('palette.html', {'usermodules':usermodules}, context)
