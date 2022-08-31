from rest_framework import serializers
from .models import Board,ReviewImg
from django.db import models

from django.conf import settings

class ImgSerializer(serializers.ModelSerializer):
      class Meta:
        model=ReviewImg
        fields = ['id','image_name','image_url']
        # fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    # img = ImgSerializer()
    # reviewimgs = ImgSerializer(many=True, read_only=True)
    img_list = serializers.SerializerMethodField(method_name='_get_imgs')

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
        read_only_fields = ['writer','created_at','updated_at']
        # lookup_field = 'writer'
        # read_only_fields = ['created_at']
        # fields = "__all__"
