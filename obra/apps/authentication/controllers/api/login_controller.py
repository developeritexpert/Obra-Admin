from django.shortcuts import render

def api_login(request):
    return render(request, 'auth/login.html')