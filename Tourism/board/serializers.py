from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields = "__all__"
        # fields = ('b_title', 'b_writer', 'b_date')

