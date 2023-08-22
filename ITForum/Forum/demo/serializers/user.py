from rest_framework import serializers
from ..models import User
from serializers import CategorySerializer


class UserSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        fields = ('__all__')
        model = User