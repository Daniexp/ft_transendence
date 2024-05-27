# Create your views here.

from django.shortcuts import render
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    print("PRESUNTA RUTA DE TEMPLATES")
    print(os.path.join(BASE_DIR))
    return render(request, 'myapp/index.html')

