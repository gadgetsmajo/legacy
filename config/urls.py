from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def health_check(request):
    return JsonResponse({'status': 'ok'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check, name='health-check'),
    path('api/auth/', include('accounts.urls')),
    path('api/shop/', include('shop.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/inquiries/', include('inquiries.urls')),
    path('api/newsletter/', include('newsletter.urls')),
    path('api/dashboard/', include('dashboard.urls')),
]
