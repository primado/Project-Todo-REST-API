from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from dj_rest_auth.views import LoginView

from .models import CustomUser
from .serializers import *

# Create your views here.

def index(request):
    return HttpResponse('Helloworld')


class CustomUserList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    

class CustomUserLogin(LoginView):
    serializer_class = CustomUserLoginSerializer

            
