from django.core.paginator import Paginator
from apps.dashboards.admin.repositories.trader_repository import (
    TraderRepository
)

class TraderService:
    @staticmethod
    def list_traders(
        *,
        search_query: str = "",
        sort_by: str = "created_at",
        order: str = "desc",
        page: int = 1,
        per_page: int = 10,
    ):
        queryset = TraderRepository.base_queryset()

        queryset = TraderRepository.search(queryset, search_query)
        queryset = TraderRepository.order(queryset, sort_by, order)

        paginator = Paginator(queryset, per_page)
        return paginator.get_page(page)
