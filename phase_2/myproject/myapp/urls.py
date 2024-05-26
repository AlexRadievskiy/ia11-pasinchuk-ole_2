from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentResourceViewSet

router = DefaultRouter()
router.register(r'parent-resources', ParentResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
