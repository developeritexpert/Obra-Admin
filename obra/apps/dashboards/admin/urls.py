from django.urls import path
from obra.apps.dashboards.admin.controllers.dashboard_controller import admin_dashboard
from obra.apps.dashboards.admin.controllers.customer_controller import all_customers
from obra.apps.dashboards.admin.controllers.trade_partner_controller import all_trade_partners
from obra.apps.dashboards.admin.controllers.products_controller import all_products

app_name = "admin"

urlpatterns = [
    path("dashboard/", admin_dashboard , name="dashboard"),
    path("customers/", all_customers , name="customers"),
    path("trade-partners/", all_trade_partners , name="trade_partners"),
    
    path("products/", all_products , name="products"),
    
]
