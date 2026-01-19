from django.urls import path , include
from django.http import JsonResponse

def test(request):
    return JsonResponse({"success": True , "message": "Service is up and running."})

urlpatterns = [
    path('test/', test),
    
    path('auth/', include('obra.apps.authentication.urls')),
    path('user/', include('obra.apps.dashboards.user.urls')),
    path('trader/', include('obra.apps.dashboards.trader.urls')),
    path('admin/', include('obra.apps.dashboards.admin.urls')),
]
