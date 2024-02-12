from django.shortcuts import render
from rest_framework.decorators import action
from . import models
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from . import serializers, permissions


# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = models.Women.objects.all()
#     serializer_class = serializers.WomenSerializer
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = models.Category.objects.get(pk=pk)
#         return Response({'cats': cats.name for c in cats})


class WomenAPIList(generics.ListAPIView):
    queryset = models.Women.objects.all()
    serializer_class = serializers.WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = models.Women.objects.all()
    serializer_class = serializers.WomenSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly, )


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Women.objects.all()
    serializer_class = serializers.WomenSerializer
    permission_classes = (permissions.IsAdminOrReadOnly, )


