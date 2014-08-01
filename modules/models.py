from django.db import models
from django import forms
from django.contrib.auth.models import User
#from allauth.account.models import EmailAddress
#from allauth.socialaccount.models import SocialAccount
from django_facebook import *
import hashlib

# Create your models here.
AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

class Module(models.Model):

	def __str__(self):
		return self.module_code
		
	module_code = models.CharField(max_length=10, null=True, blank=True)
	
	module_title = models.CharField(max_length=200, null=True, blank=True)
	
	department = models.CharField(max_length=50, null=True, blank=True)

	faculty = models.CharField(max_length=50, null=True, blank=True)

	module_description = models.TextField(null=True, blank=True)
	
	module_credit = models.FloatField(null=True, blank=True)
	
	prerequisite = models.TextField(null=True, blank=True)
	
	preclusion = models.TextField(null=True, blank=True)
	
	exam_date = models.CharField(max_length=200, null=True, blank=True)
	
	exam_duration = models.CharField(max_length=50, null=True, blank=True)

	preclu = models.CharField(max_length=50, null=True, blank=True)

	prereqAnd = models.CharField(max_length=50, null=True, blank=True)

	prereqOr = models.CharField(max_length=50, null=True, blank=True)
		
class Lesson(models.Model):
	ClassNo = models.CharField(max_length=50)
	LessonType = models.CharField(max_length=50)
	WeekText = models.CharField(max_length=50)
	DayText = models.CharField(max_length=50)
	StartTime = models.CharField(max_length=50)
	EndTime = models.CharField(max_length=50)
	Venue = models.CharField(max_length=50)
	module = models.ForeignKey(Module)

class UserModule(models.Model):
	def __str__(self):
		return self.module.module_code

	module = models.ForeignKey(Module)
	user = models.ForeignKey(User, blank=True, related_name="usermodule")
	#links may only be 'sem1', 'sem2' and so on or 'pal' for palette
	link = models.CharField(max_length=10, default='pal')
	unique_together = (("user", "module"),)

#TO CREATE USERMODULES
class Module_Form(forms.ModelForm):
	module = forms.ModelChoiceField(queryset=Module.objects.all().order_by("module_code"))
	
	class Meta:
		model = UserModule
		exclude = ('user', 'link')

#Creating USERFORM
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



#FACEBOOK EDIT
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
 
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
     
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
     
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
