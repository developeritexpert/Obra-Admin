from django.shortcuts import render
from apps.dashboards.admin.services.customer_service import CustomerService


def all_customers(request):
    customers = CustomerService.list_customers(
        search_query=request.GET.get("q", "").strip(),
        sort_by=request.GET.get("sort", "created_at"),
        order=request.GET.get("order", "desc"),
        page=request.GET.get("page"),
    )

    context = {
        "customers": customers,
        "search_query": request.GET.get("q", ""),
        "sort": request.GET.get("sort", "created_at"),
        "order": request.GET.get("order", "desc"),
    }

    return render(
        request,
        "dashboards/admin/pages/customers/customers.html",
        context
    )
