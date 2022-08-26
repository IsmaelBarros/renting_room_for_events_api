from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/room/', include('room.urls')),
    path('api/event/', include('event.urls')),
    path('api/book/', include('book.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    # Optional UI:
    path(
        'api/docs/', 
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs'
    ),
]
