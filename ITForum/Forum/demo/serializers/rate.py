from rest_framework import serializers
from ..models import rate


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = rate.Like


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = rate.Dislike
