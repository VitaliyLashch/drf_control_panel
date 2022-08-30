from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from api_control_panel.settings import CONFIG_MOBILE

# Create your views here.
LINK = ('https://' + CONFIG_MOBILE['host'] + ':' + str(CONFIG_MOBILE['port'])) if CONFIG_MOBILE['ssl'] \
    else ('http://' + CONFIG_MOBILE['host'] + ':' + str(CONFIG_MOBILE['port']))


def all_banners(request):
    if request.method == 'POST':
        resp = requests.post(url=LINK + '/postFilterPromo', json=json.loads(request.body), headers={
            "x-api-key": CONFIG_MOBILE['api_key'],
            "Content-Type": "application/json"
        })
        return JsonResponse(resp.json(), safe=False)


def banners_edit_content(request, id):
    if request.method == 'PATCH':
        resp = requests.post(url=LINK + '/banners_content' + str(id), json=json.loads(request.body), headers={
            "x-api-key": CONFIG_MOBILE['api_key'],
            "Content-Type": "application/json"
        })
        return JsonResponse(resp.json(), safe=False)
    elif request.method == 'DELETE':
        resp = requests.post(url=LINK + '/banners_content/' + str(id), json=json.loads(request.body), headers={
            "x-api-key": CONFIG_MOBILE['api_key'],
            "Content-Type": "application/json"
        })
        return JsonResponse(resp.json(), safe=False)


def post_banners_content(request):
    if request.method == 'POST':
        resp = requests.post(url=LINK + '/banners_content', json=json.loads(request.body), headers={
            "x-api-key": CONFIG_MOBILE['api_key'],
            "Content-Type": "application/json"
        })
        return JsonResponse(resp.json(), safe=False)


def post_banners_image(request):
    if request.method == 'POST':
        resp = requests.post(url=LINK + '/banners_image', files=request.FILES, headers={
            "x-api-key": CONFIG_MOBILE['api_key']
        })
        return JsonResponse(resp.json(), safe=False)


def patch_banners_image(request, id):
    if request.method == 'PATCH':
        resp = requests.patch(url=LINK + '/banners_image/' + str(id), files=request.FILES, headers={
            "x-api-key": CONFIG_MOBILE['api_key']
        })
        return JsonResponse(resp.json(), safe=False)
