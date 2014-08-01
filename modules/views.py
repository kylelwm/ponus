from django.shortcuts import render
from django.shortcuts import render_to_response
from modules.models import *
from django.template import RequestContext
from django import forms
from django.contrib.auth.models import User
from django.db.models.query import EmptyQuerySet
from django.http import HttpResponse
from modules.models import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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


#Registration page
def main(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Update our variable to tell the template registration was successful.
            registered = True            
            #log in after registering and making sure the form is valid
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
            	login(request, user)
            	moduleslist = Module.objects.all()
            	try:
            		usermodules = UserModule.objects.filter(user=request.user)
            	except:
            		usermodules = UserModule.objects.none()
            	return render_to_response('home.html', {'usermodules':usermodules, 'moduleslist': moduleslist}, context)
        else:
			print user_form.errors
    else:
        user_form = UserForm()


    # Render the template depending on the context.
    return render_to_response(
            'modules/main.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/modules/home')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('modules/main.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/modules/main.html')