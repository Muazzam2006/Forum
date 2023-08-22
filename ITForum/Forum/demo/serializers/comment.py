from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Comment
