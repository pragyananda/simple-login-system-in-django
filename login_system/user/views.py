from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect



# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return render(request,"register.html")
            elif User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,"User Created")
                return render(request,"login.html")
        else:
            messages.error(request,"Password not matching")
            return render(request,"register.html")
    else:
        return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user:
            auth.login(request,user)
            return render(request,"home.html")
        else:
            messages.error(request,"Invalid Credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def logout(request):
    auth.logout(request)
    return render(request,"login.html")

