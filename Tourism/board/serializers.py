from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="b_title")
    writer = serializers.CharField(source="b_writer")
    date = serializers.DateTimeField(source="b_date")
    user = serializers.CharField(source="accessUser")

    class Meta:
        model=Board
        fields = ['user','id','title','writer','date']
        # fields = "__all__"
        # fields = ('b_title', 'b_writer', 'b_date')


