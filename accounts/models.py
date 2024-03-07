from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.conf import settings
from rest_framework import request, status, viewsets


from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import UserSerializer
from rest_framework.response import Response



# Create your models here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # #authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50,default="",blank=True)
    reset_password_expire = models.DateTimeField(null=True,blank=True)

    
@receiver(post_save, sender=User)
def save_profile(sender,instance, created, **kwargs):

    print('instance',instance)
    user = instance

    if created:
        profile = Profile(user = user)
        profile.save()
     

