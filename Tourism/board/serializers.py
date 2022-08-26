from rest_framework import serializers
from .models import Board,ReviewImg
from django.db import models

from django.conf import settings

class BoardSerializer(serializers.ModelSerializer):

    # def get_something(self, obj):
    #   if not hasattr(obj, 'id'):
    #     return None
    #   if not isinstance(obj,'id'):
    #     return None
    #   return obj.get_somethingfield()

    def to_representation(self, instance):
      res = super().to_representation(instance)
      res.update({'writer': instance.writer.__str__()}) 
      return res

    class Meta:
        model=Board
        fields = ['id','title','writer','content','created_at','updated_at']
        read_only_fields = ['writer','created_at','updated_at']
        # lookup_field = 'writer'
        # read_only_fields = ['created_at']
        # fields = "__all__"

class ImgSerializer(serializers.ModelSerializer):
      class Meta:
        model=ReviewImg
        fields = ['user_id','image_name','image_url']