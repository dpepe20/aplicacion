from django.shortcuts import render
from app.models import *
from .serializer import *
from django.contrib.auth.models import *
from rest_framework import viewsets

from django.contrib.auth.models import User, Group,UserManager
from service.serializer import GroupSerializer
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

####################api############################

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse


from .serializer import RegisterSerializer
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from .models import DriverUser




from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication


from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import (
	AllowAny,
	)

class Register(CreateAPIView):
	#permission_classes = (AllowAny,permissions.IsAuthenticated)

	serializer_class = RegisterSerializer
	queryset = DriverUser.objects.all()



####################api############################

#USER



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#USER

class descarga_views(viewsets.ModelViewSet):
	queryset = Descarga.objects.all()
	serializer_class = descarga_serializer

class estreno_views(viewsets.ModelViewSet):
	queryset = Extreno.objects.all()
	serializer_class = estreno_serializer
	


###PELICULA####
class pelicula_views(viewsets.ModelViewSet):
	
	queryset = Pelicula.objects.all()
	serializer_class = pelicula_serializer
###PELICULA####
#############################################################





class genero_views(viewsets.ModelViewSet):
	queryset = Genero.objects.all()
	serializer_class = genero_serializer

class filtro_views(viewsets.ModelViewSet):
	queryset  = Filtro.objects.all()
	serializer_class = filtro_serializer

class recomendacion_views(viewsets.ModelViewSet):
	queryset = Recomendacion.objects.all()
	serializer_class = recomendacion_serializer