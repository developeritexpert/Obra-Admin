from django.shortcuts import render
from obra.apps.dashboards.admin.services.trader_services import TraderService

def all_trade_partners(request):
    traders = TraderService.list_traders(
        search_query=request.GET.get("q", "").strip(),
        sort_by=request.GET.get("sort", "created_at"),
        order=request.GET.get("order", "desc"),
        page=request.GET.get("page"),
    )

    context = {
        "traders": traders,
        "search_query": request.GET.get("q", ""),
        "sort": request.GET.get("sort", "created_at"),
        "order": request.GET.get("order", "desc"),
    }

    return render(
        request,
        "dashboards/admin/pages/traders/traders.html",
        context
    ) 