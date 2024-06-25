from django.urls import path
from .views import RegisterView, LoginView, LogoutView,ProtectedView,PersonalSpaceView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tokens/', TokenRefreshView.as_view(), name='token_obtain_pair'), # token ganaxlebistvis 
    path('protect/', ProtectedView.as_view(), name='protected'), #requestis dasatestad
    path('personal/', PersonalSpaceView.as_view(), name='personal-space'),
]
