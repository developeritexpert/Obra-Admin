from django.urls import path
from apps.dashboards.admin.controllers.dashboard_controller import admin_dashboard
from apps.dashboards.admin.controllers.customer_controller import all_customers
from apps.dashboards.admin.controllers.trade_partner_controller import all_trade_partners
from apps.dashboards.admin.controllers.products_controller import all_products
from apps.dashboards.admin.controllers.regions_controller import all_regions , create_region

app_name = "admin"

urlpatterns = [
    path("dashboard/", admin_dashboard , name="dashboard"),
    path("customers/", all_customers , name="customers"),
    path("trade-partners/", all_trade_partners , name="trade_partners"),
    
    path("products/", all_products , name="products"),

    # Regions Routes
    path("regions/" , all_regions , name="regions"),
    path("regions/add/" , create_region , name="create_region"),
    
]
