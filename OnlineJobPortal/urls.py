"""OnlineJobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('admin_login/',admin_login,name='admin_login'),

    #admin
    path('admin_login/',admin_login,name='admin_login'),
    path('admin_home/',admin_home,name='admin_home'),

    #user and student
    path('user_signup/',user_signup,name='user_signup'),
    path('user_login/',user_login,name='user_login'),
    path('user_home/',user_home,name='user_home'),
    path('user_logout/',user_logout,name='user_logout'),
    path('all_users/',view_users,name='view_users'),
    path('delete_user/<int:id>/',delete_users,name='delete_user'),

    #recruiter
    path('recruiter_login/',recruiter_login,name='recruiter_login'),
    path('recruiter_signup/',recruiter_signup,name='recruiter_signup'),
    path('recruiter_home/',recruiter_home,name='recruiter_home'),
    path('recruiter_list/',recruiter_list,name='recruiter_list'),
    path('recruiter_delete/<int:id>/',recruiter_delete,name='recruiter_delete'),
    path('deleterec/',delete_recruiter), #for ajax

    #job pOsting
    path('postjob/',post_job,name='post_job'),
    path('latestjobs/',latestjob,name='latestjobs'),
    path('jobdetail/<int:id>/',job_detail,name='jobdetail'),
    path('alljobs/',alljobs,name='alljobs'),
    path('deletejob/',deletejob),

    #applicant
    path('applying/<int:id>/',applicant,name='applicant'),
    path('applicantdetail/',applicant_details,name='appdetail'),


]+static(settings.MEDIA_URL,docuemt_root=settings.MEDIA_ROOT)
