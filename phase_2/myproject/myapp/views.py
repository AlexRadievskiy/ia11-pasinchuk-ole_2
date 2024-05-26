from rest_framework import viewsets
from .models import ParentResource
from .serializers import ParentResourceSerializer

class ParentResourceViewSet(viewsets.ModelViewSet):
    queryset = ParentResource.objects.all()
    serializer_class = ParentResourceSerializer
