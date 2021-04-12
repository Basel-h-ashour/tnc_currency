from django.contrib import admin
from django.urls import path, include
from .views import FiatViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('fiats', FiatViewSet)


urlpatterns = [
    path('', include(router.urls)),
]