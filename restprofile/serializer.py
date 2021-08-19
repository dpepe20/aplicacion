from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from app.models import Genero,Pelicula
from restprofile.views import * 

from restprofile import *
from django.contrib.auth.models import User, Group
from rest_framework.serializers import (
	ModelSerializer,
)
class listUserSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields =('url','id','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')

class deleteSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields = ('id',)	
		
class updateSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields =('id','url','id','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')
