from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse



def home(request):
    return JsonResponse({"app":'users'})