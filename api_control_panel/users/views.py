
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework_simplejwt.state import token_backend
from .serializer import UserSerializer


class User(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(UserSerializer(request.user).data)
        content = UserSerializer(request.user).data
        return Response(dict(content))


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(200)