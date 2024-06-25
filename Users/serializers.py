from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()

class PersonalSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSpace
        fields = ['bio', 'profile_picture'] 
        read_only_fields = ['user'] # amas ro ver sheexos saertod, ro ar shecvalon 

class UserSerializer(serializers.ModelSerializer):  #es mushaobs, inaxavs bazashi. daloginebis mere minda tokeni
    personal_space = PersonalSpaceSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'personal_space']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        PersonalSpace.objects.create(user=user) #personal spaceis sheqmna
        return user # shevqmat da davabrunot daregistrirebuli user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


