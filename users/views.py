from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from users.models import User
from users.serializers import UserSerializer

@method_decorator(cache_page(60 * 15), name='list')
@method_decorator(cache_page(60 * 15), name='retrieve')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer