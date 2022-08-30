from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from api_control_panel.settings import CONFIG_PARSER

# Create your views here.
LINK = ('https://' + CONFIG_PARSER['host'] + ':' + str(CONFIG_PARSER['port'])) if CONFIG_PARSER['ssl'] \
    else ('http://' + CONFIG_PARSER['host'] + ':' + str(CONFIG_PARSER['port']))
# Create your views here.
def allPrice(request):
    resp = requests.get(url=LINK + '/get_all_link', headers={
                "x-api-key": CONFIG_PARSER['api_key'],
                "Content-Type": "application/json"
            })
    return JsonResponse(resp.json())


def link(request):
    if request.method == 'POST':
        resp = requests.post(url=LINK + '/link', json=json.loads(request.body), headers={
        "x-api-key": CONFIG_PARSER['api_key'],
        "Content-Type": "application/json"
    })
        return JsonResponse(resp.json(), safe=False)
    elif request.method == 'PATCH':
        resp = requests.post(url=LINK + '/link/' + str(request.body['ID']), json=json.loads(request.body), headers={
            "x-api-key": CONFIG_PARSER['api_key'],
            "Content-Type": "application/json"
        })
        return JsonResponse({resp.json()}, safe=False)


def deleteLink(request, id_):
    resp = requests.delete(url=LINK + '/link/' + str(id_), headers={
        "x-api-key": CONFIG_PARSER['api_key'],
        "Content-Type": "application/json"
    })
    return JsonResponse(resp.status_code, safe=False)