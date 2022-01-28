from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    TEXT = os.environ.get("TEST")
    return HttpResponse(f"<h1>{TEXT}</h1>")
