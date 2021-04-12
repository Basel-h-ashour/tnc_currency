from django.shortcuts import render
from .serializers import FiatSerializer
from .models import Fiat

from rest_framework import viewsets, mixins


class FiatViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, \
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, \
                    mixins.CreateModelMixin):
    serializer_class = FiatSerializer
    queryset = Fiat.objects.all()
