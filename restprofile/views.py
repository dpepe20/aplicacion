from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .permissions import  IsOwnerOrReadOnly

from rest_framework.generics import (
	RetrieveUpdateAPIView, 
	DestroyAPIView,
	ListAPIView)


from restprofile.serializer import *


from rest_framework.permissions import (
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,)

from rest_framework import viewsets
from django.contrib.auth.models import User


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


from app.models import Pelicula,Genero
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response





from django.http import HttpResponse
from app.forms import *





from restprofile.urls import *

from rest_framework import serializers





from rest_framework.serializers import (
	ModelSerializer,
)





class ListAuthor(ListAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	serializer_class = listUserSerializer
 
	
	def get_queryset(self, *args, **kwargs):
		return Pelicula.objects.all().filter()
		#(id=self.request.user.id)


class DeletePost(DestroyAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = deleteSerializer
	lookup_field = 'id'
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	authentication_classes = (TokenAuthentication, SessionAuthentication)


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = updateSerializer
	lookup_field = 'id'
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	authentication_classes = (TokenAuthentication, SessionAuthentication)
