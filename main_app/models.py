from django.db import models

from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField



class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )


    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    data_brith = models.DateField(auto_now_add=True,null=True,blank=True)
    mobile = PhoneField(blank=True,help_text='Contact Phone Number')
    address = models.CharField(max_length=202,null=True,blank=True)
    proffession = models.CharField(max_length=202,null=True,blank=True)