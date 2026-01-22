from django.urls import path , include
from django.http import JsonResponse

def test(request):
    return JsonResponse({"success": True , "message": "Service is up and running."})

urlpatterns = [
    path('test/', test),
    
    path('auth/', include('apps.authentication.urls')),
    path('user/', include('apps.dashboards.user.urls')),
    path('trader/', include('apps.dashboards.trader.urls')),
    path('admin/', include('apps.dashboards.admin.urls')),
]
