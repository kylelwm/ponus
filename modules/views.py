from django.shortcuts import render

from modules.models import Module

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