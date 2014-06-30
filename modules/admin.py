from django.contrib import admin
from modules.models import *

# Register your models here.
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Semester)
admin.site.register(UserModule)
admin.site.register(Semester_UserModule_Link)