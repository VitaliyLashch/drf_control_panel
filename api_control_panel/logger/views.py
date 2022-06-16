from django.shortcuts import render
import requests
from rest_framework.response import Response
from django.http import JsonResponse
import json
# Create your views here.


def loger_api_filters(request):
    resp = requests.post(url='http://127.0.0.1:5559/get_api_loggin_data', json=json.loads(request.body), headers={
                "x-api-key": '1111',
                "Content-Type": "application/json"
            })
    return JsonResponse(resp.json())


def loger_traceback_filters(request):
    resp = requests.post(url='http://127.0.0.1:5559/get_trace_loggin_data', json=json.loads(request.body), headers={
                "x-api-key": '1111',
                "Content-Type": "application/json"
            })
    return JsonResponse(resp.json())

def loger_report(request):
    resp = requests.post(url='http://127.0.0.1:5559/get_api_report', json=json.loads(request.body), headers={
        "x-api-key": '1111',
        "Content-Type": "application/json"
    })
    return JsonResponse(resp.json())