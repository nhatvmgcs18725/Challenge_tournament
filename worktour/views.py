from rest_framework import generics

from preworktour.models import driverPost
from .serializers import driverPostSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, DjangoModelPermissions, SAFE_METHODS
from django.shortcuts import render


class PostUserWrite(BasePermission):
    message = 'edit by author'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class Post(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = driverPost.Post.all()
    serializer_class = driverPostSerializer


class ListpostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWrite):
    permission_classes = [PostUserWrite]
    queryset = driverPost.Post.all()
    serializer_class = driverPostSerializer


def ttest(request):
    return render(request, 'index.html', {})


def room(request, chatchit):
    return render(request, 'chatroom.html', {
        'chatchit': chatchit})
