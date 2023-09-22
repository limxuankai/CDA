from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden
from django.urls import reverse

# Create your views here.
def home(request):
    try:
        request.session.get('username') 
    except KeyError:
        request.session['username'] is None
    if request.session.get('username') is not None:
        return redirect("dashboard")
    if request.method == 'POST':
        username = request.POST.get('Name')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "home.html")
        else:
            request.session['username'] = username
            return redirect('dashboard', user=request.session.get('username'))
    return render(request, "home.html")

def dashboard(request, user):
    if 'username' not in request.session:
        return render(request,"trial.html")
    username = request.session['username']
    context = {
        'user': username,
    }
    return render(request, "dashboard.html", context)

def trial(request):
    return render(request,"trial.html")

def index(request):
    return render(request, "trial.html")