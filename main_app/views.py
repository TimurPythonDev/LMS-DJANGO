from django.shortcuts import render



def base(request):
    return render(request,'base.html')



def login(request):
    return render(request,'login.html')

