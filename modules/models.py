from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Module(models.Model):

	def __str__(self):
		return self.module_code
		
	module_code = models.CharField(max_length=10, null=True, blank=True)
	
	module_title = models.CharField(max_length=200, null=True, blank=True)
	
	department = models.CharField(max_length=50, null=True, blank=True)
	
	module_description = models.TextField(null=True, blank=True)
	
	module_credit = models.FloatField(null=True, blank=True)
	
	prerequisite = models.TextField(null=True, blank=True)
	
	preclusion = models.TextField(null=True, blank=True)
	
	exam_date = models.CharField(max_length=200, null=True, blank=True)
	
	exam_duration = models.CharField(max_length=50, null=True, blank=True)
		
class Lesson(models.Model):
	ClassNo = models.CharField(max_length=50)
	LessonType = models.CharField(max_length=50)
	WeekText = models.CharField(max_length=50)
	DayText = models.CharField(max_length=50)
	StartTime = models.CharField(max_length=50)
	EndTime = models.CharField(max_length=50)
	Venue = models.CharField(max_length=50)
	module = models.ForeignKey(Module)

class Semester(models.Model):
	def __str__(self):
		return self.semester_name
	
	semester_name = models.CharField(max_length=20, null=True, blank=True)

class UserModule(models.Model):

	def __str__(self):
		return module.module_code
		
	module = models.ForeignKey(Module)
	semester = models.ForeignKey(Semester)
	
class Module_Form(forms.ModelForm):
	module = forms.ModelChoiceField(queryset=Module.objects.all().order_by("module_code"))
	
	class Meta:
		model = UserModule
		exclude = ('semester',)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	