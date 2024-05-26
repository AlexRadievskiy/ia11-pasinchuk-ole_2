from rest_framework import serializers
from .models import ParentResource

class ParentResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentResource
        fields = '__all__'
