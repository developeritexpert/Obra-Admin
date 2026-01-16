from django.shortcuts import render

def api_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return render(request, 'auth/login.html')