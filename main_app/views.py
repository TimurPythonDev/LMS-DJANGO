from django.contrib import messages

from django.shortcuts import render, redirect,HttpResponse

from main_app.email_backend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from main_app.models import CustomUser





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





@login_required(login_url='/')
def Profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        'user': user,
    }

    return render(request,'profile/profile.html',context)

@login_required(login_url='/')
def Edit_Profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profession = request.POST.get('profession')
        data_brith = request.POST.get('data_brith')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(address)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profession = profession
            customuser.data_brith = data_brith
            customuser.phone = phone
            customuser.address = address

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request, 'Failed To Update Your Profile')

    context = {
        'user': user,
    }
    return render(request,'profile/edit_profile.html',context)