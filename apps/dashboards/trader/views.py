from django.shortcuts import render

def trader_dashboard(request):
    return render(request, "dashboards/trader/dashboard.html")
