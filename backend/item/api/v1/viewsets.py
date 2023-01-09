from rest_framework import authentication
from item.models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Item.objects.all()