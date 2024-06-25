from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, PersonalSpaceSerializer
from .models import PersonalSpace
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# {"username":"username", "password":"password"}

User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # yvelas sheedzlos registracia


class LoginView(APIView):         #redirectebis damateba
    permission_classes = [AllowAny] # yvelas sheedzlos login

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None: 
                #useris avtomaturad shesvlistvis
                refresh = RefreshToken.for_user(user)
                user_data = UserSerializer(user).data
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': user_data
                }, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

#dasatesti class permissionebistvis-backistvis
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"message": "This is a protected view!"})
    

class PersonalSpaceView(generics.RetrieveUpdateAPIView):
    # queryset = PersonalSpace.objects.all()
    serializer_class = PersonalSpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.personal_space

    #     user = self.request.user
    #     if not user.is_authenticated:
    #         raise PermissionDenied("User must be logged in to access personal space.")
    #     try:
    #         return user.personal_space
    #     except PersonalSpace.DoesNotExist:
    #         raise PermissionDenied("Personal space does not exist for this user.")

    # def post(self, request, *args, **kwargs):
    #     # shevamowmot tu arsebobs personal space
    #     # if hasattr(self.request.user, 'personal_space'):
    #     #     raise PermissionDenied("Personal space already exists for this user.")

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user=self.request.user)    

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)