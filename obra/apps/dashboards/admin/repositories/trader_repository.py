from django.db.models import Q
from obra.apps.users.models import User


class TraderRepository:
    @staticmethod
    def base_queryset():
        return User.objects.filter(role=User.Role.TRADER)

    @staticmethod
    def search(queryset, search_query: str):
        if not search_query:
            return queryset

        return queryset.filter(
            Q(email__icontains=search_query) |
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )

    @staticmethod
    def order(queryset, sort_by: str, order: str):
        if order == "desc":
            sort_by = f"-{sort_by}"
        return queryset.order_by(sort_by)
