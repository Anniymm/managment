from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):  #es mushaobs, inaxavs bazashi. daloginebis mere minda tokeni
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        PersonalSpace.objects.create(user=user) #personal spaceis sheqmna
        return user #shevqmat da davabrunot daregistrirebuli user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class PersonalSpaceSerializer(serializers.Serializer):
    class Meta:
        model = PersonalSpace
        fields = ['bio', 'profile_picture'] #isedac gadaecema user da 2jer gamodis 
        # read_only_fields = ['user'] # amas ro ver sheexos saertod
    def create(self, validated_data):
        user = self.context['request'].user
        return PersonalSpace.objects.create(user=user, **validated_data)