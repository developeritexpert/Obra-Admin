from django.shortcuts import render

def all_pages(request):
    return render(request,"dashboards/admin/pages/page_builder/website_pages.html")

def edit_pages(request):
    return render(request,"dashboards/admin/pages/page_builder/personalized_pages.html")