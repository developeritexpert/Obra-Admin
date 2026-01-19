from django.shortcuts import render

def user_dashboard(request):
    return render(request, "dashboards/user/dashboard.html")
