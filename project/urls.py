from django.contrib import admin
from django.urls import path, include
# from registration.views import register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('users/', include('Users.urls')),
]

admin.site.site_header = 'Time Management'
admin.site.index_title = 'Service'