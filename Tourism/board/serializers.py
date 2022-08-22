from rest_framework import serializers
from .models import Board
from django.db import models

from django.conf import settings

class BoardSerializer(serializers.ModelSerializer):
    # title = serializers.CharField()
    # fk_writer = serializers.CharField(source="writer")
    # content = serializers.CharField()
    # created_at = serializers.DateTimeField()

    # accessUser = serializers.RelatedField( read_only=True)
    def to_representation(self, instance):
      res = super().to_representation(instance)
      res.update({'writer': instance.writer.__str__()}) 
      return res

    class Meta:
        model=Board
        fields = ['id','title','writer','content','created_at','updated_at']
        read_only_fields = ['writer','created_at','updated_at']
        # read_only_fields = ['created_at']
        # fields = "__all__"
