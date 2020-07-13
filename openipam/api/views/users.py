from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from openipam.api.permissions import IPAMAPIAdminPermission
from openipam.api.serializers.users import UserSerializer, GroupSerializer
from openipam.api.singular_url_logger import singular_url_logger

User = get_user_model()


class UserList(generics.ListAPIView):
    queryset = User.objects.prefetch_related("user_permissions").all()
    permission_classes = (permissions.IsAuthenticated, IPAMAPIAdminPermission)
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("groups__name", "username", "email")

    def get(self, request, format=None):
        singular_url_logger(request)
        return super().get(request, format)


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticated, IPAMAPIAdminPermission)
    serializer_class = GroupSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("name",)

    def get(self, request, format=None):
        singular_url_logger(request)
        return super().get(request, format)


class GroupOptionsList(APIView):
    permission_classes = (permissions.IsAuthenticated, IPAMAPIAdminPermission)

    def get(self, request, format=None):
        singular_url_logger(request)
        name = request.GET.get("term")
        if name:
            queryset = Group.objects.filter(name__istartswith=name)
        else:
            queryset = Group.objects.none()
        groups = [{"text": group.name, "value": group.name} for group in queryset]
        return Response(groups)
