from rest_framework.serializers import ModelSerializer
from accounts.models import User

class NoteSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'