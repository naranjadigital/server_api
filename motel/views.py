from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from motel.models import *
from motel.serializers import *


class ApiMotelList(generics.ListCreateAPIView):
    serializer_class = MotelSerializer
    queryset = Motel.objects.all()


class ApiMotelEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MotelSerializer
    queryset = Motel.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)


class ApiDistritoList(generics.ListCreateAPIView):
    serializer_class = DistritoSerializer
    queryset = Distrito.objects.all()


class ApiDistritoEdit(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication,]
    permission_classes = (IsAuthenticated,)
    serializer_class = DistritoSerializer
    queryset = Distrito.objects.all()