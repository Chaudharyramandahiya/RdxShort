from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate,login as dj_login,logout

# Create your views here.

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

            loginusername = request.POST['username']
            loginpassword = request.POST['password']

            user = authenticate(username=loginusername,password=loginpassword)

            if user is not None:
                dj_login(request,user)

                messages.success(request,"Login Successful")
                return redirect("/")

            else:
                messages.error(request,"Invalid Credentials ")
                return redirect("/login")

        else:
            return render(request, 'login.html')
    else:
        return redirect('/')


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    # user = User.objects.get(email=request.POST['email'])
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'signup.html', {'error': "User Already Exists"})

                except User.DoesNotExist:
                    User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'],
                    )
                    messages.success(request, "Signup Successful - Login Here")
                    return redirect(login)
            else:
                return render(request, 'signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'signup.html', {'error': "Password's Don't Match"})
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')




