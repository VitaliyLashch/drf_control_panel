from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework.renderers import JSONRenderer

class getUserFromToken(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(UserSerializer(User.objects.get(id=request.user.id)).data)
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(200)