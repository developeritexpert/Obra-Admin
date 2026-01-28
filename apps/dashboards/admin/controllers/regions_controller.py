from django.shortcuts import render

def all_regions(request):
    return render(request, "dashboards/admin/pages/regions/all_regions.html")

def create_region(request):
    return render(request, "dashboards/admin/pages/regions/create_region.html")