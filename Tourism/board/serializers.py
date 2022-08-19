from asyncio.windows_events import NULL
from rest_framework import serializers
from .models import Board
from django.db import models

from django.conf import settings

class BoardSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="b_title")
    writer = serializers.CharField(source="b_writer")
    date = serializers.DateTimeField(source="b_date")
    # accessUser = serializers.RelatedField( read_only=True)
    def to_representation(self, instance):
      res = super().to_representation(instance)
      res.update({'accessUser': instance.accessUser.__str__()}) 
      return res

        # return {
        #   'accessUser' : instance.accessUser.get_username(),
        #   'id': instance.id,
        #   'title' :instance.b_title,
        #   'writer':instance.b_writer,
        #   'date':instance.b_date,
        # }



    class Meta:
        model=Board
        fields = ['accessUser','id','title','writer','date']
        # fields = "__all__"
        # fields = ('b_title', 'b_writer', 'b_date')
        
        # ex)
        # verbose_name = 'accessUser'
        # db_table = "job"
        # ordering = ["-dateTimeOfPosting"]
