from django.urls import path
from .views import RegisterView, LoginView, LogoutView,ProtectedView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #radgan loginshi ukve vagvareb agharaa sawhiro aq, tumca tu shevcvli mashin damwhirdeba 
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protect/', ProtectedView.as_view(), name='protected')
]