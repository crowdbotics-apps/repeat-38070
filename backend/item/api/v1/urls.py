
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ItemViewSet
router = DefaultRouter()
router.register('item', ItemViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
