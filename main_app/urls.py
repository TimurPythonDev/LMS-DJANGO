from django.urls import path,include

from hod_app import hod_views
from main_app import views




urlpatterns = [
    # Login urls
    path('',views.Login,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),


    #  Templates urls   
    path('base/',views.Base,name='base'),

    # hod urls
    path('hod/home/',hod_views.Home,name='hod_home')


]