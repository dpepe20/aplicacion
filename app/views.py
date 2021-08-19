from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from.forms import contacto_form
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
import json
from django.db.models import Q 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import LoginView

class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)

#register 


def register_user(request):
	formulario = register_form()
	if request.method=="POST":
		formulario =register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			email = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario,email=email,password=password_1)
			u.save()
			return render(request,'gracias_register.html',locals())
		else:
			return render(request,'register.html',locals())
	return render(request,'register.html',locals())




def vista_login(request):
	usu=""
	cla=""
	if request.method=='POST':
		formulario =login_form(request.POST)
		if formulario.is_valid():
			usu=formulario.cleaned_data['user']
			cla=formulario.cleaned_data['password']
			usuario=authenticate(username=usu,password=cla)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return redirect('/inicio/')
			else:
				msj = "Usuario o Clave Incorrectos"
	else:
		formulario=login_form()
	return render(request,'login.html',locals())


def vista_logout(request):
	logout(request)
	return redirect('vista_login')
	
@login_required(login_url='vista_login')
def contacto(renquest):
	info_enviado =False
	email = ""
	title = ""
	text = ""
	if renquest.method == "POST":
		formulario = contacto_form(renquest.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
	else:
		formulario = contacto_form()
	return render (renquest,'contacto.html', locals())

@login_required(login_url='vista_login')
def inicio(renquest):
	genero=Genero.objects.all()
	return render(renquest,'inicio.html')

@login_required(login_url='vista_login')
def pagina_peliculas(renquest):
	return render (renquest,'peliculas.html')

def foro_vista(renquest):
	return render(renquest,'foro.html')

		#PELICULAS
		#PELICULAS
		#
		
		#





@login_required(login_url='vista_login')
def  vista_peliculas(request):
	queryset = request.GET.get("buscar")
	lista = Pelicula.objects.filter()
	if queryset:
		lista=Pelicula.objects.filter(
			Q(nombre__icontains=queryset) 
			#| 
			#Q(descripcion__icontains=queryset)
			).distinct()
	paginator = Paginator(lista,3)
	page =request.GET.get('page')
	lista = paginator.get_page(page)

	return render(request, 'lista_peliculas.html', locals())




@staff_member_required(login_url='vista_login')
def vista_agregar_pelicula(request):
	if request.method == 'POST':
		formulario = agregar_pelicula_form(request.POST, request.FILES)
		if formulario.is_valid():
			peli = formulario.save(commit = False)
			peli.status = True
			peli.save()
			formulario.save_m2m()
			return redirect ('/lista_peliculas/')
	else:
		formulario = agregar_pelicula_form()
	return render(request, 'vista_agregar_pelicula.html', locals()) 



@login_required(login_url='vista_login')
def vista_ver_pelicula(request,id_peli):
	p = Pelicula.objects.get(id=id_peli)
	return render(request,'ver_pelicula.html',locals())

@staff_member_required(login_url='vista_login')
def vista_editar_pelicula(request, id_peli):
	peli = Pelicula.objects.get(id=id_peli)
	if request.method == "POST":
		formulario = agregar_pelicula_form(request.POST, request.FILES, instance=peli)
		if formulario.is_valid():
			peli = formulario.save()
			return redirect ('/lista_peliculas/')
	else:
		formulario = agregar_pelicula_form(instance = peli)
	return render(request, 'vista_agregar_pelicula.html',locals())


@staff_member_required(login_url='vista_login')
def vista_eliminar_pelicula(request, id_peli):
	peli = Pelicula.objects.get(id=id_peli)
	peli.delete()
	return redirect ('/lista_peliculas/')


	#Filtros
	#Filtros
@login_required(login_url='vista_login')
def lista_filtro(request):
	lista = Filtro.objects.filter()
	return render(request, 'lista_filtro.html', locals())

@staff_member_required(login_url='vista_login')
def vista_agregar_filtro(request):
	if request.method == 'POST':
		formulario = agregar_filtro_form(request.POST, request.FILES)
		if formulario.is_valid():
			peli = formulario.save(commit = False)
			peli.status = True
			peli.save()
			formulario.save_m2m()
			return redirect ('/filtro/')
	else:
		formulario = agregar_filtro_form()
	return render(request, 'vista_agregar_filtro.html', locals()) 

@staff_member_required(login_url='vista_login')
def vista_editar_filtro(request, id_fil):
	fil = Filtro.objects.get(id=id_fil)
	if request.method == "POST":
		formulario = agregar_filtro_form(request.POST, request.FILES, instance=fil)
		if formulario.is_valid():
			fil = formulario.save()
			return redirect ('/filtro/')
	else:
		formulario = agregar_filtro_form(instance = fil)
	return render(request, 'vista_agregar_filtro.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_filtro(request, id_fil):
	peli = Filtro.objects.get(id=id_fil)
	peli.delete()
	return redirect ('/filtro/')

		#DESCARGAS
		#DESCARGAS
@login_required(login_url='vista_login')
def lista_descarga(request):
	lista = Descarga.objects.filter()
	return render(request, 'lista_descarga.html', locals())

@staff_member_required(login_url='vista_login')
def vista_agregar_descarga(request):
	if request.method == 'POST':
		formulario = agregar_descarga_form(request.POST, request.FILES)
		if formulario.is_valid():
			peli = formulario.save(commit = False)
			peli.status = True
			peli.save()
			formulario.save_m2m()
			return redirect ('/descarga/')
	else:
		formulario = agregar_descarga_form()
	return render(request, 'vista_agregar_descarga.html', locals()) 

@staff_member_required(login_url='vista_login')
def vista_editar_descarga(request, id_des):
	des= Descarga.objects.get(id=id_des)
	if request.method == "POST":
		formulario = agregar_descarga_form(request.POST, request.FILES, instance=des)
		if formulario.is_valid():
			des = formulario.save()
			return redirect ('/descarga/')
	else:
		formulario = agregar_descarga_form(instance = des)
	return render(request, 'vista_agregar_descarga.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_descarga(request, id_des):
	peli = Descarga.objects.get(id=id_des)
	peli.delete()
	return redirect ('/descarga')

	#RECOMENDACIONES
	#RECOMENDACIONES
@login_required(login_url='vista_login')
def lista_recomendacion(request):
	lista = Recomendacion.objects.filter()
	return render(request, 'lista_recomendacion.html', locals())

@staff_member_required(login_url='vista_login')
def vista_agregar_recomendacion(request):
	if request.method == 'POST':
		formulario = agregar_recomendacion_form(request.POST, request.FILES)
		if formulario.is_valid():
			peli = formulario.save(commit = False)
			peli.status = True
			peli.save()
			formulario.save_m2m()
			return redirect ('/recomendacion/')
	else:
		formulario = agregar_recomendacion_form()
	return render(request, 'vista_agregar_recomendacion.html', locals()) 

@staff_member_required(login_url='vista_login')
def vista_editar_recomendacion(request, id_rec):
	rec= Recomendacion.objects.get(id=id_rec)
	if request.method == "POST":
		formulario = agregar_recomendacion_form(request.POST, request.FILES, instance=rec)
		if formulario.is_valid():
			rec = formulario.save()
			return redirect ('/recomendacion/')
	else:
		formulario = agregar_recomendacion_form(instance = rec)
	return render(request, 'vista_agregar_recomendacion.html',locals())

@staff_member_required(login_url='vista_login')
def vista_eliminar_recomendacion(request, id_rec):
	peli = Recomendacion.objects.get(id=id_rec)
	peli.delete()
	return redirect ('/recomendacion/')

			#ESTRENO
			#ESTRENO
@login_required(login_url='vista_login')
def lista_estreno(request):
	lista = Extreno.objects.filter()
	return render(request, 'lista_estreno.html', locals())

@staff_member_required(login_url='vista_login')
def vista_agregar_estreno(request):
	if request.method == 'POST':
		formulario = agregar_estreno_form(request.POST, request.FILES)
		if formulario.is_valid():
			peli = formulario.save(commit = False)
			peli.status = True
			peli.save()
			formulario.save_m2m()
			return redirect ('/estreno/')
	else:
		formulario = agregar_estreno_form()
	return render(request, 'vista_agregar_estreno.html', locals()) 

@staff_member_required(login_url='vista_login')
def vista_editar_estreno(request, id_est):
	est = Extreno.objects.get(id=id_est)
	if request.method == "POST":
		formulario = agregar_estreno_form(request.POST, request.FILES, instance=est)
		if formulario.is_valid():
			est = formulario.save()
			return redirect ('/estreno/')
	else:
		formulario = agregar_estreno_form(instance = est)
	return render(request, 'vista_agregar_estreno.html',locals())


@staff_member_required(login_url='vista_login')
def vista_eliminar_estreno(request, id_est):
	peli = Extreno.objects.get(id=id_est)
	peli.delete()
	return redirect ('/estreno/')


		#GENERO
		#GENERO
@login_required(login_url='vista_login')
def lista_genero(request):
	lista = Genero.objects.filter()
	return render(request, 'lista_genero.html', locals())
@staff_member_required(login_url='vista_login')
def vista_agregar_genero(request):
	if request.method == 'POST':
		formulario = agregar_genero_form(request.POST, request.FILES)
		if formulario.is_valid():
			peli = formulario.save(commit = False)
			peli.status = True
			peli.save()
			formulario.save_m2m()
			return redirect ('/generos/')
	else:
		formulario = agregar_genero_form()
	return render(request, 'vista_agregar_genero.html', locals()) 

@staff_member_required(login_url='vista_login')
def vista_editar_genero(request,id_gen):
	gen = Genero.objects.get(id=id_gen)
	if request.method == "POST":
		formulario = agregar_genero_form(request.POST,request.FILES, instance=gen)
		if formulario.is_valid():
			gen = formulario.save()
			return redirect ('/generos/')
	else:
		formulario = agregar_genero_form (instance = gen)
		
	return render(request, 'vista_agregar_genero.html',locals())
	
@staff_member_required(login_url='vista_login')
def vista_eliminar_genero(instance, id_gen):
	peli = Genero.objects.get(id=id_gen)
	peli.delete()
	return redirect ('/generos/')


		# LOGIN
		# LOGIN


