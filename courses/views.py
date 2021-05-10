from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
import json

# Create your views here.

def index(request):
    payload={'message': 'Hello World!'}
    response = JsonResponse(payload)
    return response

def signup (request):
    if request.method == "POST":
        data=json.loads(request.body)
        username = data.get ("username")
        password = data.get ("password")
        profile = Profile(username=username, password=password)
        profile.validate_unique()
        profile.save()
        return JsonResponse({
            "username": username,
            "message": "Profile created sucessfully"
        })

def login(request):
    if request.method == "POST":
        data=json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        try:
            profile = Profile.objects.get(username=username)
        except:
            return JsonResponse({
                "message" : f"Profile with {username}, Does Not Exist"
            })
        if profile.password==password:
            return JsonResponse({
                "message" : f"Login Successful. Welcome {username}"
            })
        else:
            return JsonResponse({
                "message" : "Login Unsuccessful"
            })
        

        


#Assignment
def sign_out(request):
    if request.method == "POST":
        data=json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        try:
            profile = Profile.objects.get(username=username)
            return JsonResponse({"message" : f"{username} has successfully logged out"})
        except:
            return JsonResponse({"message": f"user {username} could not log out due to network issues"})

def password_reset(request):
    if request.method == "POST":
        data=json.loads(request.body)
        username= data.get("username")
        password = data.get("password")
        password2 = data.get("password_again")
        try:
            profile=Profile.objects.get(username=username)
        except:
            return JsonResponse({
                "message" : f"Profile with username {username}, does not exist"
            })
        if password==password2:
            profile.password=password
            profile.save()
            return JsonResponse({
                "message": f"Dear {username}, your password is now set to {password2}"
            })
        else:
            return JsonResponse({
                "message" : f"password {password} does not match with {password2}"
            })