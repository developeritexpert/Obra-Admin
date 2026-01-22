from django.shortcuts import render

def all_products(request):
    return render(request, "dashboards/admin/pages/products/all_products.html")