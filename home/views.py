from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import HttpResponse

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='signin')
def index(request):
    if 'name' in request.session:
        return render(request,'index.html')
    else:
        return redirect('signin')


def signup(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email = email).exists():
            messages.info(request,'Email Taken')
            return redirect('signup')
        elif User.objects.filter(username = username).exists():
            messages.info(request,'Username Taken')
            return redirect('signin')
        else:
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
        
    else:
        return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        request.session['name']=username

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Credentials not valid')
            return redirect('signin')
    else:
       return render(request,'login.html')


@login_required(login_url='signin')
def logout(request):
    del request.session['name']
    auth.logout(request)
    return redirect('signin')

 