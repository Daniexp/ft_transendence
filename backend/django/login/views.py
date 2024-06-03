from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import requests

# Create your views here.

authorize_url = "https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-7f23e63d9f57af46395fc37255f56e7ad8e8c11b19428dc7518a02725743582e&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Foauth2%2Flogin%2Fredirect&response_type=code"


def intraLogin(request):
    return redirect(authorize_url)

def printAuthRequest(request):
    code = request.GET.get('code')
    exchange_code(code)
    return JsonResponse(request.GET.dict())

def exchange_code(code):
    data = {
        "client_id": "u-s4t2ud-7f23e63d9f57af46395fc37255f56e7ad8e8c11b19428dc7518a02725743582e",
        "client_secret": "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",
        "code": code,
        "redirect_uri": "http://localhost:8080/oauth/login/redirect",
    }
    headers = {
        #'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
   

    response = requests.post("https://api.intra.42.fr/oauth/token", data=data)#, headers=headers)
    print(response)
    credentials = response.json()
