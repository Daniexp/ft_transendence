from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import requests

# Create your views here.

authorize_url = "https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-7f23e63d9f57af46395fc37255f56e7ad8e8c11b19428dc7518a02725743582e&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=public"
state = "juajcuiwgciu7348vijbibrr"


def intraLogin(request):
    return redirect(authorize_url)

def printAuthRequest(request):
    code = request.GET.get('code')
    exchange_code(code)
    return JsonResponse(request.GET.dict())

def exchange_code(code):
    data = {
        "grant_type":"client_credentials",
        "client_id": "u-s4t2ud-7f23e63d9f57af46395fc37255f56e7ad8e8c11b19428dc7518a02725743582e",
        "client_secret": "", ## deleteado por securite, hay que hablar hasta que punto se podria liar y como evitarlo
        "code": code,
        "redirect_uri": "http://localhost:8080/oauth/login/redirect",
        #"state": state,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    response = requests.post("https://api.intra.42.fr/oauth/token", data=data, headers=headers)
    print(response)
    print(code)
    credentials = response.json()
    print(credentials)
