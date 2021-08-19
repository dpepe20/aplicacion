
from django.urls.conf import path
from .views import *

urlpatterns = [
path('contacto/',contacto,name='contacto'),
path('',vista_login,name ='vista_login'),
path('logout/',vista_logout,name='vista_logout'),
path('register/',register_user,name='register_user'),
path('inicio/',inicio,name='inicio'),
path('peliculas/',pagina_peliculas,name='pagina_peliculas'),
path('foro/',foro_vista,name='vista_foro'),
		#LISTA_PELICULAS
		#Lista_Peliculas
path('lista_peliculas/',vista_peliculas, name='lista_peliculas'),
path('agregar_pelicula/',vista_agregar_pelicula, name = 'vista_agregar_pelicula'),
path('ver_peliculas/<int:id_peli>/',vista_ver_pelicula, name = 'vista_ver_pelicula'),
path('editar_pelicula/<int:id_peli>/',vista_editar_pelicula, name='vista_editar_pelicula'),
path('eliminar_pelicula/<int:id_peli>/',vista_eliminar_pelicula, name='vista_eliminar_pelicula' ),
		#Lista_Filtro
		#Lista_Filtro
path('filtro/',lista_filtro, name='lista_filtro'),
path('agregar_filtro/',vista_agregar_filtro, name = 'vista_agregar_filtro'),
path('editar_filtro/<int:id_fil>/',vista_editar_filtro, name='vista_editar_filtro'),
path('eliminar_filtro/<int:id_fil>/',vista_eliminar_filtro, name='vista_eliminar_filtro' ),

		# Descarga
		# Descarga
path('descarga/',lista_descarga, name='lista_descarga'),
path('agregar_descarga/',vista_agregar_descarga, name = 'vista_agregar_descarga'),
path('editar_descarga/<int:id_des>/',vista_editar_descarga, name='vista_editar_descarga'),
path('eliminar_descarga/<int:id_des>/',vista_eliminar_descarga, name='vista_eliminar_descarga' ),
		#RECOMENDACION
		#RECOMENDACION
path('recomendacion/',lista_recomendacion, name='lista_recomendacion'),
path('agregar_recomendacion/',vista_agregar_recomendacion, name = 'vista_agregar_recomendacion'),
path('editar_recomendacion/<int:id_rec>/',vista_editar_recomendacion, name='vista_editar_recomendacion'),
path('eliminar_recomendacion/<int:id_rec>/',vista_eliminar_recomendacion, name='vista_eliminar_recomendacion'),

				#estreno
				#estreno

path('estreno/',lista_estreno, name='lista_estreno'),
path('agregar_estreno/',vista_agregar_estreno, name = 'vista_agregar_estreno'),
path('editar_estrenos/<int:id_est>/',vista_editar_estreno, name='vista_editar_estreno'),
path('eliminar_estreno/<int:id_est>/',vista_eliminar_estreno, name='vista_eliminar_estreno'),

			#GENERO
			#GENERO

path('generos/',lista_genero, name='lista_genero'),
path('agregar_genero/',vista_agregar_genero, name = 'vista_agregar_genero'),
path('editar_genero/<int:id_gen>/',vista_editar_genero, name='vista_editar_genero'),
path('eliminar_genero/<int:id_gen>/',vista_eliminar_genero, name='vista_eliminar_genero'),



 					# Login
 					# Login
]