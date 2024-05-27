# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    return render(request, 'myapp/index.html')

def get_data(request):
    data = {"message": "Hello, World!"}
    return JsonResponse(data)

