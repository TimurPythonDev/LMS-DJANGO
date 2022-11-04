from django.urls import path,include

from main_app import views
 


urlpatterns = [
    # Login urls
    path('',views.login,name='login'),


    #  Templates urls   
    path('base/',views.base,name='base'),


]