from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class EmailBackEnd(ModelBackend):

    def authenticate(self,usernam=None,password=None,**kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=usernam)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None