from django.urls import path, include
from rest_framework import routers
from app.models import *
from service.views import *
####		1		###
from service import views
from django.conf.urls import include ,url
from rest_framework.authtoken import views as authviews

####		end 1	###
from django.contrib import admin

router = routers.DefaultRouter()

router.register(r'groups', GroupViewSet)

router.register(r'Descarga',descarga_views)
router.register(r'Extreno',estreno_views)
router.register(r'v1/Pelicula',pelicula_views)
router.register(r'Genero',genero_views)
router.register(r'Filtro',filtro_views)
router.register(r'Recomendacion',recomendacion_views)



urlpatterns =	[
	path('api/',include(router.urls)),

	path('register',views.Register.as_view(),name='register'),
	
	
	
	path('api-token-auth/',authviews.obtain_auth_token, name='api-token-auth'),
	
	
]