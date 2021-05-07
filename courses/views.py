from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    payload={'message': 'Hello World!'}
    response = JsonResponse(payload)
    return response

