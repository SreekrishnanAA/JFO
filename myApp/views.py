from django.shortcuts import render, HttpResponse
import subprocess
import json
import sys
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def organize(request):    
    if request.method == 'GET':
        if not request.user.username:
            return redirect("../login")
        
        script_path = "C:/Users/admin/junkFileOrganizer/myApp/fileSystem.py"
        process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with open('output.json', 'r') as f:
            data = json.load(f)
    if request.method == 'POST':
        location = request.POST.get("hiddenInput")
        
        script_path = "C:/Users/admin/junkFileOrganizer/myApp/idk.py"
        process = subprocess.Popen([sys.executable, script_path, location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # locations = str(stdout.decode())

        # script_path = "C:/Users/admin/junkFileOrganizer/myApp/deleteFiles.py"
        # process = subprocess.Popen([sys.executable, script_path, json.dumps(locations)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout, stderr = process.communicate()
        temp = stdout.decode().split(":")
        temp2 = [item.strip() for item in temp]
        datas = [int(data) for data in temp2]
        print(datas)
        return render(request, "statistics/index.html", {"datas" : datas})

    return render(request, "organize.html", {"data" : data})

def statistics(request):
     return render(request, "statistics/index.html")

def login(request):
     if request.method == 'GET':
        return render(request, "login/index.html")
     else:
        if request.POST.get('emailreg'):
           email = request.POST["emailreg"]
           password = request.POST["password"]
           password2 = request.POST["password2"]

           if password != password2:
               return render(request, "login/index.html")
           if User.objects.filter(username=email).exists():
               return render(request, "login/index.html")
           else:
               user = User.objects.create_user(username = email, email = email, password=password)
               user.save()
               user = authenticate(username = email , password = password)

               if user:
                   auth_login(request, user)
                   return redirect("/")
               else:
                   return render(request, "login/index.html")
        else:
            username = request.POST["emaillog"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password = password)

            if user:
                auth_login(request, user)
                return redirect("/")
            else:
                return render(request, "login/index.html")
            

def logout(request):
    auth_logout(request)
    return redirect("/")

def about(request):
    return render(request, "about.html")