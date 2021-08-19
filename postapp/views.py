from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse


from postapp.serializer import *

from app.forms import *
from postapp.urls import *

from app.models import *
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from rest_framework import serializers

from rest_framework.permissions import (
	IsAuthenticated,
	)


from rest_framework.serializers import (
	ModelSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

class PostListAPIView(ListAPIView):
	serializer_class = listSerializer
	queryset = Pelicula.objects.all()


class AddPost(CreateAPIView):
	#authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = addSerializer
	queryset = Pelicula.objects.all()

	def perform_create(self, serializer):
		serializer.save(nombre = self.request.user.id)



class ShowPost(RetrieveAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = showSerializer
	lookup_field = 'id'


class GeneroAllAPIView(ListAPIView):
	serializer_class = listGeneroSerializer
	queryset = Genero.objects.all()


class CategoryIdAPIView(ListAPIView):
	serializer_class = listSerializer

	def get_queryset(self):
		return Pelicula.objects.filter(id=self.kwargs['id'])