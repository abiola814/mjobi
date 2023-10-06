from dataclasses import field
from rest_framework import serializers
from .models import Message , UserProfile,Customers

class MessageSeriallizer(serializers.ModelSerializer):
    user_name = serializers.SlugRelatedField(many=False,slug_field='username',queryset=UserProfile.objects.all())
    staff_name = serializers.SlugRelatedField(many=False,slug_field='username',queryset=UserProfile.objects.all())
    class Meta:
        model =Message
        fields = ['user_name','staff_name','description','time_taken']