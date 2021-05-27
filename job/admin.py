from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Recruiter)

@admin.register(Job)
class Job_Admin(admin.ModelAdmin):
    list_display=['title','type','salary']

@admin.register(Applicant)
class Applicant_admin(admin.ModelAdmin):
    list_display=['skills','city']