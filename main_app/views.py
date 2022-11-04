from django.contrib import messages

from django.shortcuts import render, redirect,HttpResponse

from main_app.email_backend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required






def Base(request):
    return render(request,'base.html')



def Login(request):
    return render(request,'login.html')


def doLogin(request):
    if request.method == "POST":
       user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       print(user)
       if user != None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('hod_home')
           elif user_type == '2':
               return HttpResponse('This is Staff Panel')
           elif user_type == '3':
               return HttpResponse('This is Student Panel')
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('login')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')