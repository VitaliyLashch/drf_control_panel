from django.shortcuts import render
import json
import requests
from django.http import JsonResponse

# Create your views here.
def allPrice(request):
    resp = requests.get(url='http://192.168.0.101:5885/get_all_link', headers={
                "x-api-key": '1111',
                "Content-Type": "application/json"
            })
    return JsonResponse(resp.json())


def link(request):
    if request.method == 'POST':
        resp = requests.post(url='http://192.168.0.101:5885/link', json=json.loads(request.body), headers={
        "x-api-key": '1111',
        "Content-Type": "application/json"
    })
        return JsonResponse(resp.json(), safe=False)
    elif request.method == 'PATCH':
        resp = requests.post(url='http://192.168.0.101:5885/link/' + str(request.body['ID']), json=json.loads(request.body), headers={
            "x-api-key": '1111',
            "Content-Type": "application/json"
        })
        return JsonResponse({resp.json()}, safe=False)


def deleteLink(request, id_: str):
    resp = requests.get(url='http://192.168.0.101:5885/get_all_link/'+str(id_), headers={
        "x-api-key": '1111',
        "Content-Type": "application/json"
    })
    return JsonResponse({resp.json()}, safe=False)
