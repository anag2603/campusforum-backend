from rest_framework import serializers
from rest_framework.authtoken.models import Token
from CampusForum_API.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class ProfilesSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = "__all__"
class ProfilesAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = '__all__'
        depth = 1
