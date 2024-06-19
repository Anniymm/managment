from django.urls import path
from .views import RegisterView, LoginView, LogoutView,ProtectedView,PersonalSpaceView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), #aqac mibrundeba, amitom tokens sadac mibrundeba is da es ar chakonflikdnen
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tokens/', TokenRefreshView.as_view(), name='token_obtain_pair'), #davabrunot orive refresh da access token
    path('protect/', ProtectedView.as_view(), name='protected'), #requestis dasatestad
    path('personal/', PersonalSpaceView.as_view(), name='personal'),
]
