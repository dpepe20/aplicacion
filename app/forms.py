from django import forms
from .models import *
from django.contrib.auth.models import User
from datetime import date
from django.forms import ModelForm,Select
from django.contrib.auth import get_user_model
User = get_user_model()
#REGISTER



class register_form(forms.Form):
	username =forms.CharField(widget=forms.TextInput(attrs={
		'id':'username','class':'form-control','placeholder':'Nombre de Usuario','autofocus':'autofocus',
		}))
	email    =forms.EmailField(widget=forms.TextInput(attrs={
		'id':'email','class':'form-control','placeholder':'Correo Electronico','autofocus':'autofocus',
		}))
	password_1 = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={
		'id':'password','class':'form-control','placeholder':'Contraseña','autofocus':'autofocus',
		}))
	password_2 = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={
		'id':'password2','class':'form-control','placeholder':'placeholder','autofocus':'autofocus',
		}))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('NOMBRE DE USUARIO YA REGISTRADO')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('CORREO ELECTRONICO YA EXISTE')

	def clean_password_2(self):
		password_1 =self.cleaned_data['password_1']
		password_2 =self.cleaned_data['password_2']
		if not len(password_1)>7:
			raise forms.ValidationError('La contraseña debe contener minimo 8 caracteres')
		else:
			pass 
		if password_1==password_2:
			pass
		else:
			raise forms.ValidationError('Las contraseñas no coinciden')


class login_form(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}))

	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class contacto_form(forms.Form):

	# required=True es para decirle que es obligatorio llenar los cuadros
	correo = forms.EmailField(max_length=100,widget = forms.TextInput,required=True)
	titulo = forms.CharField(max_length=400,widget = forms.TextInput,required=True)
	texto = forms.CharField(max_length=1000,widget = forms.Textarea,required=True)


		#PELICULAS

class agregar_pelicula_form(forms.ModelForm):
	class Meta:
		model = Pelicula
		fields = 'nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online'
		widgets= {
		'fecha' : forms.TextInput(attrs={'class' :'form-control datepicker','placeholder':'FECHA' }),
		'descripcion' : forms.Textarea(attrs={
				'id' : 'descripcion','class':'form-control','placeholder':'DESCRIPCION',
										'autofocus': 'autofocus','type' : 'text'
					}),
		'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		'idioma': forms.TextInput(attrs={'class':'form-control','placeholder':'IDIOMA'}),
		'calidad': forms.TextInput(attrs={'class':'form-control','placeholder':'CALIDAD'}),
		'Ver_online': forms.TextInput(attrs={'class':'form-control','placeholder':'VER_ONLINE'}),
		
		
		
		
				}
	



	def clean_nombre(self):
		nombre = self.cleaned_data['nombre']
		words =nombre.split(' ')
		if len(words) >  5:
			raise forms.ValidationError('SOLO CINCO PALABRAS')
		return nombre
	def clean_fecha(self):
		fecha = self.cleaned_data['fecha']
		if (fecha)>date.today():
				raise forms.ValidationError('la fecha tiene que ser pasado de la presente')
		return fecha

		#PELICULAS



class agregar_filtro_form(forms.ModelForm):
	class Meta:
		model = Filtro
		fields = '__all__'
		

class agregar_descarga_form(forms.ModelForm):	
	class Meta:
		model = Descarga
		fields = '__all__'

class agregar_recomendacion_form(forms.ModelForm):
	class Meta:
		model = Recomendacion
		fields = '__all__'


class agregar_estreno_form(forms.ModelForm):
	class Meta:
		model = Extreno
		fields = '__all__'
		widgets={
		'fecha_estreno' : forms.TextInput(attrs={'class' : 'datepicker'})
		}

class agregar_genero_form(forms.ModelForm):
	class Meta:
		model = Genero
		fields = '__all__'
