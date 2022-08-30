from django.shortcuts import render
import requests
from rest_framework.response import Response
from django.http import JsonResponse
import json
# Create your views here.
from api_control_panel.settings import CONFIG_LOGER

# Create your views here.
LINK = ('https://' + CONFIG_LOGER['host'] + ':' + str(CONFIG_LOGER['port'])) if CONFIG_LOGER['ssl'] \
    else ('http://' + CONFIG_LOGER['host'] + ':' + str(CONFIG_LOGER['port']))

def loger_api_filters(request):
    resp = requests.post(url=LINK + '/get_api_loggin_data', json=json.loads(request.body), headers={
                "x-api-key": CONFIG_LOGER['api_key'],
                "Content-Type": "application/json"
            })
    return JsonResponse(resp.json())


def loger_traceback_filters(request):
    resp = requests.post(url=LINK + '/get_trace_loggin_data', json=json.loads(request.body), headers={
                "x-api-key": CONFIG_LOGER['api_key'],
                "Content-Type": "application/json"
            })
    return JsonResponse(resp.json())

def loger_report(request):
    resp = requests.post(url=LINK + '/get_api_report', json=json.loads(request.body), headers={
        "x-api-key": CONFIG_LOGER['api_key'],
        "Content-Type": "application/json"
    })
    return JsonResponse(resp.json())