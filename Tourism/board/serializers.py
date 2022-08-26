from rest_framework import serializers
from .models import Board,ReviewImg
from django.db import models

from django.conf import settings

class ImgSerializer(serializers.ModelSerializer):
      class Meta:
        model=ReviewImg
        fields = ['image_name','image_url']

class BoardSerializer(serializers.ModelSerializer):

    # reviewimgs = ImgSerializer(many=True, read_only=True)
    img_list = serializers.SerializerMethodField('_get_imgs')

    def _get_imgs(self, obj):

      serializer = ImgSerializer(obj.reviewimg_set.all(),many=True)
      return serializer.data

    def to_representation(self, instance):
      res = super().to_representation(instance)
      res.update({'writer': instance.writer.__str__()}) 
      return res

    class Meta:
        model=Board
        fields = ['id','title','writer','content','created_at','updated_at','img_list']
        read_only_fields = ['writer','created_at','updated_at','img_list']
        # lookup_field = 'writer'
        # read_only_fields = ['created_at']
        # fields = "__all__"

