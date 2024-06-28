from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views  import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# from registration.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('users/', include('Users.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# admin.site.site_header = 'Time Management'
# admin.site.index_title = 'Service'   valid name-ebi