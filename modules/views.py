from django.shortcuts import render
from django.shortcuts import render_to_response
from modules.models import *
from django.template import RequestContext
from django import forms

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
	
	if request.method == 'POST':
		form = Module_Form(request.POST)
		if form.is_valid():
			form.save(commit=False)
			return index(request)
	else:
		form = Module_Form()
	return render_to_response('addmodule.html', {'form': form}, context)