
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Applicant, StudentUser,Recruiter,Job
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def user_login(request):
    error=""
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            try:
                user1=StudentUser.objects.get(user=user)
                if user1.typ=="Student":
                    login(request, user)
                    return redirect('alljobs')
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request, 'user_login.html',d)

def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def admin_login(request):
    error=""
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'admin_login.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')

def user_signup(request):
    error=""
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        image=request.FILES['image']
        type=request.POST['type']
        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,password=password,username=email)
            StudentUser.objects.create(user=user,mobile=contact,image=image,gender=gender,typ=type)
            error="no"
            
        except:
            error="yes"
    d={'error':error}
    return render(request, 'user_signup.html',d)

def recruiter_login(request):
    error=""
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            try:
                user1=Recruiter.objects.get(user=user)
                if user1.typ=="Student" and user1.status=="pending":
                    login(request, user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request, 'recruiter_login.html',d)


def recruiter_signup(request):
    error=""
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        image=request.FILES['image']
        company=request.POST['company']
        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,password=password,username=email)
            Recruiter.objects.create(user=user,mobile=contact,image=image,gender=gender,typ="recruiter",company=company,status="pending")
            error="no"
            
        except:
            error="yes"
    d={'error':error}
    
    return render(request, 'recruiter_signup.html',d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
        
    return render(request,'recruiter_home.html')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    allusers=StudentUser.objects.all()
    d={'d':allusers}   
    return render(request,'view_users.html',d)

def delete_users(request,id=None):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if id is None:
        allusers=StudentUser.objects.all()
    else:

    
        allusers=StudentUser.objects.get(id=id)
        allusers.delete()
       
    return redirect('view_users')

def post_job(request):
    user=Recruiter.objects.get(user=request.user)
    print(user)
    error=""
    if request.method=='POST':
        jobtitle=request.POST['jobtitle']
        salary=request.POST['salary']
        type=request.POST['type']
        desc=request.POST['desc']
        location=request.POST['location']
        deadline=request.POST['deadline']
        
        try:
            job=Job.objects.create(title=jobtitle,type=type,company=user,salary=salary,desc=desc,location=location,deadline=deadline)
            error="no"
        except:
            error="yes"
    d={'error':error}
    
    return render(request, 'postjob.html',d)


def latestjob(request):
    user=Recruiter.objects.get(user=request.user)
    jobs=Job.objects.all()
    d={'jobs':jobs,'user':user}
    return render(request,'latestjob.html',d)

def job_detail(request,id):
    job=Job.objects.get(pk=id)
    d={'job':job}
    return render(request,'jobdetail.html',d)

def recruiter_list(request):
    
    user=request.user
    if user.is_authenticated:
        print(request.user)
        error=""
        
        try:
            if user.is_staff:
                recruiter=Recruiter.objects.all()
                error='no'
            else:
                redirect('admin_login')
                recruiter=""
                error='yes'
        except:
            error='yes'

    return render(request,'recruiter_list.html',{'d':error,'lists':recruiter})

def recruiter_delete(request,id):
    rec=Recruiter.objects.get(pk=id)
    rec.delete()   
    return redirect('recruiter_list')

def alljobs(request):
    jobs=Job.objects.all().order_by('-date_posted')
    return render(request,'alljobs.html',{'jobs':jobs})

def applicant(request,id):
    error=""
    if request.method=='POST':
        stu=StudentUser.objects.get(user=request.user)
        print(stu)
        job=Job.objects.get(pk=id)
        print(job.title)
        skills=request.POST['skills']
        mobile=request.POST['mobile']
        city=request.POST['city']
        try:
            applicant=Applicant.objects.create(skills=skills,mobile=mobile,city=city,name=stu,applied_job=job)
            error="no"
        except:
            error="yes"
    return render(request,'applicant.html',{'d':error})

def applicant_details(request):
    applicant=Applicant.objects.all()
    return render(request,'app_detail.html',{'applicants':applicant})

def deletejob(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        print(prod_id)
        job=Job.objects.get(id=prod_id)
        print(job)
        job.delete()
        data={'msg':'Deleted Job'}
        return JsonResponse(data)

def delete_recruiter(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        print(prod_id)
        rec=Recruiter.objects.get(id=prod_id)
        
        rec.delete()
        data={'msg':'Deleted Job'}
        return JsonResponse(data)









   
    



