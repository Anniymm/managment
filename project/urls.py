from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]

admin.site.site_header = 'Time Management'
admin.site.index_title = 'Service'