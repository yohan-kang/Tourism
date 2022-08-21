from asyncio.windows_events import NULL
from rest_framework import serializers
from .models import Board
from django.db import models

from django.conf import settings

class BoardSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    fk_writer = serializers.CharField(source="writer")
    content = serializers.CharField()
    created_at = serializers.DateTimeField()

    # accessUser = serializers.RelatedField( read_only=True)
    def to_representation(self, instance):
      res = super().to_representation(instance)
      res.update({'fk_writer': instance.writer.__str__()}) 
      return res

    class Meta:
        model=Board
        fields = ['id','title','fk_writer','content','created_at']
        # fields = "__all__"
