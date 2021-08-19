from rest_framework import serializers
from app.models import *



from django.contrib.auth.models import User, Group
############################################################
from rest_framework.serializers import (
	ModelSerializer,
	ValidationError,
	EmailField,
)
from app.models import Pelicula
from app.models import Genero
from app.models import Filtro

from app.models import Descarga
from app.models import Recomendacion


from service.models import DriverUser

class RegisterSerializer(ModelSerializer):
	email = EmailField(label='Email adress')
	class Meta:
		model = DriverUser
		fields = [
			'id',
			'username',
			'password',
			'email',
		]
	extra_kwargs = {"password":
					{"write_only":True},
					"id":
					{"read_only":True}
					}

	def validate(self, data):
		return data

	def validate_email(self, value):
		email = value
		user_qs = DriverUser.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError("Email alredy registred")
		return value


	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		email = validated_data['email']
		user_obj = DriverUser(
			username = username,
			password = password,
			email = email,
		)
		user_obj.set_password(password)
		user_obj.save()
		return user_obj
#############################################################




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']





class descarga_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Descarga
		fields = ('url','des_Nombre','link','fotejes','descripcion')


class estreno_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Extreno
		fields = ('url','ext_Nombree','ext_Idioma','ext_descripcion','fecha_estreno','imagenes')

class pelicula_serializer(serializers.ModelSerializer):

	
	class Meta:
		model = Pelicula
		fields =('url','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')

class genero_serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model  = Genero
		fields = '__all__'

class filtro_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Filtro
		fields = '__all__'

class recomendacion_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Recomendacion
		fields = '__all__'
