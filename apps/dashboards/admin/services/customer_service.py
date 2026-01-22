from django.core.paginator import Paginator
from apps.dashboards.admin.repositories.customer_repository import (
    CustomerRepository
)


class CustomerService:
    @staticmethod
    def list_customers(
        *,
        search_query: str = "",
        sort_by: str = "created_at",
        order: str = "desc",
        page: int = 1,
        per_page: int = 10,
    ):
        queryset = CustomerRepository.base_queryset()

        queryset = CustomerRepository.search(queryset, search_query)
        queryset = CustomerRepository.order(queryset, sort_by, order)

        paginator = Paginator(queryset, per_page)
        return paginator.get_page(page)
