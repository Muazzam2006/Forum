from rest_framework import serializers
from ..models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Topic
