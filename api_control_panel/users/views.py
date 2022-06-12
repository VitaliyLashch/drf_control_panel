
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import User
from rest_framework_simplejwt.state import token_backend
from .serializer import UserSerializer
import requests
import json
from django.views.decorators.csrf import csrf_exempt
class uuser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = UserSerializer(request.user).data
        return Response(dict(content))

    def put(self, request):
        print(request.data)
        content = UserSerializer(data=dict(request.data))

        if(content.is_valid()):
            content.save()
            return Response(200)
        else:
            content.save()
            return Response(400)

"""
def restore(request: HttpRequest):
    if request.method == 'POST':
        logging = json.loads(request.body)
        user_id = User.objects.get(email__iexact=logging['email'].strip()).id
        if user_id:
            rand_string = ''.join(random.choice(string.ascii_letters) for i in range(44))
            request_to_email = send_message_email.Email()
            request_to_email.send_massage(address_recipient=logging['email'].strip(),
                                          subject='restore password in Controle Panel',
                                          text='Щоб відновити пароль перейдіть по цій силці: http://127.0.0.1:8000/restore?'
                                               + rand_string)
            user_restore = RestoreUser(userid=user_id, key=rand_string, expire_date=datetime.now()+timedelta(hours=5), restorted=0)
            user_restore.save()
            return JsonResponse(data={"result": True, "message": "Login not existed."})
        else:
            return JsonResponse(data={"result": False, "message":"Login not existed."})
    elif request.method == 'GET':
        return render(request, 'authorization.html', {'auth': False})
"""

def getUserAll(request):
    k = []
    permission_classes = (IsAuthenticated,)
    for i in User.objects.all():
        k.append(UserSerializer(i).data)
    return JsonResponse({'data': k}, safe=False)

@csrf_exempt
def settings_user(request):

    try:
        if request.method == 'POST':
            us = json.loads(request.data)
            if(us):
                user = User(
                        username=us['username'],
                        email=us['email'],
                        permissions=us['permissions'],
                        password=us['password']
                )
                user.save()
            return Response(200)
        elif request.method == 'PATCH':
            us = json.loads(request.data)
            print(us)
            user = User.objects.get(id=us["id"])
            print(user)
            user.name = us["name"]
            user.email = us["email"]
            user.permissions = us["permissions"]
            user.save()
            return Response(request, status=200)
        elif request.method == 'DELETE':
            data = json.loads(request.data)
            user = User.objects.get(id=data['id'])
            user.delete()
            return Response(200)
    except:
        print(990)
        return Response(500)

def loger_api_filters(request):
    resp = requests.post(url='http://127.0.0.1:5559/get_api_loggin_data', json=json.loads(request.body), headers = {
                "x-api-key": '1111',
                "Content-Type": "application/json"
            })

    return Response(resp.json())


def loger_traceback_filters(request):
    resp = requests.post(url='http://127.0.0.1:5559/get_trace_loggin_data', json=json.loads(request.body), headers = {
                "x-api-key": '1111',
                "Content-Type": "application/json"
            })

    return Response(resp.json())


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(200)