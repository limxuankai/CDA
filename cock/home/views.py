from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    print(request)
    if request.method == 'POST':
        username = request.POST.get('Name')
        password = request.POST.get('Password')
        print(user)
        return redirect("dashboard")
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")
    