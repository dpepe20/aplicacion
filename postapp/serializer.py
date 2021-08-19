from rest_framework import serializers


from app.models import Genero,Pelicula



from django.contrib.auth.models import User, Group



from rest_framework.serializers import (
	ModelSerializer,
)

class listSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields =('id','url','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')



class addSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields =('url','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')


class showSerializer(ModelSerializer):
	class Meta:
		model = Pelicula
		fields =('url','id','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')


class listGeneroSerializer(ModelSerializer):
	class Meta:
		model  = Genero
		fields ='__all__'
		
